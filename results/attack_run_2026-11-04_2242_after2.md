# Attack run — after2

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-04 22:42
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `82cd52d0-73f9-4a2e-83db-11e32790e9e3` | unsure | 0.400 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `41272b5d-a7d5-4949-8e63-7ae2efb77870` | human | 0.315 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `b54c6792-4d65-4397-bde8-4b595fd636fd` | unsure | 0.400 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `fddff84d-2cad-4544-acd9-d7ca960a4924` | unsure | 0.506 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `9cb2f02c-13fe-4229-8afc-b4b873ec4a53` | human | 0.230 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `045c3cb8-292f-4f38-b0af-9c0aa0938b7f` | unsure | 0.481 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d3661f00-6d28-477d-bc8f-3b5f5ca0f09c` | unsure | 0.598 | HELD |
| EV08 | evasion | signal one: text below the token window | 422 | `—` | — | — | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `505351f7-a02e-4bf7-92d2-7a2735ffa2bd` | unsure | 0.498 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `0d56561f-b490-4fc3-b330-ede9dfaaef8e` | unsure | 0.704 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9548459d-15a7-4fec-9a88-ef167383ae3f` | unsure | 0.476 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `c3269d5b-599a-418d-b829-84d8a2ed35ae` | unsure | 0.602 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e6e968df-7f35-4116-b030-b96b2b827201` | unsure | 0.598 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `c74e8f59-4450-4496-9b69-b4447a4a8719` | unsure | 0.724 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `353f0fce-a851-4b14-ad85-91d878cdfb6b` | unsure | 0.643 | HELD |
| FP06 | false_positive | a person imitating a formal template | 200 | `0712845a-379c-4f41-83fc-a9d1c6763bca` | unsure | 0.611 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `b4a51bcd-9e81-4ce6-b8ee-dd0089426320` | unsure | 0.591 | HELD |
| FP08 | false_positive | very short genuine human submission | 422 | `—` | — | — | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `244a285d-2a77-4ce4-93c1-5837ee432d9a` | unsure | 0.477 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `6ac2c5e7-f8ed-4033-b717-ed6be09a60c1` | unsure | 0.477 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `566eaf75-86dc-4f10-a41a-3dde1dbc18bf` | unsure | 0.555 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `eea0db4c-940b-4292-81ca-23a1637121fc` | human | 0.386 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `e42c3fd3-8f65-4949-981a-b2c263804eec` | unsure | 0.430 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6756a088-b4da-4b7c-849a-b62c3b067869` | unsure | 0.476 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 422 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 422 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 422 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 422 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 422 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 422 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 422 | `—` | — | — | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "82cd52d0-73f9-4a2e-83db-11e32790e9e3",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.1635,
  "style_score": 0.8,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "41272b5d-a7d5-4949-8e63-7ae2efb77870",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3147,
  "model_score": 0.5943,
  "style_score": 0.0703,
  "label": "This piece looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "b54c6792-4d65-4397-bde8-4b595fd636fd",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4,
  "model_score": 0.6662,
  "style_score": 0.2293,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "fddff84d-2cad-4544-acd9-d7ca960a4924",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5057,
  "model_score": 0.6114,
  "style_score": 0.8,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "9cb2f02c-13fe-4229-8afc-b4b873ec4a53",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2303,
  "model_score": 0.3212,
  "style_score": 0.2789,
  "label": "This piece looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "045c3cb8-292f-4f38-b0af-9c0aa0938b7f",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4809,
  "model_score": 0.5727,
  "style_score": 0.4159,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d3661f00-6d28-477d-bc8f-3b5f5ca0f09c",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5983,
  "model_score": 0.5862,
  "style_score": 0.2208,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_EV08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "505351f7-a02e-4bf7-92d2-7a2735ffa2bd",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4977,
  "model_score": 0.7042,
  "style_score": 0.5825,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "0d56561f-b490-4fc3-b330-ede9dfaaef8e",
  "creator_id": "attacker_EV10",
  "guess": "unsure",
  "confidence": 0.7036,
  "model_score": 0.9792,
  "style_score": 0.8561,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9548459d-15a7-4fec-9a88-ef167383ae3f",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4761,
  "model_score": 0.6175,
  "style_score": 0.6692,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "c3269d5b-599a-418d-b829-84d8a2ed35ae",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6016,
  "model_score": 0.7387,
  "style_score": 0.9291,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "e6e968df-7f35-4116-b030-b96b2b827201",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.5975,
  "model_score": 0.8051,
  "style_score": 0.7798,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "c74e8f59-4450-4496-9b69-b4447a4a8719",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.7238,
  "model_score": 0.8329,
  "style_score": 0.739,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "353f0fce-a851-4b14-ad85-91d878cdfb6b",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.6435,
  "model_score": 0.8005,
  "style_score": 0.9731,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "0712845a-379c-4f41-83fc-a9d1c6763bca",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.6105,
  "model_score": 0.8814,
  "style_score": 0.6794,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "b4a51bcd-9e81-4ce6-b8ee-dd0089426320",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.5908,
  "model_score": 0.8816,
  "style_score": 0.6,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "244a285d-2a77-4ce4-93c1-5837ee432d9a",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.477,
  "model_score": 0.754,
  "style_score": 0.4,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "6ac2c5e7-f8ed-4033-b717-ed6be09a60c1",
  "creator_id": "attacker_PI02",
  "guess": "unsure",
  "confidence": 0.477,
  "model_score": 0.754,
  "style_score": 0.4,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "566eaf75-86dc-4f10-a41a-3dde1dbc18bf",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.555,
  "model_score": 0.7667,
  "style_score": 0.6864,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "eea0db4c-940b-4292-81ca-23a1637121fc",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.3855,
  "model_score": 0.5129,
  "style_score": 0.5163,
  "label": "This piece looks like it was written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "e42c3fd3-8f65-4949-981a-b2c263804eec",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4301,
  "model_score": 0.6569,
  "style_score": 0.4066,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "6756a088-b4da-4b7c-849a-b62c3b067869",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4761,
  "model_score": 0.6175,
  "style_score": 0.6692,
  "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 422,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
