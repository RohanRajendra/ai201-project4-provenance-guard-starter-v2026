# Capstone run — after

- Produced by: `run_capstone.py::main` · 3 trials · 2026-11-18 18:52 · server output in `capstone_2026-11-18_1851_after/`

| Criterion | Run 1 | Run 2 | Run 3 | All met |
|---|---|---|---|---|
| C2 | 26/26 · log +26 · write failed 0 | 26/26 · log +26 · write failed 0 | 26/26 · log +26 · write failed 0 | MET |
| C3 | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2970.73 · max other failure ms 8.18 · timing ok True | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2693.93 · max other failure ms 7.24 · timing ok True | 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 3108.32 · max other failure ms 7.23 · timing ok True | MET |
| C4 | cold 3.56 s (200) · warm 25/25 ≤ 500 ms (max 222.49 ms) | cold 3.61 s (200) · warm 25/25 ≤ 500 ms (max 258.47 ms) | cold 3.70 s (200) · warm 25/25 ≤ 500 ms (max 220.52 ms) | MET |
| C5 | cpu 25/25 ≤ 500 ms (max 452.09) · peak 1306.9 MB | cpu 23/25 ≤ 500 ms (max 531.07) · peak 1304.8 MB | cpu 25/25 ≤ 500 ms (max 460.16) · peak 1223.8 MB | MISSED |

## C2

**Trial 1** — 26/26 · log +26 · write failed 0

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.65,
  "rid": "ccc8a00e3dd9",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 9.19,
  "rid": "83089c71ba58",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 5649.82,
  "rid": "7e267cab726d",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 200.12,
  "rid": "aa9c08fe8385",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 175.1,
  "rid": "0ee5b617740b",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 139.97,
  "rid": "fa8300f0cad0",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 143.36,
  "rid": "2b0e0708f899",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 2.56,
  "rid": "abb8afd524ee",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.83,
  "rid": "028323065e4c",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.79,
  "rid": "d6dda59a52d1",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.06,
  "rid": "6bf9537d420c",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.77,
  "rid": "f31ee7e6dc78",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.18,
  "rid": "cbe91551c7e5",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 2.03,
  "rid": "e391d2a6ae8e",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 13.59,
  "rid": "c424d319dc6d",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 1.96,
  "rid": "b172ffd16843",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.94,
  "rid": "e05724230d26",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.61,
  "rid": "946fefcf76d3",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.32,
  "rid": "28e9591776a6",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 8.68,
  "rid": "f6541fc6a652",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.78,
  "rid": "c2ff44b56283",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/2c0747e5-ced2-454e-8379-839262a4417a",
  "status": 404,
  "client_ms": 8.76,
  "rid": "8d80ce414b54",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.81,
  "rid": "aaea3f0a33ae",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.73,
  "rid": "7da869abdc48",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 4.41,
  "rid": "ed59014e9d61",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.74,
  "rid": "181ada86ece0",
  "fails": []
 }
]
```

**Trial 2** — 26/26 · log +26 · write failed 0

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.83,
  "rid": "8ebc3a365c71",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 9.57,
  "rid": "1f51a8edac7d",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 3519.97,
  "rid": "8180304380ea",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 184.67,
  "rid": "f669ffc86138",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 169.16,
  "rid": "75e9b3e5223a",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 137.31,
  "rid": "486452ef60f9",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 142.39,
  "rid": "1c6adcdfacc9",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 2.42,
  "rid": "976ba990fab1",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.19,
  "rid": "37b77bcac774",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.01,
  "rid": "de9658487767",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.73,
  "rid": "4b71f1873ce2",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.63,
  "rid": "f79078f960a2",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.52,
  "rid": "e70bb3d161c7",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 1.76,
  "rid": "9de4961c5308",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 13.55,
  "rid": "09510c41a8a5",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 1.83,
  "rid": "ad1e948ff912",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.82,
  "rid": "d33a405322ac",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.58,
  "rid": "008d07b36b64",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.59,
  "rid": "13bb2aca4d6b",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 9.16,
  "rid": "ddaa9003140d",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.48,
  "rid": "8dc2d17b1007",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/7ebfe187-2e8e-4ca6-8ab2-5068e86a259e",
  "status": 404,
  "client_ms": 8.68,
  "rid": "caca70eb6ba4",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.45,
  "rid": "6d8314d80767",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.42,
  "rid": "213e655f4193",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 4.54,
  "rid": "0c99983ad38d",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.95,
  "rid": "1871af624553",
  "fails": []
 }
]
```

**Trial 3** — 26/26 · log +26 · write failed 0

```json
[
 {
  "#": 1,
  "request": "POST /ping",
  "status": 200,
  "client_ms": 2.48,
  "rid": "bfa582f237e5",
  "fails": []
 },
 {
  "#": 2,
  "request": "GET /health",
  "status": 200,
  "client_ms": 9.31,
  "rid": "8286a6d3c255",
  "fails": []
 },
 {
  "#": 3,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 3693.43,
  "rid": "4ea912062503",
  "fails": []
 },
 {
  "#": 4,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 242.01,
  "rid": "0c64c10e693e",
  "fails": []
 },
 {
  "#": 5,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 178.58,
  "rid": "12af1f2325ea",
  "fails": []
 },
 {
  "#": 6,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 138.22,
  "rid": "759611005e10",
  "fails": []
 },
 {
  "#": 7,
  "request": "POST /submit",
  "status": 200,
  "client_ms": 145.52,
  "rid": "e6d9d35c4697",
  "fails": []
 },
 {
  "#": 8,
  "request": "POST /submit",
  "status": 429,
  "client_ms": 2.39,
  "rid": "809c00500640",
  "fails": []
 },
 {
  "#": 9,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.82,
  "rid": "69b2b645a7c4",
  "fails": []
 },
 {
  "#": 10,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 2.07,
  "rid": "06bce8e7fb3f",
  "fails": []
 },
 {
  "#": 11,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.73,
  "rid": "f45ec41c04f1",
  "fails": []
 },
 {
  "#": 12,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.57,
  "rid": "fe0f8b726133",
  "fails": []
 },
 {
  "#": 13,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.55,
  "rid": "7c6620cc5f5f",
  "fails": []
 },
 {
  "#": 14,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 1.83,
  "rid": "7dde88c4bf72",
  "fails": []
 },
 {
  "#": 15,
  "request": "POST /submit",
  "status": 413,
  "client_ms": 13.42,
  "rid": "d6846c3e431f",
  "fails": []
 },
 {
  "#": 16,
  "request": "POST /submit",
  "status": 422,
  "client_ms": 1.82,
  "rid": "cb34948dff05",
  "fails": []
 },
 {
  "#": 17,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.71,
  "rid": "ca8d056bba13",
  "fails": []
 },
 {
  "#": 18,
  "request": "POST /submit",
  "status": 400,
  "client_ms": 1.56,
  "rid": "2d760734412c",
  "fails": []
 },
 {
  "#": 19,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 6.35,
  "rid": "f1476be64a07",
  "fails": []
 },
 {
  "#": 20,
  "request": "POST /appeal",
  "status": 200,
  "client_ms": 9.22,
  "rid": "d05af365a57d",
  "fails": []
 },
 {
  "#": 21,
  "request": "POST /appeal",
  "status": 400,
  "client_ms": 1.36,
  "rid": "42da969b1dda",
  "fails": []
 },
 {
  "#": 22,
  "request": "GET /content/d98ad91c-2bcf-4b3f-9e38-59f191b1dddf",
  "status": 404,
  "client_ms": 10.7,
  "rid": "dc7b094dc4fe",
  "fails": []
 },
 {
  "#": 23,
  "request": "GET /nope",
  "status": 404,
  "client_ms": 1.74,
  "rid": "fbaa530bd345",
  "fails": []
 },
 {
  "#": 24,
  "request": "GET /submit",
  "status": 405,
  "client_ms": 1.46,
  "rid": "ddaec901a227",
  "fails": []
 },
 {
  "#": 25,
  "request": "GET /log?log=requests&limit=1",
  "status": 200,
  "client_ms": 5.2,
  "rid": "1a1f417753db",
  "fails": []
 },
 {
  "#": 26,
  "request": "POST /submit",
  "status": 500,
  "client_ms": 7.24,
  "rid": "329b87b622e6",
  "fails": []
 }
]
```

## C3

**Trial 1** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2970.73 · max other failure ms 8.18 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2970.73,
  "rid": "da7aa16b75ad"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.8,
  "rid": "06e9f70d5368"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.85,
  "rid": "f8f5c1dc486b"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.18,
  "rid": "d69dd35d9421"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.76,
  "rid": "0489d4f79a9b"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.58,
  "rid": "ff2ab43f9cbf"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1726.45,
  "rid": "9abbb29d5d4c"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 8.18,
  "rid": "1411f47ffe8a"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.67,
  "rid": "3b77f7bbc06a"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.9,
  "rid": "4ec839ac7176"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.9,
  "rid": "dbb7a8b4b749"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 108.59,
  "rid": "04d2d3d68369"
 }
]
```

**Trial 2** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 2693.93 · max other failure ms 7.24 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2693.93,
  "rid": "58f238841f36"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.38,
  "rid": "adb425c7c685"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.63,
  "rid": "848882b64d34"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.3,
  "rid": "43fd738757a7"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.31,
  "rid": "eb3248c10c4b"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.54,
  "rid": "5914858abf36"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1610.2,
  "rid": "d62acc8779d7"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 7.24,
  "rid": "4ae5c7ef777a"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.74,
  "rid": "68b8f58657d8"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.18,
  "rid": "0caaba9c6700"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.86,
  "rid": "8fb0d5e6baa0"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 105.7,
  "rid": "8d5df685e5be"
 }
]
```

**Trial 3** — 503 ×5 5/5 · recovered True · 500 ×3 3/3 · new decided 2 · pids 1 · pings 200 True · first 503 ms 3108.32 · max other failure ms 7.23 · timing ok True

```json
[
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3108.32,
  "rid": "2168034a3b6f"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 7.19,
  "rid": "c2b96eb468db"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 3.3,
  "rid": "1a83c66f14db"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.74,
  "rid": "e222374dedd7"
 },
 {
  "path": "/submit",
  "status": 503,
  "client_ms": 2.81,
  "rid": "03af634d44dd"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 2.83,
  "rid": "04d98922db8e"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 1607.55,
  "rid": "2d02ab65e2a2"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 7.23,
  "rid": "06ed94b412fc"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 4.21,
  "rid": "fb30738c119b"
 },
 {
  "path": "/submit",
  "status": 500,
  "client_ms": 3.8,
  "rid": "61d8908c3cb2"
 },
 {
  "path": "/ping",
  "status": 200,
  "client_ms": 1.46,
  "rid": "637b192229f0"
 },
 {
  "path": "/submit",
  "status": 200,
  "client_ms": 104.45,
  "rid": "d12cc3d42043"
 }
]
```

## C4

**Trial 1** — cold 3.56 s (200) · warm 25/25 ≤ 500 ms (max 222.49 ms)

```json
[
 {
  "cold_ms": 3564.65,
  "warm_ms": [
   151.4,
   173.26,
   162.81,
   135.75,
   142.58,
   168.91,
   97.57,
   93.04,
   123.09,
   95.79,
   133.52,
   187.94,
   190.64,
   140.42,
   173.9,
   185.65,
   99.65,
   94.25,
   124.47,
   97.08,
   215.13,
   211.18,
   218.52,
   217.66,
   222.49
  ],
  "measure_file": "measure_2026-11-18_1852_c45_t1_after.md"
 }
]
```

**Trial 2** — cold 3.61 s (200) · warm 25/25 ≤ 500 ms (max 258.47 ms)

```json
[
 {
  "cold_ms": 3609.72,
  "warm_ms": [
   152.94,
   200.18,
   172.78,
   138.34,
   141.97,
   168.45,
   109.13,
   98.24,
   129.21,
   97.18,
   133.98,
   172.14,
   161.15,
   133.91,
   140.85,
   178.15,
   101.03,
   96.38,
   135.19,
   107.81,
   226.45,
   258.47,
   225.56,
   246.55,
   228.96
  ],
  "measure_file": "measure_2026-11-18_1852_c45_t2_after.md"
 }
]
```

**Trial 3** — cold 3.70 s (200) · warm 25/25 ≤ 500 ms (max 220.52 ms)

```json
[
 {
  "cold_ms": 3695.68,
  "warm_ms": [
   175.17,
   183.92,
   169.62,
   135.76,
   143.18,
   170.48,
   103.19,
   92.98,
   128.85,
   96.79,
   135.99,
   168.18,
   164.09,
   134.84,
   140.6,
   166.33,
   95.07,
   92.28,
   122.02,
   96.18,
   220.52,
   212.6,
   214.48,
   208.29,
   204.92
  ],
  "measure_file": "measure_2026-11-18_1852_c45_t3_after.md"
 }
]
```

## C5

**Trial 1** — cpu 25/25 ≤ 500 ms (max 452.09) · peak 1306.9 MB

```json
[
 {
  "cpu_ms": [
   240.51,
   358.58,
   317.81,
   255.52,
   274.59,
   349.92,
   155.23,
   140.67,
   205.16,
   148.92,
   220.22,
   375.21,
   372.62,
   266.26,
   318.45,
   384.87,
   158.17,
   141.36,
   204.08,
   149.22,
   438.85,
   426.55,
   442.79,
   440.81,
   452.09
  ],
  "peak_mb": 1306.9
 }
]
```

**Trial 2** — cpu 23/25 ≤ 500 ms (max 531.07) · peak 1304.8 MB

```json
[
 {
  "cpu_ms": [
   243.81,
   404.95,
   333.22,
   259.1,
   273.13,
   352.79,
   172.15,
   148.18,
   212.56,
   149.56,
   221.02,
   349.66,
   316.62,
   257.89,
   273.99,
   368.42,
   161.14,
   141.59,
   216.63,
   160.53,
   453.88,
   531.07,
   464.03,
   503.14,
   465.82
  ],
  "peak_mb": 1304.8
 }
]
```

**Trial 3** — cpu 25/25 ≤ 500 ms (max 460.16) · peak 1223.8 MB

```json
[
 {
  "cpu_ms": [
   272.71,
   375.94,
   328.94,
   256.97,
   277.03,
   353.4,
   158.02,
   140.33,
   210.66,
   150.32,
   221.93,
   349.64,
   316.38,
   256.07,
   270.63,
   346.86,
   148.68,
   138.55,
   201.12,
   149.16,
   460.16,
   434.17,
   432.83,
   423.3,
   414.15
  ],
  "peak_mb": 1223.8
 }
]
```
