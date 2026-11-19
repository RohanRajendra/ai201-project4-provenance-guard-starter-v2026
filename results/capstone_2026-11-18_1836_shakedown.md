# Capstone run — shakedown

- Produced by: `run_capstone.py::main` · 1 trials · 2026-11-18 18:36 · server output in `capstone_2026-11-18_1836_shakedown/`

| Criterion | Run 1 | All met |
|---|---|---|
| C2 | 25/26 · log +25 · write failed 1 | MISSED |
| C3 | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2895.53 · max other failure ms 8.78 · timing ok True | MET |
| C4 | cold 4.24 s (200) · warm 25/25 ≤ 500 ms (max 258.0 ms) | MET |
| C5 | cpu 24/25 ≤ 500 ms (max 504.04) · peak 1092.5 MB | MISSED |

## C2

**Trial 1** — 25/26 · log +25 · write failed 1

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 3.28,
  "rid": "44e600a377a2",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 8.52,
  "rid": "857161101a13",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 6315.08,
  "rid": "8a86b60992b4",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 209.26,
  "rid": "a11234a17d22",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 182.88,
  "rid": "fb8b2dd6e8c7",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 140.66,
  "rid": "5823be0e9dfb",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 146.17,
  "rid": "1d86d1433ad4",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 3.66,
  "rid": "8b793f7eb494",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.9,
  "rid": "c03a9184b8c8",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.17,
  "rid": "7a4145ee66c9",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.9,
  "rid": "31cffa30361a",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.76,
  "rid": "b12b6c3a3588",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.01,
  "rid": "ac60d0afc04a",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 2.44,
  "rid": "8b9e3cb0c271",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 15.75,
  "rid": "64d186489a4c",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 2.02,
  "rid": "1b6514c4e8b9",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.81,
  "rid": "5ea21819f386",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.78,
  "rid": "9eb78d3ddb6c",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 7.5,
  "rid": "2f3c472f0f83",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 8.9,
  "rid": "de4aadf8aa1b",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.54,
  "rid": "ce0dc1ba35af",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/2794e2e3-ac61-4749-9207-9aaae204ce73",
  "status": 404,
  "client_ms": 8.0,
  "rid": "8ad51e1a7b0b",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.56,
  "rid": "034159e3bfaa",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.34,
  "rid": "822a370aadc5",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 2.82,
  "rid": "19452ab02c2d",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 7.25,
  "rid": "5688a4f2dec1",
  "fails": [
   "0 records"
  ]
 }
]
```

## C3

**Trial 1** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2895.53 · max other failure ms 8.78 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2895.53,
  "rid": "d6b854203bea"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 4.84,
  "rid": "026cccd07495"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.44,
  "rid": "d77ff85bcf1a"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.93,
  "rid": "a31fa826f962"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.8,
  "rid": "49d27521cc4e"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 3.05,
  "rid": "e582ffc050fd"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1818.13,
  "rid": "b5c3068b6d95"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 8.78,
  "rid": "008cd1ff3172"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 5.44,
  "rid": "f33df36168fa"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 5.02,
  "rid": "7afa7829a5ed"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 2.01,
  "rid": "652006fb52bd"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 118.65,
  "rid": "2c7c48b0bc64"
 }
]
```

## C4

**Trial 1** — cold 4.24 s (200) · warm 25/25 ≤ 500 ms (max 258.0 ms)

```json
[
 {
  "cold_ms": 4240.06,
  "warm_ms": [
   192.29,
   202.2,
   258.0,
   167.04,
   156.31,
   200.12,
   108.63,
   107.72,
   149.48,
   103.2,
   135.35,
   169.25,
   171.21,
   174.58,
   186.7,
   190.71,
   98.53,
   92.18,
   126.41,
   96.46,
   224.36,
   249.46,
   230.22,
   209.88,
   214.32
  ],
  "measure_file": "measure_2026-11-18_1836_c45_t1_shakedown.md"
 }
]
```

## C5

**Trial 1** — cpu 24/25 ≤ 500 ms (max 504.04) · peak 1092.5 MB

```json
[
 {
  "cpu_ms": [
   298.06,
   401.08,
   455.83,
   316.05,
   305.77,
   419.68,
   166.7,
   154.86,
   234.77,
   159.86,
   223.01,
   350.23,
   335.2,
   329.81,
   359.13,
   391.65,
   155.2,
   138.4,
   205.64,
   148.88,
   458.45,
   504.04,
   467.91,
   428.65,
   436.0
  ],
  "peak_mb": 1092.5
 }
]
```
