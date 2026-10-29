# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---

## 1. My own writing is never labeled AI

**Criterion:** Of 10 paragraphs I wrote myself, none gets `guess: "ai"` in any
trial, and at least 6 of the 10 get `guess: "human"` in every trial.

**Target:** `ai` = 0 of 10 **and** `human` ≥ 6 of 10, in all 3 trials.

**How to test:**
1. Put the 10 paragraphs in `scenarios.py` under the scenario `"my own writing"`.
   Each is 100–300 words, written with no AI help. At least 3 are written on
   purpose in short, plain sentences with common words.
2. Run `python run_eval.py` three times.
3. In each trial, count the results with `guess == "ai"` and with
   `guess == "human"`.

**Why this target:** Telling a real writer their work is AI-generated is the
most expensive mistake this service can make. The AI band needs all three
signals ≥ 0.60, so if my own writing is labeled `ai`, the agreement rule failed
on exactly the case it exists for. The human floor is there because labeling
everything "unsure" would pass the first half with no effort — and plain
writing already scores 0.85 on `model_score`, so I don't demand all 10.

---

## 2. AI text and human text score clearly apart

**Criterion:** Across 5 AI-generated and 5 known-human paragraphs, the AI set's
average `confidence` is at least 0.30 higher than the human set's, in every
trial.

**Target:** mean(`confidence`, AI set) − mean(`confidence`, human set) ≥ 0.30,
in all 3 trials.

**How to test:**
1. **AI set** (scenario `"spread ai"`): 5 paragraphs from one chat model, each
   made with the same prompt — *"Write a 150-word explanatory paragraph about
   [topic]."* — on 5 different topics. Save the output exactly as generated, with
   the model name and prompt in a comment.
2. **Human set** (scenario `"spread human"`): 5 paragraphs of 100+ words
   published before December 2019, with each source in a comment. None reused
   from criterion 1.
3. Run `python run_eval.py` three times. In each trial, subtract the human
   set's mean `confidence` from the AI set's.

**Why this target:** On `model_score` alone the gap runs the wrong way — my
plain human test paragraph scored 0.85 and a stock AI paragraph 0.83. This
criterion checks that the style and marker signals actually reverse that. A
gap under 0.30 would leave both sets inside the 0.40–0.85 unsure band, and the
labels would tell a reader nothing.

---

## 3. All three labels are reachable

**Criterion:** On 9 inputs, 3 built for each label, each label comes back for
at least 2 of its 3 inputs in every trial, and every `label` string exactly
matches one of the three texts in README → Label Variants.

**Target:** ≥ 2 of 3 per label, for all three labels, in all 3 trials, and
9 of 9 `label` strings matching the README.

**How to test:**
1. Scenario `"coverage"`:
   - **AI ×3:** stock AI paragraphs containing at least 2 phrases from the
     list in `markers.py`.
   - **Human ×3:** my own writing in my normal style, not reused from
     criterion 1.
   - **Borderline ×3:** half of one of my own paragraphs joined to half of an
     AI paragraph on the same topic.
2. Run `python run_eval.py` three times.
3. In each trial, check AI inputs → `ai`, human → `human`, borderline →
   `unsure`, and that each `label` equals the README text for its `guess`.

**Why this target:** My thresholds are deliberately cautious, and that has a
cost: if any signal stays under 0.60, the 0.84 cap makes the `ai` label
unreachable and the detector is useless in practice. Borderline text is where
the signals should split, so it is the input that should land in unsure.

---

## 4. Every appeal changes status and is recorded

**Criterion:** For 5 real `content_id`s, `POST /appeal` returns `under_review`
and adds an appeal entry to the log while the original decision entry stays
unchanged. An unknown id returns 404 and writes nothing.

**Target, per trial:**
- 5 of 5 appeals return 200 with `status: "under_review"`.
- 5 of 5 ids get exactly one new log entry with `event: "appeal"`,
  `status: "under_review"` and the exact reasoning sent, placed after the
  decision entry.
- 5 of 5 original `decided` entries are byte-identical to the saved log.
- An unknown id → 404 `not_found`, with no new log entry.
- Missing `reasoning` → 400.
- `GET /content/<id>` (stretch) shows `under_review` for 5 of 5.

**How to test** (by hand — `run_eval.py` only calls `/submit`):
1. Submit 5 texts, at least one that comes back `human` and one `unsure`.
   Note each `content_id`.
2. Save the output of `GET /log`.
3. Send `POST /appeal` for each id with `reasoning: "I wrote this myself."`
4. Send one appeal with a made-up UUID, and one with a valid id but no
   `reasoning`.
5. Run `GET /log` again and compare against the saved copy. Call
   `GET /content/<id>` for each id.
6. Repeat three times, for three trials.

**Why this target:** An appeal is the only remedy a writer has against a false
positive, so a single dropped appeal leaves someone wrongly marked with no
record that they objected. The original decision has to survive unchanged,
because the append-only log is the evidence in a dispute.

---

## 5. Bad input is refused, logged, and never scored

**Criterion:** Each of 9 malformed requests gets its specified status code
(never 200 or 500) and a `rejected` log entry. A text of exactly 10,000
characters is still accepted.

**Target, per trial:** 9 of 9 malformed requests return the listed code, 0
return 200 or 500; 9 new `rejected` log entries, each with a `reason`; 0 new
`decided` entries for them; the 10,000-character text returns 200.

**How to test:**
1. Scenario `"bad input"` with these `bodies`:

   | Body | Expected |
   |---|---|
   | `{"creator_id": "x"}` (no `text`) | 400 |
   | `{"text": "", "creator_id": "x"}` | 400 |
   | `{"text": " \n\t", "creator_id": "x"}` (whitespace only) | 400 |
   | `{"text": null, "creator_id": "x"}` | 400 |
   | `{"text": 123, "creator_id": "x"}` | 400 |
   | `{"text": "a" * 10001, "creator_id": "x"}` (10,001 chars) | 413 |
   | `{"text": "word " * 50000, "creator_id": "x"}` (250,000 chars) | 413 |
   | `{"text": "Hi", "creator_id": "x"}` (under the 20-word minimum) | 422 |

2. Put the boundary body — exactly 10,000 characters of real prose — in a
   separate scenario. Expected: 200.
3. By hand, send a non-JSON body (the 9th case):
   `curl -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d 'not json'`
   → 400.
4. Run all 3 trials. Check each status code in the `run_eval.py` report. In
   `GET /log`, count the new `event: "rejected"` entries and check none of them
   has a `content_id`.

**Why this target:** A blank or 250,000-character text that gets scored would
show a writer a confident-looking label on nothing, and a 500 tells the calling
site nothing it can act on. The boundary case stops "reject everything" from
passing, because the 10,000-character cap is a promise the site relies on.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
