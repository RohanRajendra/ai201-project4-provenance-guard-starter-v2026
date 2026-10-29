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
## 1. Expensive false positives

<!-- Your criterion. It must name a number. -->
My own writing is never labeled as AI. 0/10 paragraphs that I write myself gets a guess: "ai" in any trial, at least 6/10 get guess: "human" in every trial. 
To test this: put the 10 paragraphs in scenarios.py under "my own writing". Each 100-300 words written with no AI help. Some (atleast 3) written as short plain sentences. Run run_eval.py thrice. For each trial, count the results with guess == "ai" and guess == "human"

ai = 0 of 10 in all 3 trials, and human ≥ 6 of 10 in all 3 trials.


**Why this target:**

Telling a human writer that their writing is AI is a very expensive mistake. The AI band needs all three signals ≥ 0.60, so if my own writing is labeled ai, the agreement rule failed on the case that it exists for. The human count exists because putting everything under the "unsure" label would pass the first half with no effort, plain writing already scores 0.85 on the model_score. 

---

## 2. Score spread on AI text and Human text

<!-- Your criterion. -->
Across 5 AI-generated and 5 known-human paragraphs, the AI set's average confidence is at least 0.30 higher than the human set's in every trial.

gap ≥ 0.30 in all 3 trials.

To test: AI set: 5 paragraphs from one chat model, each made with the same prompt to generate a 150 word explanatory paragraph about xxx. using 5 different topics. Output saved as is. Prompt and model saved alongside as a comment. 
Human set: 5 paragrahs of 100+ words published prior to December 2019, with the source added in a comment. Not to re-use paragraphs from the first criterion. 
run_eval.py runs thrice, in each trial, compute difference between mean of confidence on AI set and mean of confidence on human set. 

**Why this target:**

This criterion checks that style plus markers actually reverse the measured gap on the model_score. For example if the plain human paragraph scored 0.85 and the stock AI paragraph 0.83. A gap under 0.30 would put both sets inside the 0.40–0.85 unsure band, which means the labels tell a reader nothing.


---

## 3. Label coverage on all three labels for the input. 

<!-- Your criterion. -->
On 9 inputs, 3 built for each band, each band's intended label comes back for at least 2 of its 3 inputs in every trial, and every label string exactly matches one of the three texts in README → Label Variants.

≥ 2 of 3 per band, for all three bands, in all 3 trials, with 9 of 9 label strings

To test: Use AI ×3: stock AI paragraphs that contain at least 2 phrases from markers.py's list. Use human ×3: own writing in normal style, and not reused from prior criterion 1. Use borderline ×3: merging own paragraphs and with an AI paragraph on the same topic taking half from each, joined into one text.
Run run_eval.py thrice. For each trial, check AI inputs → ai, human → human, borderline → unsure, and that each label equals the README text for its guess.

**Why this target:**

Criterion 1 establishes a very cautious approach which might mean that the AI label could become unreachable making the detector useless in practice. if any signal stays under 0.60, the 0.84 cap makes the ai label unreachable. Borderline text is where the signals should split, so it is the input that should land in unsure. 


---

## 4. Appeals changes the status and is recorded. 

<!-- Your criterion. -->
For 5 real content_ids, POST /appeal returns under_review and adds an appeal entry to the log while the original decision entry stays unchanged. An unknown id returns 404 and writes nothing.
5/5 appeals return 200 with status: "under_review". 5/5 ids get exactly one new log entry with event: "appeal", status: "under_review" and the exact reasoning, placed after the decision entry. 5/5 original decided entries are byte-identical to the saved log. Unknown id → 404 not_found with no new entry. Missing reasoning → 400. If built, /content/id shows under_review for 5/5.

To test: Submit 5 texts (at least one that comes back human and one unsure). Note each content_id. Save the GET /log output. Send POST /appeal for each id with reasoning: "I wrote this myself". Send one appeal with a made-up UUID, and one valid-id appeal with reasoning missing. Run GET /log again and compare. GET /content/id for each.
Run this thrice for three trials. 

**Why this target:**
Appeals are the only way to fix false positives, so a dropped appeal leaves a writer with no routes for remedies or fixes to their situation. The original decision has to survive unchanged. The log is the evidence for dispute. 


---

## 5. Bad input refused, logged and not scored. 

<!-- Your criterion. -->
Each of 9 malformed requests gets its specified status code (never a 200 or 500) and a rejected log entry. A text of exactly 10,000 characters is still accepted.
Per trial in the tests: 9/9 malformed requests return the listed code, with 0 returning 200 or 500. 9 new rejected log entries with a reason. 0 new decided entries for them. The boundary text returns 200.
To test: Scenario "bad input" with these bodies:
{"creator_id":"x"} → 400
{"text":"","creator_id":"x"} → 400
{"text":" \n\t","creator_id":"x"} → 400
{"text":null,"creator_id":"x"} → 400
{"text":123,"creator_id":"x"} → 400
{"text":"a"*10001,"creator_id":"x"} → 413
{"text":"word "*50000,"creator_id":"x"} → 413
{"text":"Hi","creator_id":"x"} → 422 (minimum is 20 words, pinned in README contract)
Put the boundary body {"text": <10,000 chars of real prose>, "creator_id":"x"} (→ 200) in a separate scenario.
By hand, send a non-JSON body: curl -X POST .../submit -H "Content-Type: application/json" -d 'not json' → 400.
Run all 3 trials. Check status in the run_eval report. In GET /log, count the new event: "rejected" entries and check that none of them has a content_id.

**Why this target:**

Mainly tackles the edge cases. A blank or 250,000-character text that gets scored would show a writer a confident-looking label on nothing, and a 500 tells the calling site nothing it can act on. The boundary case keeps "reject everything" from passing, because the 10,000-character cap is a contract the site is promised.


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
