# Capstone run — before (C1)

- Produced by: `run_capstone.py::main` · 3 trials · 2026-11-18 18:42 · server output in `capstone_2026-11-18_1838_before_c1/`

| Criterion | Run 1 | Run 2 | Run 3 | All met |
|---|---|---|---|---|
| C1 | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | 0 extra steps · status decided · 0 log line(s), status — · model cache 1050 MB | 0 extra steps · status decided · 0 log line(s), status — · model cache 1050 MB | MISSED |

## C1

**Trial 1** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "16a7a374-a66f-44c4-92fa-7eff879d1206",
  "record": [
   {
    "timestamp": "2026-11-18T23:39:35.923+00:00",
    "request_id": "c5c75433b339",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4226.89,
    "cpu_ms": 3415.55,
    "max_rss_mb": 855.6,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "16a7a374-a66f-44c4-92fa-7eff879d1206",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.29,
     "model_load": 4136.76,
     "model": 81.87,
     "style": 0.16,
     "markers": 0.04,
     "combine": 0.01,
     "verified_lookup": 6.76,
     "audit_write": 0.26
    },
    "error": null,
    "pid": 79962
   }
  ]
 }
]
```

**Trial 2** — 0 extra steps · status decided · 0 log line(s), status — · model cache 1050 MB

```json
[
 {
  "content_id": "4c72e029-ee10-42d7-bf3e-45271c79c963",
  "record": []
 }
]
```

**Trial 3** — 0 extra steps · status decided · 0 log line(s), status — · model cache 1050 MB

```json
[
 {
  "content_id": "645daee2-7308-4b49-bb1d-9c96b0ce4964",
  "record": []
 }
]
```
