#!/usr/bin/env python3
"""
Criteria 4 and 5 — the parts `run_eval.py` can't check, three trials each.

    python app.py                          # in one terminal
    python run_checks.py --label before    # in another

`run_eval.py` only POSTs to /submit and never reads the log, so:
  - criterion 4 (appeals) needs a content_id, an appeal, and a log diff;
  - criterion 5 needs a non-JSON body and a count of the `rejected` entries.

Writes results/checks_<stamp>_<label>.md with every trial's raw output.
"""

import argparse
import datetime as dt
import json
import uuid

import requests

import config
import scenarios


def log_lines():
    return config.AUDIT_LOG.read_text(encoding="utf-8").splitlines() if config.AUDIT_LOG.exists() else []


def new_entries(before):
    return [json.loads(line) for line in log_lines()[len(before):]]


def appeal_trial(url, trial):
    """Criterion 4: five appeals, an unknown id, a missing reasoning."""
    items = []
    for i, text in enumerate(scenarios.APPEAL_TEXTS, 1):
        r = requests.post(f"{url}/submit", json={"text": text, "creator_id": f"appeal_t{trial}_{i}"}).json()
        items.append({"content_id": r["content_id"], "guess": r["guess"]})

    saved = log_lines()
    reasoning = "I wrote this myself."
    for item in items:
        r = requests.post(f"{url}/appeal", json={"content_id": item["content_id"], "reasoning": reasoning})
        item["appeal_status"], item["appeal_body_status"] = r.status_code, r.json().get("status")

    n = len(log_lines())
    unknown = requests.post(f"{url}/appeal", json={"content_id": str(uuid.uuid4()), "reasoning": reasoning})
    unknown_wrote = len(log_lines()) - n
    missing = requests.post(f"{url}/appeal", json={"content_id": items[0]["content_id"]})

    after = log_lines()
    added = new_entries(saved)
    for item in items:
        cid = item["content_id"]
        mine = [e for e in added if e.get("content_id") == cid]
        decision_at = next(i for i, line in enumerate(after) if cid in line and '"decided"' in line)
        appeal_at = next((i for i, line in enumerate(after) if cid in line and '"appeal"' in line), -1)
        item["new_entries"] = len(mine)
        item["appeal_entry_ok"] = (len(mine) == 1 and mine[0].get("event") == "appeal"
                                   and mine[0].get("status") == "under_review"
                                   and mine[0].get("reasoning") == reasoning and appeal_at > decision_at)
        item["content_status"] = requests.get(f"{url}/content/{cid}").json().get("status")
        item["passed"] = (item["appeal_status"] == 200 and item["appeal_body_status"] == "under_review"
                          and item["appeal_entry_ok"] and item["content_status"] == "under_review")

    return {
        "items": items,
        "originals_byte_identical": after[:len(saved)] == saved,
        "unknown_id": {"status": unknown.status_code, "error": unknown.json().get("error"), "log_entries_written": unknown_wrote},
        "missing_reasoning": {"status": missing.status_code},
        "appeals_passed": sum(i["passed"] for i in items),
        "guesses": sorted({i["guess"] for i in items}),
    }


def bad_input_trial(url, trial, as_written=False):
    """Criterion 5: nine malformed requests — status codes and the log they leave.

    `as_written` sends every body as creator_id "x", exactly as criteria.md lists
    them, so they share one rate-limit bucket.
    """
    before = log_lines()
    results = []
    for i, (body, expected) in enumerate(scenarios.BAD_INPUT, 1):
        if "creator_id" in body:
            body = {**body, "creator_id": "x" if as_written else f"chk_bad_t{trial}_{i}"}
        r = requests.post(f"{url}/submit", json=body)
        results.append({"case": i, "expected": expected, "status": r.status_code})
    r = requests.post(f"{url}/submit", data="not json", headers={"Content-Type": "application/json"})
    results.append({"case": "non-JSON body", "expected": 400, "status": r.status_code})

    added = new_entries(before)
    return {
        "results": results,
        "correct_codes": sum(r["status"] == r["expected"] for r in results),
        "got_200_or_500": sum(r["status"] in (200, 500) for r in results),
        "new_rejected_with_reason": sum(e.get("event") == "rejected" and bool(e.get("reason")) for e in added),
        "new_decided": sum(e.get("status") == "decided" for e in added),
        "rejected_with_content_id": sum(e.get("event") == "rejected" and "content_id" in e for e in added),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--trials", type=int, default=3)
    parser.add_argument("--label", default="")
    parser.add_argument("--url", default=f"http://{config.HOST}:{config.PORT}")
    parser.add_argument("--as-written", action="store_true",
                        help='criterion 5 only, every body as creator_id "x" as in criteria.md')
    args = parser.parse_args()

    runs = {"criterion 4 — appeals": appeal_trial, "criterion 5 — bad input (log side)": bad_input_trial}
    if args.as_written:
        runs = {"criterion 5 — bad input, as written (creator_id \"x\")":
                lambda url, t: bad_input_trial(url, t, as_written=True)}
    lines = [f"# Checks{f' — {args.label}' if args.label else ''}", "",
             "- Produced by: `run_checks.py::appeal_trial`, `run_checks.py::bad_input_trial`",
             f"- {args.trials} trials · {dt.datetime.now():%Y-%m-%d %H:%M}", ""]
    for name, fn in runs.items():
        lines += [f"## {name}", ""]
        for t in range(1, args.trials + 1):
            out = fn(args.url, t)
            summary = {k: v for k, v in out.items() if k not in ("items", "results")}
            print(f"{name} · trial {t}: {summary}")
            lines += [f"**Trial {t}**", "", "```json", json.dumps(out, indent=2), "```", ""]

    config.RESULTS_DIR.mkdir(exist_ok=True)
    path = config.RESULTS_DIR / f"checks_{dt.datetime.now():%Y-%m-%d_%H%M}{'_' + args.label if args.label else ''}.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {path.relative_to(config.ROOT)}")


if __name__ == "__main__":
    main()
