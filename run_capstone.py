#!/usr/bin/env python3
"""
Capstone criteria C2–C5 (criteria.md), three trials each. Every trial starts
its own fresh `gunicorn -c gunicorn.conf.py app:app`, because C3 and C4 need a
new process (a cold start, a missing model) — so don't start one yourself.

    python run_capstone.py --label before          # C2–C5
    python run_capstone.py --label before --c1     # C1: three fresh clones (~2.4 GB download)

Writes results/capstone_<stamp>_<label>.md, with server output beside it.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

import requests

import config
import scenarios

PORT = os.getenv("CAPSTONE_PORT", "5001")  # AirPlay holds 5000 on macOS
URL = f"http://127.0.0.1:{PORT}"
BIN = Path(sys.executable).parent
T6 = scenarios.MY_WRITING[6]
SURROGATES = ["\ud800 " + T6, T6[:len(T6) // 2] + " \ud800 " + T6[len(T6) // 2:], T6 + " \udc00"]


# ── plumbing ──────────────────────────────────────────────────────────────────

def start(out: Path, **env):
    """A fresh gunicorn on PORT; returns once /health answers."""
    proc = subprocess.Popen([str(BIN / "gunicorn"), "-c", "gunicorn.conf.py", "app:app"], cwd=config.ROOT,
                            env={**os.environ, "PORT": PORT, **env}, stdout=out.open("w"), stderr=subprocess.STDOUT)
    for _ in range(300):
        try:
            requests.get(f"{URL}/health", timeout=1)
            return proc
        except requests.RequestException:
            time.sleep(0.2)
    proc.kill()
    raise RuntimeError(f"server didn't come up — see {out}")


def stop(proc):
    proc.terminate()
    proc.wait(15)


def call(method, path, sent=None, **kw):
    """One request, timed the way measure.py times it."""
    t = time.perf_counter()
    r = requests.request(method, URL + path, timeout=180, **kw)
    ms = round((time.perf_counter() - t) * 1000, 2)
    try:
        body = r.json()
    except ValueError:
        body = r.text[:80]
    return {"method": method, "path": path, "status": r.status_code, "rid": r.headers.get("X-Request-Id"),
            "client_ms": ms, "received": dt.datetime.now(dt.timezone.utc), "body": body, "sent": sent or {}}


def submit(text, creator):
    return call("POST", "/submit", {"text": text, "creator_id": creator}, json={"text": text, "creator_id": creator})


def log_lines(path=None):
    path = path or config.REQUEST_LOG
    return path.read_text(encoding="utf-8").splitlines() if path.exists() else []


def new_records(before: int):
    return [json.loads(line) for line in log_lines()[before:]]


def decided_count():
    return sum('"status": "decided"' in line for line in log_lines(config.AUDIT_LOG))


def by_id(records):
    out = {}
    for r in records:
        out.setdefault(r.get("request_id"), []).append(r)
    return out


# ── C2: one correct record per request ────────────────────────────────────────

def c2_batch(n):
    flood = f"c2_t{n}_flood"
    raw = lambda body: {"data": body, "headers": {"Content-Type": "application/json"}}  # noqa: E731
    out = [call("POST", "/ping", json={"message": "c2"}), call("GET", "/health")]
    out += [submit(scenarios.MY_WRITING[i], flood) for i in range(6)]                      # 3–8
    out += [call("POST", "/submit", body, json=body) for body, _ in scenarios.BAD_INPUT]  # 9–16
    out += [call("POST", "/submit", **raw("not json")), call("POST", "/submit", **raw("[1, 2, 3]")),
            submit(SURROGATES[0], f"c2_t{n}_sur")]                                         # 17–19
    cid = out[3]["body"]["content_id"]
    out += [call("POST", "/appeal", {"content_id": cid}, json={"content_id": cid, "reasoning": f"c2 trial {n}"}),
            call("POST", "/appeal", {"content_id": cid}, json={"content_id": cid}),
            call("GET", f"/content/{uuid.uuid4()}"), call("GET", "/nope"), call("GET", "/submit"),
            call("GET", "/log?log=requests&limit=1"),
            call("POST", "/submit", **raw("[" * 100_000 + "]" * 100_000))]               # 20–26
    return out


def c2_check(resp, records):
    """Which of C2's checks this request's record fails ([] = all pass)."""
    if len(records) != 1:
        return [f"{len(records)} records"]
    rec, fails, s = records[0], [], resp["sent"]
    if rec["status"] != resp["status"]:
        fails.append("status")
    if (resp["status"] >= 500) != isinstance(rec["error"], dict) or (rec["error"] and "type" not in rec["error"]):
        fails.append("error")
    if abs(dt.datetime.fromisoformat(rec["timestamp"]) - resp["received"]).total_seconds() > 1:
        fails.append("timestamp")
    fails += [f"input.{k}" for k in ("creator_id", "content_id") if k in s and rec["input"].get(k) != s[k]]
    if isinstance(s.get("text"), str) and rec["input"].get("sha256") != \
            hashlib.sha256(s["text"].encode("utf-8", "surrogatepass")).hexdigest()[:12]:
        fails.append("input.sha256")
    body = resp["body"] if isinstance(resp["body"], dict) else {}
    if resp["path"] == "/submit" and resp["status"] == 200 and rec["output"].get("content_id") != body.get("content_id"):
        fails.append("output.content_id")
    if "error" in body and rec["output"].get("error") != body["error"]:
        fails.append("output.error")
    if not resp["client_ms"] - 25 <= rec["duration_ms"] <= resp["client_ms"]:
        fails.append(f"duration ({rec['duration_ms']} vs client {resp['client_ms']})")
    return fails


def c2(n, outdir):
    server = outdir / f"c2_t{n}_server.txt"
    proc, before = start(server), len(log_lines())
    try:
        sent = c2_batch(n)
    finally:
        stop(proc)
    recs = by_id(new_records(before))
    rows = [{"#": i, "request": f"{r['method']} {r['path']}", "status": r["status"], "client_ms": r["client_ms"],
             "rid": r["rid"], "fails": c2_check(r, recs.get(r["rid"], []))} for i, r in enumerate(sent, 1)]
    grew, write_failed = len(log_lines()) - before, server.read_text().count("request log write failed")
    setup_ok = sent[7]["status"] == 429 and sent[18]["status"] == 500
    passed = sum(not r["fails"] for r in rows)
    return {"result": f"{passed}/26 · log +{grew} · write failed {write_failed}", "setup_ok": setup_ok,
            "met": passed == 26 and grew == 26 and write_failed == 0, "rows": rows}


# ── C3: failures, then recovery ───────────────────────────────────────────────

def c3(n, outdir):
    from huggingface_hub import constants
    tmp = Path(tempfile.mkdtemp(prefix=f"c3_t{n}_"))
    (tmp / "hub").mkdir()
    subprocess.run(["cp", "-Rc", str(Path(constants.HF_HUB_CACHE) / "models--gpt2"), str(tmp / "hub" / "off--gpt2")], check=True)
    decided, before = decided_count(), len(log_lines())
    proc = start(outdir / f"c3_t{n}_server.txt", HF_HOME=str(tmp), HF_HUB_CACHE=str(tmp / "hub"), HF_HUB_OFFLINE="1")
    try:
        missing = [submit(scenarios.MY_WRITING[i], f"c3_t{n}_{i + 1}") for i in range(5)]
        pings = [call("POST", "/ping", json={})]
        (tmp / "hub" / "off--gpt2").rename(tmp / "hub" / "models--gpt2")
        restored = submit(scenarios.MY_WRITING[5], f"c3_t{n}_7")
        sur = [submit(t, f"c3_t{n}_s{i + 1}") for i, t in enumerate(SURROGATES)]
        pings.append(call("POST", "/ping", json={}))
        last = submit(scenarios.MY_WRITING[7], f"c3_t{n}_12")
    finally:
        stop(proc)
        shutil.rmtree(tmp, ignore_errors=True)
    recs = by_id(new_records(before))
    rec = lambda r: (recs.get(r["rid"]) or [{}])[0]  # noqa: E731
    stages = lambda r: set(rec(r).get("stages_ms") or {})  # noqa: E731
    ok503 = [r["status"] == 503 and r["body"].get("error") == "detector_unavailable" and "message" in r["body"]
             and not {"guess", "confidence", "content_id"} & set(r["body"])
             and (rec(r).get("error") or {}).get("type") == "DetectorUnavailable"
             and "model_load" in stages(r) and "model" not in stages(r) for r in missing]
    ok500 = [r["status"] == 500 and r["body"].get("error") == "internal_error" and r["body"].get("request_id") == r["rid"]
             and (rec(r).get("error") or {}).get("type") and "model" in stages(r) and "style" not in stages(r) for r in sur]
    sent = missing + pings[:1] + [restored] + sur + pings[1:] + [last]
    pids = {rec(r).get("pid") for r in sent}
    new_decided = decided_count() - decided
    timing = missing[0]["client_ms"] <= 10_000 and all(r["client_ms"] <= 500 for r in missing[1:] + sur)
    checks = {"503 ×5": f"{sum(ok503)}/5", "recovered": restored["status"] == 200, "500 ×3": f"{sum(ok500)}/3",
              "new decided": new_decided, "pids": len(pids), "pings 200": all(p["status"] == 200 for p in pings),
              "first 503 ms": missing[0]["client_ms"], "max other failure ms": max(r["client_ms"] for r in missing[1:] + sur),
              "timing ok": timing}
    met = all(ok503) and restored["status"] == 200 and all(ok500) and new_decided == 2 and len(pids) == 1 \
        and checks["pings 200"] and timing and last["status"] == 200
    return {"result": " · ".join(f"{k} {v}" for k, v in checks.items()), "setup_ok": missing[0]["status"] != 200,
            "met": met, "rows": [{k: r[k] for k in ("path", "status", "client_ms", "rid")} for r in sent]}


# ── C4 + C5: one session ──────────────────────────────────────────────────────

def c45(n, outdir, label):
    before = len(log_lines())
    proc = start(outdir / f"c45_t{n}_server.txt")
    try:
        cold = submit(scenarios.BOUNDARY_TEXT, f"c45_t{n}_cold")
        m = subprocess.run([sys.executable, "measure.py", "--n", "20", "--label", f"c45_t{n}_{label}", "--url", URL],
                           cwd=config.ROOT, capture_output=True, text=True, check=True)
        report = config.ROOT / re.search(r"Wrote (\S+)", m.stdout).group(1)
        warm = [{"status": int(s), "client_ms": float(ms), "rid": rid} for s, ms, rid in
                re.findall(r"^\| \d+ \| (\d+) \| ([\d.]+) \| [^|]+ \| [^|]+ \| `(\w+)` \|$", report.read_text(), re.M)]
        warm += [submit(scenarios.BOUNDARY_TEXT, f"c45_t{n}_max_{i}") for i in range(5)]
    finally:
        stop(proc)
    records = new_records(before)
    recs = by_id(records)
    cpu = [(recs.get(w["rid"]) or [{}])[0].get("cpu_ms") for w in warm]
    peak = max(r["max_rss_mb"] for r in records)
    warm_ok = sum(w["status"] == 200 and w["client_ms"] <= 500 for w in warm)
    cpu_ok = sum(c is not None and c <= 500 for c in cpu)
    return {
        "C4": {"result": f"cold {cold['client_ms'] / 1000:.2f} s ({cold['status']}) · warm {warm_ok}/{len(warm)} ≤ 500 ms "
                         f"(max {max(w['client_ms'] for w in warm)} ms)",
               "met": cold["status"] == 200 and cold["client_ms"] <= 10_000 and warm_ok == 25 == len(warm), "setup_ok": True,
               "rows": [{"cold_ms": cold["client_ms"], "warm_ms": [w["client_ms"] for w in warm], "measure_file": report.name}]},
        "C5": {"result": f"cpu {cpu_ok}/{len(cpu)} ≤ 500 ms (max {max(c or 0 for c in cpu)}) · peak {peak} MB",
               "met": cpu_ok == 25 == len(cpu) and peak <= 1536, "setup_ok": True, "rows": [{"cpu_ms": cpu, "peak_mb": peak}]},
    }


# ── C1: a fresh clone, from RUNNING.md alone ──────────────────────────────────

def c1(n, outdir):
    """Runs RUNNING.md → The run path's own code blocks, unchanged except the
    allowed ones: the clone URL (this repo's committed HEAD) and PORT."""
    tmp = Path(tempfile.mkdtemp(prefix=f"c1_t{n}_"))
    env = {**os.environ, "HF_HOME": str(tmp / "hf"), "HF_HUB_CACHE": str(tmp / "hf" / "hub"),
           "PIP_CACHE_DIR": str(tmp / "pip"), "PORT": PORT}
    section = (config.ROOT / "RUNNING.md").read_text().split("## The run path")[1].split("\n---")[0]
    blocks = [b.strip() for b in re.findall(r"```bash\n(.*?)```", section, re.S)]
    setup, start_cmd, checks = blocks[0], blocks[1], blocks[2:]
    setup = setup.replace("<this repo's URL>", str(config.ROOT))
    transcript = outdir / f"c1_t{n}_terminal.txt"
    with transcript.open("w") as t:
        t.write(f"# folder {tmp}\n# HF_HOME, HF_HUB_CACHE, PIP_CACHE_DIR inside it; PORT={PORT}\n\n$ {setup}\n")
        t.flush()
        r = subprocess.run(["bash", "-c", f"set -e\n{setup}"], cwd=tmp, env=env, stdout=t, stderr=subprocess.STDOUT)
        t.write(f"\n# setup exit {r.returncode}\n\n$ {start_cmd}\n")
        clone = tmp / "provenance-guard"
        if r.returncode:
            return {"result": f"setup failed (exit {r.returncode})", "met": False, "setup_ok": True, "rows": []}
        # exec: gunicorn replaces bash, so terminate() below reaches it. Without it a
        # trial's server outlives the trial and answers the next one's curls.
        server_out = outdir / f"c1_t{n}_server.txt"
        server = subprocess.Popen(["bash", "-c", f"source .venv/bin/activate && exec {start_cmd}"], cwd=clone, env=env,
                                  stdout=server_out.open("w"), stderr=subprocess.STDOUT)
        try:
            for _ in range(300):
                try:
                    requests.get(f"{URL}/health", timeout=1)
                    break
                except requests.RequestException:
                    time.sleep(0.2)
            outputs = []
            for cmd in checks:
                cmd = cmd.replace("127.0.0.1:5000", f"127.0.0.1:{PORT}")
                out = subprocess.run(["bash", "-c", cmd], cwd=clone, env=env, capture_output=True, text=True).stdout
                t.write(f"\n$ {cmd}\n{out}\n")
                outputs.append(out)
        finally:
            server.terminate()
            server.wait(15)
    body = json.loads(next(o for o in outputs if '"content_id"' in o and '"entries"' not in o))
    hits = [json.loads(line) for line in (clone / "logs" / "requests.jsonl").read_text().splitlines()
            if body["content_id"] in line]
    model = sum(f.stat().st_size for f in (tmp / "hf").rglob("*") if f.is_file()) // 2**20
    met = body.get("status") == "decided" and len(hits) == 1 and hits[0]["status"] == 200
    result = f"0 extra steps · status {body.get('status')} · {len(hits)} log line(s), status {hits[0]['status'] if hits else '—'} · model cache {model} MB"
    shutil.rmtree(tmp, ignore_errors=True)
    setup_ok = "Connection in use" not in server_out.read_text()  # another copy held the port
    return {"result": result, "met": met, "setup_ok": setup_ok, "rows": [{"content_id": body["content_id"], "record": hits}]}


# ── report ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--label", default="run")
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--c1", action="store_true", help="run C1 (fresh clones) instead of C2–C5")
    args = parser.parse_args()

    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    outdir = config.RESULTS_DIR / f"capstone_{stamp}_{args.label}{'_c1' if args.c1 else ''}"
    outdir.mkdir(parents=True)
    runs = {}
    for n in range(1, args.trials + 1):
        trial = {"C1": c1(n, outdir)} if args.c1 else {"C2": c2(n, outdir), "C3": c3(n, outdir), **c45(n, outdir, args.label)}
        for name, res in trial.items():
            runs.setdefault(name, []).append(res)
            print(f"{name} trial {n}: {'MET' if res['met'] else 'miss'} — {res['result']}{'' if res['setup_ok'] else '  (SETUP WRONG)'}")

    lines = [f"# Capstone run — {args.label}{' (C1)' if args.c1 else ''}", "",
             f"- Produced by: `run_capstone.py::main` · {args.trials} trials · {dt.datetime.now():%Y-%m-%d %H:%M} · server output in `{outdir.name}/`",
             "", "| Criterion | " + " | ".join(f"Run {n}" for n in range(1, args.trials + 1)) + " | All met |",
             "|---|" + "---|" * args.trials + "---|"]
    lines += [f"| {name} | " + " | ".join(r["result"] for r in res) + f" | {'MET' if all(r['met'] for r in res) else 'MISSED'} |"
              for name, res in runs.items()]
    for name, res in runs.items():
        lines += ["", f"## {name}"]
        for n, r in enumerate(res, 1):
            lines += ["", f"**Trial {n}** — {r['result']}", "", "```json", json.dumps(r["rows"], indent=1, default=str), "```"]
    path = outdir.with_suffix(".md")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
