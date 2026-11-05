# Checks — after_as_written

- Produced by: `run_checks.py::appeal_trial`, `run_checks.py::bad_input_trial`
- 3 trials · 2026-11-04 22:36

## criterion 5 — bad input, as written (creator_id "x")

**Trial 1**

```json
{
  "results": [
    {
      "case": 1,
      "expected": 400,
      "status": 400
    },
    {
      "case": 2,
      "expected": 400,
      "status": 400
    },
    {
      "case": 3,
      "expected": 400,
      "status": 400
    },
    {
      "case": 4,
      "expected": 400,
      "status": 400
    },
    {
      "case": 5,
      "expected": 400,
      "status": 400
    },
    {
      "case": 6,
      "expected": 413,
      "status": 429
    },
    {
      "case": 7,
      "expected": 413,
      "status": 429
    },
    {
      "case": 8,
      "expected": 422,
      "status": 429
    },
    {
      "case": "non-JSON body",
      "expected": 400,
      "status": 400
    }
  ],
  "correct_codes": 6,
  "got_200_or_500": 0,
  "new_rejected_with_reason": 9,
  "new_decided": 0,
  "rejected_with_content_id": 0
}
```

**Trial 2**

```json
{
  "results": [
    {
      "case": 1,
      "expected": 400,
      "status": 429
    },
    {
      "case": 2,
      "expected": 400,
      "status": 429
    },
    {
      "case": 3,
      "expected": 400,
      "status": 429
    },
    {
      "case": 4,
      "expected": 400,
      "status": 429
    },
    {
      "case": 5,
      "expected": 400,
      "status": 429
    },
    {
      "case": 6,
      "expected": 413,
      "status": 429
    },
    {
      "case": 7,
      "expected": 413,
      "status": 429
    },
    {
      "case": 8,
      "expected": 422,
      "status": 429
    },
    {
      "case": "non-JSON body",
      "expected": 400,
      "status": 400
    }
  ],
  "correct_codes": 1,
  "got_200_or_500": 0,
  "new_rejected_with_reason": 9,
  "new_decided": 0,
  "rejected_with_content_id": 0
}
```

**Trial 3**

```json
{
  "results": [
    {
      "case": 1,
      "expected": 400,
      "status": 429
    },
    {
      "case": 2,
      "expected": 400,
      "status": 429
    },
    {
      "case": 3,
      "expected": 400,
      "status": 429
    },
    {
      "case": 4,
      "expected": 400,
      "status": 429
    },
    {
      "case": 5,
      "expected": 400,
      "status": 429
    },
    {
      "case": 6,
      "expected": 413,
      "status": 429
    },
    {
      "case": 7,
      "expected": 413,
      "status": 429
    },
    {
      "case": 8,
      "expected": 422,
      "status": 429
    },
    {
      "case": "non-JSON body",
      "expected": 400,
      "status": 400
    }
  ],
  "correct_codes": 1,
  "got_200_or_500": 0,
  "new_rejected_with_reason": 9,
  "new_decided": 0,
  "rejected_with_content_id": 0
}
```
