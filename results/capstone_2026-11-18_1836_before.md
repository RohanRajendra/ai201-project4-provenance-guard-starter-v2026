# Capstone run — before

- Produced by: `run_capstone.py::main` · 3 trials · 2026-11-18 18:37 · server output in `capstone_2026-11-18_1836_before/`

| Criterion | Run 1 | Run 2 | Run 3 | All met |
|---|---|---|---|---|
| C2 | 25/26 · log +25 · write failed 1 | 25/26 · log +25 · write failed 1 | 25/26 · log +25 · write failed 1 | MISSED |
| C3 | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2804.05 · max other failure ms 8.91 · timing ok True | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2830.71 · max other failure ms 8.02 · timing ok True | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 3666.15 · max other failure ms 13.48 · timing ok True | MET |
| C4 | cold 3.62 s (200) · warm 25/25 ≤ 500 ms (max 314.35 ms) | cold 3.77 s (200) · warm 25/25 ≤ 500 ms (max 243.26 ms) | cold 4.30 s (200) · warm 25/25 ≤ 500 ms (max 256.08 ms) | MET |
| C5 | cpu 20/25 ≤ 500 ms (max 584.64) · peak 1267.5 MB | cpu 25/25 ≤ 500 ms (max 488.72) · peak 1307.4 MB | cpu 23/25 ≤ 500 ms (max 506.23) · peak 1214.2 MB | MISSED |

## C2

**Trial 1** — 25/26 · log +25 · write failed 1

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.52,
  "rid": "86463309a33d",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 8.38,
  "rid": "2bca230b4a9e",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 5757.09,
  "rid": "43d07de9d202",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 206.14,
  "rid": "b7754b1f5a91",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 192.45,
  "rid": "5f74338f64e4",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 148.98,
  "rid": "f337c7c23768",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 166.7,
  "rid": "80351a8a5deb",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 4.22,
  "rid": "55143c2161ec",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.99,
  "rid": "81b836a0773f",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 3.01,
  "rid": "5d3c787e8bba",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 3.37,
  "rid": "5f2291b28ed8",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.51,
  "rid": "b9b9cf3b47dc",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.93,
  "rid": "db96d5a10d50",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 2.72,
  "rid": "3ff5b9adbce8",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 19.43,
  "rid": "81424969b6f2",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 3.77,
  "rid": "0c59efd43ea2",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.98,
  "rid": "21a25e8b18e8",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 4.79,
  "rid": "0c5827ee8144",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 11.07,
  "rid": "18dc1c8aee00",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 12.95,
  "rid": "cd039044c0b4",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 2.97,
  "rid": "5a237094055d",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/93dba82c-55d1-4485-908a-2731442987e6",
  "status": 404,
  "client_ms": 11.32,
  "rid": "226cdbac786b",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 2.52,
  "rid": "acca01ca18af",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 2.6,
  "rid": "c4db2e06b987",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 3.65,
  "rid": "d443062ef96c",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 8.24,
  "rid": "c0d8f586b6f1",
  "fails": [
   "0 records"
  ]
 }
]
```

**Trial 2** — 25/26 · log +25 · write failed 1

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.42,
  "rid": "e4ad66f0e959",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 8.39,
  "rid": "deaa24656042",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 3751.62,
  "rid": "039a774227e3",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 206.42,
  "rid": "d308680a19f2",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 169.26,
  "rid": "86463786610b",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 134.54,
  "rid": "30a5dc26329d",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 144.02,
  "rid": "8e2af00be0ae",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 2.38,
  "rid": "03b9775550cc",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.05,
  "rid": "9f293f8e0fa9",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.86,
  "rid": "2f7e945741ff",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.0,
  "rid": "4fd5e23bd421",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.7,
  "rid": "cf14d59f49a3",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.66,
  "rid": "e15351749259",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 2.03,
  "rid": "37d6ce4bdd36",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 13.37,
  "rid": "bfc0f39aa0b2",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 3.84,
  "rid": "ffacb51bec0d",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.88,
  "rid": "da5345ca3ee9",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.59,
  "rid": "7de56d546bd1",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.28,
  "rid": "ec11bc12af02",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 8.52,
  "rid": "894b3bfdb553",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.81,
  "rid": "5103afc34209",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/fe672d71-e82e-4a3c-9064-b065d6fe9f96",
  "status": 404,
  "client_ms": 8.05,
  "rid": "f9f69de31fe6",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.39,
  "rid": "c36c55ae4aa9",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.55,
  "rid": "6029bb391912",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 3.27,
  "rid": "6ce33e20eec6",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.4,
  "rid": "deab2aaeb67e",
  "fails": [
   "0 records"
  ]
 }
]
```

**Trial 3** — 25/26 · log +25 · write failed 1

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.5,
  "rid": "e8a973c384cf",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 8.73,
  "rid": "c8ad6df9083d",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 3706.35,
  "rid": "e1d1913d671b",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 193.29,
  "rid": "f18a4bfa9230",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 169.59,
  "rid": "229d80849abb",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 135.32,
  "rid": "2a4cccb3aa7e",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 152.84,
  "rid": "fa8c3d88f61a",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 3.41,
  "rid": "04d16f490902",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.77,
  "rid": "2f96b858f5c2",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.53,
  "rid": "fcc297b29c0d",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.49,
  "rid": "c6040dca073f",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.71,
  "rid": "4b374cb631c8",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.6,
  "rid": "6d54ab717309",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 2.05,
  "rid": "97caa4ed8615",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 13.34,
  "rid": "d744341163c3",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 2.06,
  "rid": "2fed84e9a81c",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.99,
  "rid": "ce047d0e0ce1",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.75,
  "rid": "67a852dca5e4",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.76,
  "rid": "eebbebffe98c",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 8.76,
  "rid": "629e4a2f8388",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.73,
  "rid": "9a0f3b9a2dd8",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/38860734-df06-4434-8b82-a506e1ef9946",
  "status": 404,
  "client_ms": 8.82,
  "rid": "da9290b4d52b",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.58,
  "rid": "37c4f761d63e",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.54,
  "rid": "2a41eec0bcbb",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 3.96,
  "rid": "8a064a8db39a",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.42,
  "rid": "c5f9041c8761",
  "fails": [
   "0 records"
  ]
 }
]
```

## C3

**Trial 1** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2804.05 · max other failure ms 8.91 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2804.05,
  "rid": "ed67e878bf15"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.58,
  "rid": "29e8b65cd042"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.28,
  "rid": "06296a02b6a0"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.72,
  "rid": "90fcf1030889"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.42,
  "rid": "fe4f0099da4e"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.98,
  "rid": "7bf5957265f5"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1708.18,
  "rid": "262ef1aab3f8"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 8.91,
  "rid": "fa630efa8fcc"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 5.01,
  "rid": "bb3287736b4e"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 5.46,
  "rid": "111aafc49348"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 2.06,
  "rid": "dd82da5f0088"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 134.54,
  "rid": "a76241c7def7"
 }
]
```

**Trial 2** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2830.71 · max other failure ms 8.02 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2830.71,
  "rid": "db994f58074c"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 4.27,
  "rid": "641da817b1da"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.17,
  "rid": "76a3e051814b"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.71,
  "rid": "7eb85f32c9f3"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.53,
  "rid": "5c61b392ea3d"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.47,
  "rid": "ecaf2c3f3327"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1679.87,
  "rid": "0aae7cc6cb64"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 8.02,
  "rid": "d60c24c58291"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.35,
  "rid": "516ee267eaf4"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.5,
  "rid": "5736975c0578"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.6,
  "rid": "a85000ab678a"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 105.83,
  "rid": "97b52542be57"
 }
]
```

**Trial 3** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 3666.15 · max other failure ms 13.48 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3666.15,
  "rid": "3def5a7aaef1"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 5.77,
  "rid": "5530406a0ff9"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.96,
  "rid": "05c703b415e1"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.37,
  "rid": "9873723ec117"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.41,
  "rid": "74581d0a4390"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 2.23,
  "rid": "920088b3f1bf"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1932.39,
  "rid": "7757feddebc9"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 13.48,
  "rid": "aa77987b02e6"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 5.36,
  "rid": "d81b29f6c3ab"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.67,
  "rid": "01909a2f3c80"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 2.04,
  "rid": "58d163acc9e6"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 120.4,
  "rid": "99846c76d88e"
 }
]
```

## C4

**Trial 1** — cold 3.62 s (200) · warm 25/25 ≤ 500 ms (max 314.35 ms)

```json
[
 {
  "cold_ms": 3619.8,
  "warm_ms": [
   158.15,
   187.65,
   178.97,
   158.63,
   215.67,
   202.24,
   113.57,
   106.92,
   142.35,
   108.19,
   160.45,
   196.26,
   174.43,
   148.35,
   175.04,
   255.93,
   111.41,
   101.42,
   129.93,
   114.62,
   256.9,
   314.35,
   272.17,
   253.76,
   241.22
  ],
  "measure_file": "measure_2026-11-18_1837_c45_t1_before.md"
 }
]
```

**Trial 2** — cold 3.77 s (200) · warm 25/25 ≤ 500 ms (max 243.26 ms)

```json
[
 {
  "cold_ms": 3766.89,
  "warm_ms": [
   150.93,
   183.64,
   177.5,
   157.67,
   171.21,
   193.44,
   106.03,
   96.75,
   127.64,
   99.28,
   135.93,
   214.1,
   186.64,
   151.32,
   191.73,
   243.26,
   106.3,
   100.54,
   125.24,
   97.09,
   220.2,
   211.38,
   213.34,
   237.14,
   224.73
  ],
  "measure_file": "measure_2026-11-18_1837_c45_t2_before.md"
 }
]
```

**Trial 3** — cold 4.30 s (200) · warm 25/25 ≤ 500 ms (max 256.08 ms)

```json
[
 {
  "cold_ms": 4300.43,
  "warm_ms": [
   161.23,
   194.96,
   182.1,
   147.1,
   152.71,
   182.53,
   111.54,
   100.92,
   127.35,
   103.29,
   135.85,
   166.18,
   167.85,
   137.73,
   142.5,
   170.14,
   94.85,
   91.97,
   123.33,
   96.1,
   256.08,
   216.48,
   206.41,
   218.6,
   243.58
  ],
  "measure_file": "measure_2026-11-18_1837_c45_t3_before.md"
 }
]
```

## C5

**Trial 1** — cpu 20/25 ≤ 500 ms (max 584.64) · peak 1267.5 MB

```json
[
 {
  "cpu_ms": [
   251.1,
   391.75,
   346.72,
   300.31,
   401.66,
   424.9,
   173.43,
   159.3,
   233.33,
   165.27,
   259.3,
   402.24,
   344.92,
   281.96,
   328.33,
   502.13,
   173.35,
   152.22,
   212.83,
   174.01,
   500.6,
   584.64,
   518.01,
   517.63,
   497.67
  ],
  "peak_mb": 1267.5
 }
]
```

**Trial 2** — cpu 25/25 ≤ 500 ms (max 488.72) · peak 1307.4 MB

```json
[
 {
  "cpu_ms": [
   241.89,
   378.81,
   342.98,
   294.89,
   320.55,
   398.85,
   165.27,
   144.26,
   207.89,
   152.04,
   222.4,
   433.08,
   372.38,
   284.17,
   344.78,
   467.02,
   165.28,
   149.68,
   205.95,
   150.52,
   454.89,
   423.65,
   418.41,
   488.72,
   461.81
  ],
  "peak_mb": 1307.4
 }
]
```

**Trial 3** — cpu 23/25 ≤ 500 ms (max 506.23) · peak 1214.2 MB

```json
[
 {
  "cpu_ms": [
   250.44,
   399.89,
   349.16,
   273.41,
   293.0,
   369.35,
   167.72,
   146.16,
   207.12,
   155.95,
   221.74,
   340.87,
   324.15,
   259.19,
   274.3,
   354.37,
   148.54,
   138.86,
   202.66,
   148.82,
   506.23,
   429.22,
   417.76,
   434.71,
   502.33
  ],
  "peak_mb": 1214.2
 }
]
```
