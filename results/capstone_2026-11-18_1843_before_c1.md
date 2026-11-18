# Capstone run — before (C1)

- Produced by: `run_capstone.py::main` · 3 trials · 2026-11-18 18:48 · server output in `capstone_2026-11-18_1843_before_c1/`

| Criterion | Run 1 | Run 2 | Run 3 | All met |
|---|---|---|---|---|
| C1 | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB | MET |

## C1

**Trial 1** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "d0c9e47e-0281-4735-8e06-d35b98580c47",
  "record": [
   {
    "timestamp": "2026-11-18T23:44:54.479+00:00",
    "request_id": "5140cc05f771",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4265.47,
    "cpu_ms": 3415.09,
    "max_rss_mb": 873.4,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "d0c9e47e-0281-4735-8e06-d35b98580c47",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.26,
     "model_load": 4178.95,
     "model": 78.32,
     "style": 0.14,
     "markers": 0.04,
     "combine": 0.0,
     "verified_lookup": 6.81,
     "audit_write": 0.24
    },
    "error": null,
    "pid": 81399
   }
  ]
 }
]
```

**Trial 2** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "01938f5f-ee64-4af4-b46e-b075caa58497",
  "record": [
   {
    "timestamp": "2026-11-18T23:46:29.171+00:00",
    "request_id": "dab50fefedee",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 4112.14,
    "cpu_ms": 3385.89,
    "max_rss_mb": 864.7,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "01938f5f-ee64-4af4-b46e-b075caa58497",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.22,
     "model_load": 4026.11,
     "model": 77.53,
     "style": 0.15,
     "markers": 0.04,
     "combine": 0.01,
     "verified_lookup": 7.16,
     "audit_write": 0.3
    },
    "error": null,
    "pid": 81707
   }
  ]
 }
]
```

**Trial 3** — 0 extra steps · status decided · 1 log line(s), status 200 · model cache 1050 MB

```json
[
 {
  "content_id": "c373acb6-24aa-4ab4-9f35-29951140717d",
  "record": [
   {
    "timestamp": "2026-11-18T23:48:05.655+00:00",
    "request_id": "8e4619c9233a",
    "method": "POST",
    "route": "/submit",
    "status": 200,
    "duration_ms": 3894.53,
    "cpu_ms": 3182.41,
    "max_rss_mb": 861.3,
    "input": {
     "creator_id": "me",
     "chars": 170,
     "words": 32,
     "preview": "I walked to the market this morning because the bus was late",
     "sha256": "964596cbb966"
    },
    "output": {
     "bytes": 490,
     "content_id": "c373acb6-24aa-4ab4-9f35-29951140717d",
     "guess": "unsure",
     "confidence": 0.4,
     "status": "decided"
    },
    "stages_ms": {
     "validate": 0.23,
     "model_load": 3806.67,
     "model": 79.5,
     "style": 0.14,
     "markers": 0.04,
     "combine": 0.01,
     "verified_lookup": 6.97,
     "audit_write": 0.27
    },
    "error": null,
    "pid": 82032
   }
  ]
 }
]
```
