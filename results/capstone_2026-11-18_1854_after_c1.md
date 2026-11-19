# Capstone run — after (C1)

- Produced by: `run_capstone.py::main` · 3 trials · 2026-11-18 19:00 · server output in `capstone_2026-11-18_1854_after_c1/`

| Criterion | Run 1 | Run 2 | Run 3 | All met |
|---|---|---|---|---|
| C1 | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | MET |

## C1

**Trial 1** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "159cfe1f-15d8-4e17-8e60-94017f1ebcb3",
  "record": [
   {
    "timestamp": "2026-11-18T23:55:46.593+00:00",
    "request_id": "3de917e78374",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4354.39,
    "cpu_ms": 3575.25,
    "max_rss_mb": 867.1,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "159cfe1f-15d8-4e17-8e60-94017f1ebcb3",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.24,
     "model_load": 4214.88,
     "model": 128.54,
     "style": 0.2,
     "markers": 0.05,
     "combine": 0.01,
     "verified_lookup": 8.83,
     "audit_write": 0.48
    },
    "error": null,
    "pid": 85776
   }
  ]
 }
]
```

**Trial 2** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "22354be9-17c7-42c9-9727-00bdf247226a",
  "record": [
   {
    "timestamp": "2026-11-18T23:57:57.849+00:00",
    "request_id": "68097fc99e03",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4917.03,
    "cpu_ms": 4009.34,
    "max_rss_mb": 871.9,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "22354be9-17c7-42c9-9727-00bdf247226a",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.23,
     "model_load": 4796.62,
     "model": 110.23,
     "style": 0.2,
     "markers": 0.05,
     "combine": 0.01,
     "verified_lookup": 8.64,
     "audit_write": 0.32
    },
    "error": null,
    "pid": 86403
   }
  ]
 }
]
```

**Trial 3** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "f91c4f9e-358f-4513-8634-5bed2a36ae4a",
  "record": [
   {
    "timestamp": "2026-11-19T00:00:02.729+00:00",
    "request_id": "f865812ba268",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4869.19,
    "cpu_ms": 3748.44,
    "max_rss_mb": 865.0,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "f91c4f9e-358f-4513-8634-5bed2a36ae4a",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.24,
     "model_load": 4712.96,
     "model": 138.21,
     "style": 0.2,
     "markers": 0.06,
     "combine": 0.01,
     "verified_lookup": 16.01,
     "audit_write": 0.54
    },
    "error": null,
    "pid": 86856
   }
  ]
 }
]
```
