# Probes after the Unicode fix and visible stripping — 2026-11-11 21:51

Run once against the after3 system.

```json
[
  {
    "probe": "100-word Arabic essay",
    "status": 200,
    "body": {
      "chars_removed": 0,
      "confidence": 0.6981,
      "content_id": "20886153-34fd-4ed9-9b3a-56f1e2f3ab2b",
      "creator_id": "probe_rtl_after3",
      "guess": "unsure",
      "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
      "marker_score": 0.0,
      "model_score": 0.9962,
      "status": "decided",
      "style_score": 0.8,
      "text_modified": false,
      "verified_writer": false
    }
  },
  {
    "probe": "MF07 text x6 (102 words), was 422 before",
    "status": 200,
    "body": {
      "chars_removed": 0,
      "confidence": 0.7468,
      "content_id": "1cf46d22-63bf-4de0-a90d-3027bd46c3a4",
      "creator_id": "probe_mf07x6_after3",
      "guess": "unsure",
      "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it.",
      "marker_score": 0.0,
      "model_score": 0.9936,
      "status": "decided",
      "style_score": 1.0,
      "text_modified": false,
      "verified_writer": false
    }
  },
  {
    "probe": "PI02 — stripping now visible in the response",
    "status": 200,
    "body": {
      "chars_removed": 122,
      "confidence": 0.477,
      "content_id": "821ef81d-a192-41c6-89cf-64d016f0e18c",
      "creator_id": "probe_pi02_visible",
      "guess": "unsure",
      "label": "We couldn't tell whether this piece was written by a person or by an AI tool. Many people's own writing gets this result, so it is not a sign that anything was done wrong. If you wrote this, you can ask for a person to review it. Part of this submission wasn't scored because it read as instructions to our check rather than writing.",
      "marker_score": 0.0,
      "model_score": 0.754,
      "status": "decided",
      "style_score": 0.4,
      "text_modified": true,
      "verified_writer": false
    }
  }
]
```
