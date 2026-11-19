#!/usr/bin/env python3
"""
Send N submissions to a running service, then read each one's record back
from the request log by its X-Request-Id. What the client waited sits beside
what the log says.  (Unit 9: cost per run, latency breakdown, load.)

    gunicorn -c gunicorn.conf.py app:app                   # in one terminal
    python measure.py --n 10 --label cost                  # in another
    python measure.py --n 100 --concurrency 10 --label load

Texts cycle through scenarios.MY_WRITING (10 paragraphs, 116-289 words). Each
request gets its own creator_id, so the 5-a-minute limit never fires.
Writes results/measure_<stamp>_<label>.md.
"""

import argparse
import datetime as dt
import json
import math
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

import audit
import config
import scenarios


def pct(values, p):
    """Nearest-rank percentile."""
    values = sorted(values)
    return values[max(math.ceil(p / 100 * len(values)) - 1, 0)] if values else None


def send(url, label, i):
    body = {"text": scenarios.MY_WRITING[i % len(scenarios.MY_WRITING)], "creator_id": f"measure_{label}_{i}"}
    t = time.perf_counter()
    try:
        r = requests.post(f"{url}/submit", json=body, timeout=180)
        return {"i": i, "status": r.status_code, "request_id": r.headers.get("X-Request-Id"),
                "client_ms": round((time.perf_counter() - t) * 1000, 2)}
    except requests.RequestException as exc:
        return {"i": i, "status": None, "request_id": None, "error": type(exc).__name__,
                "client_ms": round((time.perf_counter() - t) * 1000, 2)}


def summarise(sent, records):
    found = [records[s["request_id"]] for s in sent if s["request_id"] in records]
    names = dict.fromkeys(k for r in found for k in (r.get("stages_ms") or {}))
    stages = {k: round(sum((r.get("stages_ms") or {}).get(k, 0) for r in found) / len(found), 2) for k in names}
    col = lambda key: [r[key] for r in found]  # noqa: E731
    client = [s["client_ms"] for s in sent]
    return {
        "sent": len(sent), "logged": len(found),
        "statuses": {str(k): sum(s["status"] == k for s in sent) for k in sorted({s["status"] for s in sent}, key=str)},
        "client_ms": {"mean": round(sum(client) / len(client), 1), "p50": pct(client, 50), "p95": pct(client, 95), "max": max(client)},
        "duration_ms": {"mean": round(sum(col("duration_ms")) / len(found), 1), "p50": pct(col("duration_ms"), 50),
                        "p95": pct(col("duration_ms"), 95), "max": max(col("duration_ms"))} if found else None,
        "cpu_ms_mean": round(sum(col("cpu_ms")) / len(found), 1) if found else None,
        "stages_ms_mean": stages,
        "max_rss_mb": max(col("max_rss_mb")) if found else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--concurrency", type=int, default=1)
    parser.add_argument("--label", default="run")
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    parser.add_argument("--log", type=Path, default=config.REQUEST_LOG, help="the server's request log")
    args = parser.parse_args()

    started = time.perf_counter()
    with ThreadPoolExecutor(args.concurrency) as pool:
        sent = list(pool.map(lambda i: send(args.url, args.label, i), range(args.n)))
    wall_s = round(time.perf_counter() - started, 2)

    records = {r.get("request_id"): r for r in audit.read_entries(path=args.log)}
    summary = {"wall_s": wall_s, "rate_per_s": round(args.n / wall_s, 2), **summarise(sent, records)}
    print(json.dumps(summary, indent=2))

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    path = config.RESULTS_DIR / f"measure_{stamp}_{args.label}.md"
    rows = [f"| {s['i']} | {s['status']} | {s['client_ms']} | {records.get(s['request_id'], {}).get('duration_ms')} "
            f"| {records.get(s['request_id'], {}).get('cpu_ms')} | `{s['request_id']}` |" for s in sent]
    path.write_text("\n".join([
        f"# Measure — {args.label}", "",
        f"- Produced by: `measure.py::main` · {args.n} × POST /submit, concurrency {args.concurrency}, "
        f"{args.url} · {dt.datetime.now():%Y-%m-%d %H:%M}",
        "- Server side read back from the request log by `X-Request-Id`", "",
        "## Summary", "", "```json", json.dumps(summary, indent=2), "```", "",
        "## Per request", "", "| # | status | client_ms | duration_ms (log) | cpu_ms (log) | request_id |",
        "|---|---|---|---|---|---|", *rows, "",
        "## Log records", "", "```json",
        *[json.dumps(records[s["request_id"]], ensure_ascii=False) for s in sent if s["request_id"] in records],
        "```", ""]), encoding="utf-8")
    print(f"Wrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
