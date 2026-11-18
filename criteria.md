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

> **Revised in unit 8:** Each of the 8 JSON bodies is sent with its own
> `creator_id` instead of all sharing `"x"` (`eval_bad_N` in `run_eval.py`,
> `chk_bad_t<trial>_N` in `run_checks.py`). The non-JSON body has no
> `creator_id` and is unchanged. Everything else is unchanged: 9 of 9 return the listed code, 0
> return 200 or 500, 9 new `rejected` entries each with a `reason`, 0 new
> `decided` entries, and the 10,000-character text returns 200.
>
> **Why revised:** As written, it measures two stages at once. Unit 8 added a
> 5-per-minute limit per `creator_id` that runs before the route and counts
> refused requests. Under one shared `"x"`, every request from the 6th on is
> answered by the limiter, so the criterion stops seeing the route's validation,
> which is what "bad input is refused, logged, never scored" is about. The
> revision isolates the route. Run as written, it scored 6/9, 1/9 and 1/9,
> every miss a `429` (`results/checks_2026-11-04_2224_before_as_written.md`).
> That combined result is a real miss: a writer who sends a few bad requests is
> told "too many submissions" instead of what's wrong. It stays in the README
> as MISSED, with its diagnosis under the rate limiter.

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

---

# Capstone criteria (unit 9)

Five criteria for this unit's extension: the gunicorn run path, the request
log, the error handlers, and the cost. They were written before any capstone
results.

**Rules for all five:** Each criterion gets 3 trials, and a target counts as
met only if it holds in all 3. Every trial starts fresh (a new clone or a new
server), and no code changes between trials. Times are measured at the client
unless a criterion says `duration_ms`. Texts come from `scenarios.py`. The
surrogate texts are `MY_WRITING[6]` with a lone `\ud800` at the start (S1) or
in the middle (S2), or a `\udc00` at the end (S3). Each request uses its own
`creator_id` unless a criterion means to trip the rate limit.

---

## C1. A fresh clone runs from RUNNING.md alone

**Criterion:** In a new folder with empty pip and model caches, clone the repo
and follow RUNNING.md → *The run path* exactly as written. No extra step is
needed, and the `/submit` curl in RUNNING.md returns a result that the clone
logged.

**Target:** In each trial:
- 0 extra steps.
- The curl returns a `content_id` with `"status": "decided"`.
- That `content_id` appears on exactly 1 line of the clone's
  `logs/requests.jsonl`, with status 200.

**How to test:**
1. Make a new folder and point `HF_HOME`, `HF_HUB_CACHE` and `PIP_CACHE_DIR`
   inside it, so everything downloads again.
2. Record the terminal with `script`, clone the committed HEAD, and run the
   steps.
3. Count every command that RUNNING.md doesn't state, or that you had to edit.
   Not counted: the clone path, a `python3.11`–`3.13` binary, `PORT=5001`
   (RUNNING.md offers it), and re-running a command unchanged.
4. Grep the clone's log for the `content_id`.

**Why:**
- **0 extra steps:** each extra step is where a stranger gets stuck.
- **Empty caches:** Milestone 3's test shared this machine's model cache and
  copied in uncommitted files, so the 548 MB download and the committed repo
  were never tried.
- **The log check:** it proves the clone answered, and not another copy
  running on the same port.

## C2. Every request leaves exactly one correct log record

**Criterion:** Each of the 26 requests below gets exactly one new line in
`logs/requests.jsonl`, found by its `X-Request-Id`. That line matches what the
client sent and got back.

**Target:** In each trial, 26 of 26 match. The log grows by exactly 26 lines,
and the server prints `request log write failed` 0 times. A record matches
when:
- `status` is the status the client got.
- `error` is filled in for a 500 or above, and `null` for anything else.
- `timestamp` is within 1 s of the response.
- `creator_id` and `content_id` are what was sent, and `sha256` matches the
  text.
- `output` carries the body's `content_id` (on a 200) or its `error` code.
- `duration_ms` is no longer than the client's round trip, and at most 25 ms
  shorter.

**How to test:** Start a fresh `gunicorn -c gunicorn.conf.py app:app` and save
its output. Send these requests in order, one at a time. Record each one's
status, `X-Request-Id`, body, receive time and round trip.

| # | Request | Expect |
|---|---|---|
| 1 | `POST /ping` | 200 |
| 2 | `GET /health` | 200 |
| 3–7 | `/submit` `MY_WRITING[0–4]`, all from one creator | 200 ×5 |
| 8 | `/submit` `MY_WRITING[5]`, same creator | 429 |
| 9–16 | `/submit`, the 8 `BAD_INPUT` bodies | 400 ×5, 413 ×2, 422 |
| 17 | `/submit` with body `not json` | 400 |
| 18 | `/submit` with body `[1, 2, 3]` | 400 |
| 19 | `/submit` S1 | 500 |
| 20 | `/appeal` on #4's id, with reasoning | 200 |
| 21 | `/appeal` on #4's id, without reasoning | 400 |
| 22 | `GET /content/<random id>` | 404 |
| 23 | `GET /nope` | 404 |
| 24 | `GET /submit` | 405 |
| 25 | `GET /log?log=requests&limit=1` | 200 |
| 26 | `/submit` with JSON nested 100,000 levels deep | not predicted |

If #8 isn't a 429 or #19 isn't a 500, the setup is wrong. Keep that trial with
the reason, and rerun.

**Why:**
- **Every request, not most:** the cost numbers, the latency breakdown and
  every diagnosis are read from this log. A missing or wrong record breaks all
  of them, and "a failure that shows up only as an absence is one you'll never
  find."
- **26 of 26:** these paths are deterministic, so one miss is a bug, not
  noise.
- **25 ms:** Milestone 3's gap between the client and the log was 2–9 ms. A
  bigger gap is waiting the log doesn't show.
- **#26:** a real hostile body. It stays in whatever it does.

## C3. Failures return JSON, decide nothing, and the service recovers on its own

**Criterion:** When the model files are missing, `/submit` returns a JSON 503
and decides nothing. Once the files are back, the next `/submit` works without
a restart. A text with a lone surrogate returns a JSON 500 with its
`request_id`. Each failure's record names the error and the stage it stopped
in. One worker serves the whole trial, and no failure is slower than a
success.

**Target:** In each trial:
- **Missing model:** 5 of 5 return 503 `detector_unavailable` with no score.
  Each record has `DetectorUnavailable` and stopped at `model_load`.
- **Recovery:** after the files are restored, 1 of 1 returns 200 with no
  restart.
- **Surrogates:** 3 of 3 return 500 `internal_error`, and the body's
  `request_id` equals the header. Each record stopped at `model`.
- **Audit log:** exactly 2 new `decided` entries (the two 200s).
- **Worker:** all 12 records show the same `pid`, and both `/ping`s return
  200.
- **Timing:** the first 503 takes 10 s or less. Every other failure takes
  500 ms or less.

**How to test:** Copy the gpt2 cache folder to a temp folder under a different
name, then start gunicorn with `HF_HUB_CACHE` pointing there and
`HF_HUB_OFFLINE=1`. In order:
1. 5 × `/submit` (expect 503).
2. `/ping`.
3. Rename the folder back to `models--gpt2`.
4. `/submit` (expect 200).
5. S1, S2, S3 (expect 500 each).
6. `/ping`.
7. `/submit` (expect 200).

Count the `decided` lines before and after. If the first request returns 200,
the setup is wrong.

**Why:**
- **The handlers:** these are the two error handlers built this unit. A JSON
  code tells the calling site what to do: "try later" or "something broke".
- **Nothing decided:** the audit log is the evidence in a dispute.
- **One pid:** a worker restart would hide the crash, make the next writer
  wait 4.4 s for the model to reload, and reset the rate limits.
- **No restart:** there's one worker and nobody watching it, so it has to
  recover on its own.
- **The first 503's timing:** it pays the same torch import as a cold start,
  so it gets the same budget as C4's cold request.
- **Not tested:** `/health` saying `ok: true` during an outage (seen in
  Milestone 3). That's a known gap, recorded under What's Still Broken.

## C4. Cold requests answer within 10 s, warm ones within 500 ms

**Criterion:** After a fresh start, the first `/submit` (cold) returns 200
within 10 s. Each of the next 25 (warm) returns 200 within 500 ms.

**Target:** In each trial, cold 1 of 1 ≤ 10 s, and warm 25 of 25 ≤ 500 ms.

**How to test:** Start a fresh `gunicorn -c gunicorn.conf.py app:app`. As soon
as `/health` answers, send `BOUNDARY_TEXT` (10,000 characters, the longest
allowed). Then run `python measure.py --n 20 --label c45_t<n>`, then send
`BOUNDARY_TEXT` 5 more times. Count the round trips.

**Why:**
- **10 s cold:** about when a writer gives up and clicks again. That second
  click queues behind the first on the only worker, makes a second decision,
  and uses up their rate limit.
- **500 ms warm:** half the second at which a person notices waiting, which
  leaves the rest for the site and the network.
- **All 25, not a p95:** with one worker, one slow request delays everyone
  behind it.
- **Not stricter:** gpt2's forward pass alone averages 136 ms (Milestone 3),
  and a near-warm cold start would mean preloading the model, which this run
  path doesn't claim.

## C5. A warm run costs at most 0.5 CPU-seconds, and memory peaks at 1,536 MB

**Criterion:** Over C4's 25 warm requests, every record's `cpu_ms` is 500 or
less, and the highest `max_rss_mb` is 1,536 or less.

**Target:** In each trial, 25 of 25 at or under 500 `cpu_ms`, and a peak of
1,536 MB or less.

**How to test:** Use C4's session, not counting the cold request. Read
`cpu_ms` from measure.py's table and from the 5 `BOUNDARY_TEXT` records. Take
the highest `max_rss_mb` in the trial.

**Why:**
- **Memory decides the host.** Milestone 3 measured more than 1 GB, so this
  needs a 2 GB instance. 1,536 MB is 75% of that, which leaves room for the
  OS. Over it, the bill doubles or the worker gets killed mid-request with no
  record.
- **CPU:** `cpu_ms` is the number the hundred-a-day cost multiplies. On a
  1-vCPU host, a run over 0.5 CPU-s can't meet C4's 500 ms.
- **Not stricter:** Milestone 3's 0.263 mean is my own measurement, not what
  the host needs.
- **macOS:** the memory figure is measured on macOS, and Linux will differ.
