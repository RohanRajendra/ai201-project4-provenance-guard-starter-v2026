# Probes for the tighter targets — 2026-11-04 22:27

Run once against the before system: one submission as `probe_dup` appealed
twice with the same reasoning, and the MF07 attack text repeated six times
(102 words) submitted as `probe_rtl`.

```json
[
  {
    "probe": "duplicate appeal",
    "first": 200,
    "second": 200,
    "appeal_entries_for_id": 2
  },
  {
    "probe": "non-Latin essay (MF07 text x6)",
    "words_whitespace": 102,
    "status": 422,
    "body": {
      "error": "too_short",
      "message": "text needs at least 20 words to score."
    }
  }
]
```

The audit log entries behind it (`logs/audit.jsonl`):

```json
{"timestamp": "2026-11-05T03:27:34+00:00", "content_id": "99dcdb16-aadd-4cbe-b016-b1775f344dea", "creator_id": "probe_dup", "guess": "unsure", "model_score": 0.6517, "style_score": 0.6941, "combined_score": 0.4994, "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.", "status": "decided", "marker_score": 0.0, "verified_writer": false}
{"timestamp": "2026-11-05T03:27:34+00:00", "content_id": "99dcdb16-aadd-4cbe-b016-b1775f344dea", "creator_id": "probe_dup", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself."}
{"timestamp": "2026-11-05T03:27:34+00:00", "content_id": "99dcdb16-aadd-4cbe-b016-b1775f344dea", "creator_id": "probe_dup", "event": "appeal", "status": "under_review", "reasoning": "I wrote this myself."}
{"timestamp": "2026-11-05T03:27:34+00:00", "creator_id": "probe_rtl", "event": "rejected", "status": "rejected", "reason": "too_short", "http_status": 422}
```
