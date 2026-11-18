# Measure — c45_t1_shakedown

- Produced by: `measure.py::main` · 20 × POST /submit, concurrency 1, http://127.0.0.1:5005 · 2026-11-18 18:36
- Server side read back from the request log by `X-Request-Id`

## Summary

```json
{
  "wall_s": 3.09,
  "rate_per_s": 6.47,
  "sent": 20,
  "logged": 20,
  "statuses": {
    "200": 20
  },
  "client_ms": {
    "mean": 154.3,
    "p50": 156.31,
    "p95": 202.2,
    "max": 258.0
  },
  "duration_ms": {
    "mean": 151.1,
    "p50": 153.84,
    "p95": 199.34,
    "max": 255.3
  },
  "cpu_ms_mean": 277.5,
  "stages_ms_mean": {
    "validate": 0.52,
    "model_load": 0.0,
    "model": 141.41,
    "style": 0.75,
    "markers": 0.27,
    "combine": 0.0,
    "verified_lookup": 7.22,
    "audit_write": 0.33
  },
  "max_rss_mb": 1092.5
}
```

## Per request

| # | status | client_ms | duration_ms (log) | cpu_ms (log) | request_id |
|---|---|---|---|---|---|
| 0 | 200 | 192.29 | 179.77 | 298.06 | `3d15f04ba3ee` |
| 1 | 200 | 202.2 | 199.34 | 401.08 | `79c23e16be44` |
| 2 | 200 | 258.0 | 255.3 | 455.83 | `ccc36287964f` |
| 3 | 200 | 167.04 | 163.92 | 316.05 | `7a01697f7cc3` |
| 4 | 200 | 156.31 | 153.84 | 305.77 | `ce7b7e0d7ae6` |
| 5 | 200 | 200.12 | 197.65 | 419.68 | `829a3a1d33c5` |
| 6 | 200 | 108.63 | 103.91 | 166.7 | `95f07db2f79e` |
| 7 | 200 | 107.72 | 103.2 | 154.86 | `1c4da9cd02e9` |
| 8 | 200 | 149.48 | 147.01 | 234.77 | `2e545af277cf` |
| 9 | 200 | 103.2 | 100.68 | 159.86 | `3deb776bb035` |
| 10 | 200 | 135.35 | 132.84 | 223.01 | `8071b9cb8871` |
| 11 | 200 | 169.25 | 166.96 | 350.23 | `94fc075b90cd` |
| 12 | 200 | 171.21 | 168.88 | 335.2 | `968e80e76fb3` |
| 13 | 200 | 174.58 | 171.82 | 329.81 | `be01018d6600` |
| 14 | 200 | 186.7 | 183.81 | 359.13 | `df76f692b4e5` |
| 15 | 200 | 190.71 | 187.84 | 391.65 | `5dc6c46d9920` |
| 16 | 200 | 98.53 | 95.96 | 155.2 | `27a12ce044c1` |
| 17 | 200 | 92.18 | 89.82 | 138.4 | `b15bce227f1f` |
| 18 | 200 | 126.41 | 124.13 | 205.64 | `fa2e8ec82659` |
| 19 | 200 | 96.46 | 94.35 | 148.88 | `8b6684ea129e` |

## Log records

```json
{"timestamp": "2026-11-18T23:36:33.386+00:00", "request_id": "3d15f04ba3ee", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 179.77, "cpu_ms": 298.06, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_0", "chars": 1140, "words": 178, "preview": "The GuiController represents the class that acts as a contro", "sha256": "73dc0bb45c49"}, "output": {"bytes": 336, "content_id": "aa9d632d-e586-4c63-90b3-f56cf95840db", "guess": "human", "confidence": 0.3277, "status": "decided"}, "stages_ms": {"validate": 0.58, "model_load": 0.01, "model": 169.29, "style": 0.69, "markers": 0.24, "combine": 0.0, "verified_lookup": 7.39, "audit_write": 0.43}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:33.589+00:00", "request_id": "79c23e16be44", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 199.34, "cpu_ms": 401.08, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_1", "chars": 1489, "words": 289, "preview": "The top priority is to get started on the job hunt in a seri", "sha256": "56dff78794c3"}, "output": {"bytes": 335, "content_id": "2c6d4633-3a06-4ef7-a34f-462255ea775a", "guess": "human", "confidence": 0.356, "status": "decided"}, "stages_ms": {"validate": 0.59, "model_load": 0.0, "model": 189.54, "style": 0.99, "markers": 0.33, "combine": 0.0, "verified_lookup": 6.98, "audit_write": 0.31}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:33.847+00:00", "request_id": "ccc36287964f", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 255.3, "cpu_ms": 455.83, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_2", "chars": 1702, "words": 286, "preview": "A 'one world government' would make the human race collectiv", "sha256": "a8fc7e93e514"}, "output": {"bytes": 336, "content_id": "9e59a58a-b665-4125-846d-a58d857b5d97", "guess": "human", "confidence": 0.3803, "status": "decided"}, "stages_ms": {"validate": 0.69, "model_load": 0.0, "model": 241.73, "style": 1.37, "markers": 0.55, "combine": 0.01, "verified_lookup": 9.92, "audit_write": 0.45}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.014+00:00", "request_id": "7a01697f7cc3", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 163.92, "cpu_ms": 316.05, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_3", "chars": 1502, "words": 225, "preview": "In the light of innovation and technology, computers captiva", "sha256": "f6d3e4e1ec73"}, "output": {"bytes": 518, "content_id": "82706848-27b4-416b-8c2e-abc56e872a8e", "guess": "unsure", "confidence": 0.479, "status": "decided"}, "stages_ms": {"validate": 0.83, "model_load": 0.0, "model": 154.41, "style": 0.76, "markers": 0.27, "combine": 0.0, "verified_lookup": 6.71, "audit_write": 0.28}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.170+00:00", "request_id": "ce7b7e0d7ae6", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 153.84, "cpu_ms": 305.77, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_4", "chars": 1478, "words": 234, "preview": "As an active member of the basketball team on campus, this s", "sha256": "56cbea202e98"}, "output": {"bytes": 515, "content_id": "6ab9a4a1-117f-40b6-aacd-96cecaa71fc5", "guess": "unsure", "confidence": 0.405, "status": "decided"}, "stages_ms": {"validate": 0.56, "model_load": 0.0, "model": 144.81, "style": 0.79, "markers": 0.28, "combine": 0.0, "verified_lookup": 6.64, "audit_write": 0.26}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.370+00:00", "request_id": "829a3a1d33c5", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 197.65, "cpu_ms": 419.68, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_5", "chars": 1941, "words": 278, "preview": "Additionally, I had the opportunity to collaborate with the ", "sha256": "0b0ffa256bff"}, "output": {"bytes": 520, "content_id": "85e6f127-bdb7-4fff-b3f3-3442fe52ce36", "guess": "unsure", "confidence": 0.6458, "status": "decided"}, "stages_ms": {"validate": 0.67, "model_load": 0.0, "model": 186.33, "style": 1.06, "markers": 0.38, "combine": 0.0, "verified_lookup": 8.01, "audit_write": 0.68}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.478+00:00", "request_id": "95f07db2f79e", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 103.91, "cpu_ms": 166.7, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_6", "chars": 715, "words": 128, "preview": "Let me tell you a little something about the humble grape. I", "sha256": "060ec4ab8f51"}, "output": {"bytes": 336, "content_id": "302d7554-4f6b-46b9-8473-267c98ec4cda", "guess": "human", "confidence": 0.3284, "status": "decided"}, "stages_ms": {"validate": 0.34, "model_load": 0.0, "model": 95.04, "style": 0.44, "markers": 0.15, "combine": 0.0, "verified_lookup": 6.94, "audit_write": 0.42}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.587+00:00", "request_id": "1c4da9cd02e9", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 103.2, "cpu_ms": 154.86, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_7", "chars": 573, "words": 116, "preview": "I woke up later than I wanted to today. This pushed all my m", "sha256": "82a5049d58e4"}, "output": {"bytes": 517, "content_id": "a37cbd3f-a58e-4f58-87ba-9e40822f5281", "guess": "unsure", "confidence": 0.5958, "status": "decided"}, "stages_ms": {"validate": 0.27, "model_load": 0.0, "model": 94.81, "style": 0.38, "markers": 0.13, "combine": 0.0, "verified_lookup": 6.65, "audit_write": 0.34}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.736+00:00", "request_id": "2e545af277cf", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 147.01, "cpu_ms": 234.77, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_8", "chars": 1007, "words": 181, "preview": "Using the resale marketplace is a rollercoaster of an experi", "sha256": "74020aea998b"}, "output": {"bytes": 516, "content_id": "e77ff306-37dc-4676-80ae-dc257e35b159", "guess": "unsure", "confidence": 0.538, "status": "decided"}, "stages_ms": {"validate": 0.4, "model_load": 0.0, "model": 137.24, "style": 0.7, "markers": 0.24, "combine": 0.0, "verified_lookup": 7.57, "audit_write": 0.33}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.840+00:00", "request_id": "3deb776bb035", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 100.68, "cpu_ms": 159.86, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_9", "chars": 728, "words": 125, "preview": "I went to university today. Stopped by the student centre to", "sha256": "61e736e8a241"}, "output": {"bytes": 517, "content_id": "44297269-7abc-4f96-bfc0-614fc5944324", "guess": "unsure", "confidence": 0.4926, "status": "decided"}, "stages_ms": {"validate": 0.34, "model_load": 0.0, "model": 92.26, "style": 0.44, "markers": 0.15, "combine": 0.0, "verified_lookup": 6.64, "audit_write": 0.3}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:34.975+00:00", "request_id": "8071b9cb8871", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 132.84, "cpu_ms": 223.01, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_10", "chars": 1140, "words": 178, "preview": "The GuiController represents the class that acts as a contro", "sha256": "73dc0bb45c49"}, "output": {"bytes": 337, "content_id": "68d37746-2a16-433d-94a5-188e9493a521", "guess": "human", "confidence": 0.3277, "status": "decided"}, "stages_ms": {"validate": 0.45, "model_load": 0.0, "model": 124.28, "style": 0.65, "markers": 0.22, "combine": 0.0, "verified_lookup": 6.43, "audit_write": 0.3}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.145+00:00", "request_id": "94fc075b90cd", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 166.96, "cpu_ms": 350.23, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_11", "chars": 1489, "words": 289, "preview": "The top priority is to get started on the job hunt in a seri", "sha256": "56dff78794c3"}, "output": {"bytes": 336, "content_id": "03656818-6ad7-4e76-98d6-8e1b9a75d737", "guess": "human", "confidence": 0.356, "status": "decided"}, "stages_ms": {"validate": 0.59, "model_load": 0.0, "model": 157.86, "style": 0.94, "markers": 0.33, "combine": 0.0, "verified_lookup": 6.51, "audit_write": 0.26}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.316+00:00", "request_id": "968e80e76fb3", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 168.88, "cpu_ms": 335.2, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_12", "chars": 1702, "words": 286, "preview": "A 'one world government' would make the human race collectiv", "sha256": "a8fc7e93e514"}, "output": {"bytes": 337, "content_id": "95d95d50-be3b-4ba7-a2a2-04a11f0bd917", "guess": "human", "confidence": 0.3803, "status": "decided"}, "stages_ms": {"validate": 0.61, "model_load": 0.0, "model": 158.52, "style": 1.07, "markers": 0.38, "combine": 0.0, "verified_lookup": 7.54, "audit_write": 0.27}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.490+00:00", "request_id": "be01018d6600", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 171.82, "cpu_ms": 329.81, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_13", "chars": 1502, "words": 225, "preview": "In the light of innovation and technology, computers captiva", "sha256": "f6d3e4e1ec73"}, "output": {"bytes": 519, "content_id": "f5371819-297f-4f2e-8539-2eacbf327c43", "guess": "unsure", "confidence": 0.479, "status": "decided"}, "stages_ms": {"validate": 0.64, "model_load": 0.0, "model": 160.07, "style": 0.85, "markers": 0.3, "combine": 0.0, "verified_lookup": 9.04, "audit_write": 0.31}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.677+00:00", "request_id": "df76f692b4e5", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 183.81, "cpu_ms": 359.13, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_14", "chars": 1478, "words": 234, "preview": "As an active member of the basketball team on campus, this s", "sha256": "56cbea202e98"}, "output": {"bytes": 516, "content_id": "d2e3c45d-3208-4ad6-a062-e3e62e727107", "guess": "unsure", "confidence": 0.405, "status": "decided"}, "stages_ms": {"validate": 0.73, "model_load": 0.0, "model": 173.42, "style": 0.89, "markers": 0.31, "combine": 0.0, "verified_lookup": 7.53, "audit_write": 0.3}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.868+00:00", "request_id": "5dc6c46d9920", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 187.84, "cpu_ms": 391.65, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_15", "chars": 1941, "words": 278, "preview": "Additionally, I had the opportunity to collaborate with the ", "sha256": "0b0ffa256bff"}, "output": {"bytes": 521, "content_id": "ae8ee9fb-de8a-4b0c-92ce-86b9b2c3adb0", "guess": "unsure", "confidence": 0.6458, "status": "decided"}, "stages_ms": {"validate": 0.79, "model_load": 0.0, "model": 177.1, "style": 1.06, "markers": 0.39, "combine": 0.0, "verified_lookup": 7.67, "audit_write": 0.29}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:35.966+00:00", "request_id": "27a12ce044c1", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 95.96, "cpu_ms": 155.2, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_16", "chars": 715, "words": 128, "preview": "Let me tell you a little something about the humble grape. I", "sha256": "060ec4ab8f51"}, "output": {"bytes": 337, "content_id": "748f37df-861b-4b3f-9181-11f2fe483341", "guess": "human", "confidence": 0.3284, "status": "decided"}, "stages_ms": {"validate": 0.34, "model_load": 0.0, "model": 87.71, "style": 0.44, "markers": 0.15, "combine": 0.0, "verified_lookup": 6.54, "audit_write": 0.25}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:36.059+00:00", "request_id": "b15bce227f1f", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 89.82, "cpu_ms": 138.4, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_17", "chars": 573, "words": 116, "preview": "I woke up later than I wanted to today. This pushed all my m", "sha256": "82a5049d58e4"}, "output": {"bytes": 518, "content_id": "076dfabc-c40b-43cb-862b-8137678ecba7", "guess": "unsure", "confidence": 0.5958, "status": "decided"}, "stages_ms": {"validate": 0.25, "model_load": 0.0, "model": 81.84, "style": 0.38, "markers": 0.14, "combine": 0.0, "verified_lookup": 6.5, "audit_write": 0.24}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:36.185+00:00", "request_id": "fa2e8ec82659", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 124.13, "cpu_ms": 205.64, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_18", "chars": 1007, "words": 181, "preview": "Using the resale marketplace is a rollercoaster of an experi", "sha256": "74020aea998b"}, "output": {"bytes": 517, "content_id": "7c2b9894-4cca-461b-9539-fc4baa24f62e", "guess": "unsure", "confidence": 0.538, "status": "decided"}, "stages_ms": {"validate": 0.39, "model_load": 0.0, "model": 115.54, "style": 0.62, "markers": 0.21, "combine": 0.0, "verified_lookup": 6.59, "audit_write": 0.3}, "error": null, "pid": 79014}
{"timestamp": "2026-11-18T23:36:36.282+00:00", "request_id": "8b6684ea129e", "method": "POST", "route": "/submit", "status": 200, "duration_ms": 94.35, "cpu_ms": 148.88, "max_rss_mb": 1092.5, "input": {"creator_id": "measure_c45_t1_shakedown_19", "chars": 728, "words": 125, "preview": "I went to university today. Stopped by the student centre to", "sha256": "61e736e8a241"}, "output": {"bytes": 518, "content_id": "59319e50-0edf-4a8e-aa58-960e13415811", "guess": "unsure", "confidence": 0.4926, "status": "decided"}, "stages_ms": {"validate": 0.27, "model_load": 0.0, "model": 86.31, "style": 0.42, "markers": 0.15, "combine": 0.0, "verified_lookup": 6.51, "audit_write": 0.22}, "error": null, "pid": 79014}
```
