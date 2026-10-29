# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## Stretch features (declared before building)

1. **A third signal** — `markers.py::marker_signal`, the density of stock
   phrases generated prose leans on ("it is important to note", "moreover",
   "in conclusion", "delve"). A weighting note goes in *Signals and Scoring*.
2. **`GET /content/<id>`** — returns one item's current status (`decided` or
   `under_review`), its scores and label, rebuilt from the audit log.
3. **A verified-human path** — a writer completes a one-time writing check
   (`POST /verify`): they answer a server-issued prompt, and if that sample
   reads as human the creator earns a `verified_writer` credential. Every later
   submission from that creator shows it in the response and the label.

---

## What This Does

A writing site sends a piece of text; Provenance Guard sends back a guess, a
score, and a sentence the reader sees. The path:

1. **Arrives at `POST /submit`** (`app.py::submit`) as JSON `{text, creator_id}`.
   The route rejects anything it can't judge — missing, empty, non-string, or
   over the length cap — with a `400`/`413` and logs the rejection.
2. **Gets an id.** A `content_id` (UUID) is minted so the writer can appeal and
   the item can be looked up later.
3. **Signal one reads it** (`detector.py::model_signal`): gpt2 measures how
   predictable the text is → `model_score`, 0–1, higher = more AI-like.
4. **Signals two and three measure its shape** (`stylometry.py::style_signal`,
   `markers.py::marker_signal`): sentence-length spread, vocabulary variety,
   punctuation variety, and stock-phrase density → `style_score`,
   `marker_score`.
5. **The combining rule** (`scoring.py::combine_signals`) turns three numbers
   into one `confidence` — and refuses to let it reach the AI band unless every
   signal agrees.
6. **The label mapping** (`scoring.py::score_to_label`) turns that number into
   `guess` (`human` / `unsure` / `ai`) and the plain-English `label`.
7. **Logged, then answered.** `audit.py::log_decision` writes all scores and
   `status: decided` to `logs/audit.jsonl`; the JSON response goes back.
   If the writer disagrees, `POST /appeal` appends an appeal and moves the item
   to `under_review`.

### Endpoint contract

**`POST /submit`**

| In | Type | Rule |
|---|---|---|
| `text` | string | required, non-empty after trimming, ≤ 10,000 characters |
| `creator_id` | string | required, non-empty |

| Out (200) | Type | Meaning |
|---|---|---|
| `content_id` | string | UUID; use it to appeal or look the item up |
| `creator_id` | string | echoed back |
| `guess` | `"human"` \| `"unsure"` \| `"ai"` | machine-readable verdict |
| `confidence` | float 0–1 | combined score; higher = more likely AI |
| `label` | string | the sentence a reader sees |
| `model_score`, `style_score`, `marker_score` | float 0–1 | each signal; higher = more AI-like |
| `status` | `"decided"` | item status |
| `verified_writer` | bool | creator holds the verified-human credential |

Errors: `400 {"error": "invalid_input", "message": ...}` for a missing / empty /
non-string field or a non-JSON body; `413 {"error": "too_long", ...}` above the
cap; `422 {"error": "too_short", ...}` under 20 words — too little for any
signal to mean something. Every rejection is logged with `audit.log_rejection`.

**`POST /appeal`**

| In | Type | Rule |
|---|---|---|
| `content_id` | string | required; must exist in the log |
| `reasoning` | string | required, non-empty — the writer's explanation |

| Out (200) | Type | Meaning |
|---|---|---|
| `content_id` | string | echoed back |
| `status` | `"under_review"` | new status |
| `message` | string | confirmation shown to the writer |

Errors: `400` for missing fields, `404 {"error": "not_found"}` for an unknown
`content_id`.

### Tracing the false positive

A student writing in their second language submits a plain, honest paragraph —
short sentences, common words, nothing ornate. Signal one scores that as
highly predictable: my plain-human test paragraph ("I went to the store
today. I bought milk and bread…") scored **0.85** on `model_score`, higher than
a stock AI paragraph (0.83). If that number alone decided, they'd be told their
work was machine-written.

The style signal may not save them either — even, simple sentences look
AI-like to it too. What stands between them and the accusation is the marker
signal, which finds no stock phrases, and my combining rule, which caps the
score below the AI band whenever any signal disagrees. They land in **unsure**
at worst, with a label that says plainly it is not an accusation and how to
appeal. If they appeal, `POST /appeal` records their reasoning next to the
original decision and the item shows `under_review` to anyone who looks it up.
This scenario is why my AI band starts at 0.85 and requires agreement.

---

## Signals and Scoring

### Signal one — the model signal

**What it measures:** Perplexity under gpt2 — how surprised a language model is
by each next word — squashed onto 0–1 (`detector.py::model_signal`, midpoint
perplexity 45 → 0.5). Low perplexity → high score.

**Why that might differ between human and AI writing:** A model writes by
picking likely next words, so its output is text a model finds easy to
predict. People make odder, more specific choices.

**What it can't see:** Authorship. It rewards common words in ordinary
sentences, so plain human writing — second-language writers, younger writers,
anyone writing simply — scores as machine-like (0.85 in my test above). The
reverse also holds: AI text prompted to use rare words, or with typos added,
reads as human.

### Signal two — the style signal

**What it measures:** The shape of the text with no idea what it says
(`stylometry.py::style_signal`), from three measures, each mapped to 0–1
AI-likeness between two anchors:

| Measure | Raw value | Human anchor → 0 | AI anchor → 1 | Weight |
|---|---|---|---|---|
| `sentence_length_spread` | stdev / mean of sentence lengths | 0.65 | 0.25 | 0.4 |
| `type_token_ratio` | unique words / total, averaged over 50-word windows | 0.86 | 0.72 | 0.2 |
| `punctuation_density` | `; : ! ? ( ) — – … "` per 100 words | 4.0 | 0.0 | 0.4 |

Under 3 sentences the spread measure is replaced by a neutral 0.5.

**Why that might differ between human and AI writing:** Generated prose
marches in even, mid-length sentences with a safe vocabulary and mostly commas
and full stops. Human writing is lumpier — a three-word sentence beside a
forty-word one, a dash, a semicolon.

**What it can't see:** Meaning. Anything that changes the shape without
changing the substance moves it — splitting or merging sentences, adding
dashes, pasting in a quotation. Very short texts give it almost nothing to
measure. And plain writing with no semicolons or dashes maxes out the
punctuation measure — the same writers signal one already misreads.

**A finding from calibration:** type-token ratio ran *backwards* on my short
inputs — the stock AI paragraph had the most varied vocabulary (0.92) of all
five, because generated prose avoids repeating words. That's why it carries
half the weight of the other two.

### Signal three — the marker signal (stretch)

**What it measures:** How often the text uses phrases generated prose leans on
— "it is important to note", "moreover", "plays a crucial role", "in
conclusion" — per 100 words (`markers.py::marker_signal`).

**Why that might differ between human and AI writing:** Chat models are tuned
toward a recognisable register of signposting and hedging; most people don't
write "furthermore" in a poem.

**What it can't see:** Anything outside its list. One pass of paraphrasing
removes every marker, and a human who writes formal essays with those
connectives gets marked up.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** A weighted average of the three signals, then an agreement
check. If *any* signal is below 0.60, the score is capped at 0.84 — one point
under the AI band — so the item can land in unsure but never in AI. Two methods
disagreeing is uncertainty, and uncertainty should never accuse anyone.

**The numbers:** (`config.py`)

| Setting | Value |
|---|---|
| `WEIGHT_MODEL_SIGNAL` | 0.50 |
| `WEIGHT_STYLE_SIGNAL` | 0.25 |
| `WEIGHT_MARKER_SIGNAL` | 0.25 |
| `AGREEMENT_FLOOR` | 0.60 (cap at `AI_THRESHOLD − 0.01` = 0.84 below it) |
| `HUMAN_THRESHOLD` | 0.40 |
| `AI_THRESHOLD` | 0.85 |

**How the three are weighted against each other (stretch note):** The model
signal gets half because it's the only one that reads the words; the style and
marker signals split the other half because each is trivially cheap to fool on
its own — reshape sentences, or paraphrase out the stock phrases. Weighting
alone isn't what protects writers, though: the agreement floor is. With it, the
cheapest signal to fool can veto an AI label but can never create one.

**Calibration run** (through `POST /submit`):

| Input | model | style | marker | confidence | guess |
|---|---|---|---|---|---|
| clearly AI (generated, stock phrases) | 0.868 | 0.782 | 1.000 | 0.879 | ai |
| clearly human (casual, personal) | 0.473 | 0.005 | 0.000 | 0.238 | human |
| plain human (short, common words) | 0.821 | 0.876 | 0.000 | 0.629 | unsure |
| formal human (Gettysburg Address, 1863) | 0.727 | 0.758 | 0.000 | 0.553 | unsure |
| lightly-edited AI (markers removed) | 0.687 | 0.642 | 0.000 | 0.504 | unsure |

The casual and plain "human" inputs are stand-ins written for calibration; the
student's own writing replaces them in unit 8's criteria runs.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

The plain human paragraph. Signal one (0.82) and signal two (0.88) both read
it as AI — short common words, even sentences, no expressive punctuation. The
marker signal finds nothing (0.00). The weighted average is 0.63, and because
the marker signal is under the 0.60 floor the cap applies anyway: it lands in
**unsure**, not AI. That's exactly the writer from *Tracing the false
positive*. With only the first two signals averaged it would have scored
0.849 — a hair under the AI line, held there by luck rather than by a rule.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |  |  |
| unsure |  |  |
| high-confidence AI |  |  |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

*Milestone 3 run — one signal, placeholders for confidence and label:*

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Artificial intelligence is transforming the way we live and work. It is important to note that these technologies offer significant benefits. Moreover, they present challenges that must be carefully considered.", "creator_id": "writer_01"}'
```

```json
{
  "confidence": null,
  "content_id": "a522fc16-f200-4346-a294-d435bf25ee3c",
  "creator_id": "writer_01",
  "guess": null,
  "label": "PLACEHOLDER \u2014 scoring not built yet",
  "model_score": 0.8515,
  "status": "decided",
  "style_score": null
}
```

Log entry (`GET /log?limit=1`):

```json
{
  "combined_score": null,
  "content_id": "a522fc16-f200-4346-a294-d435bf25ee3c",
  "creator_id": "writer_01",
  "guess": null,
  "label": "PLACEHOLDER \u2014 scoring not built yet",
  "model_score": 0.8515,
  "status": "decided",
  "style_score": null,
  "timestamp": "2026-10-29T01:56:07+00:00"
}
```

A refused request still leaves a trace — `{"text": "Hi", "creator_id": "x"}`
returns `422 {"error": "too_short", "message": "text needs at least 20 words to score."}`
and logs:

```json
{"creator_id": "x", "event": "rejected", "http_status": 422, "reason": "too_short", "status": "rejected", "timestamp": "2026-10-29T01:56:07+00:00"}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*
- *What came back:*
- *What I changed:*

**Moment 2**

- *What I asked for:*
- *What came back:*
- *What I changed:*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
