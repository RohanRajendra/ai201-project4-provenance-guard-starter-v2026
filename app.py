#!/usr/bin/env python3
"""
Provenance Guard — the web service.

    python app.py

Then, in another terminal:

    curl -X POST http://127.0.0.1:5000/ping \
      -H "Content-Type: application/json" \
      -d '{"message": "hello"}'

That's the example route. It works right now, before you've written anything.
**Leave it alone** — it's your control. When something breaks later, check that
`/ping` still answers: if it does, the problem is in your handler; if it
doesn't, it's the service itself.

Routes:

    POST /ping        the worked example. Already works. Don't edit it
    POST /submit      judge a piece of text
    POST /appeal      a writer contests a decision
    GET  /content/<id> one item's current status (stretch)
    GET  /verify/prompt  verified-writer check, step 1 (stretch)
    POST /verify      verified-writer check, step 2 (stretch)
    GET  /log         the audit log. Already works
    GET  /health      is the service up, and is the model loaded
"""

import random
import uuid
from datetime import datetime, timedelta, timezone

from flask import Flask, jsonify, request

import audit
import config
import detector
import markers
import scoring
import stylometry

app = Flask(__name__)


# ── Rate limiting — UNIT 8 ────────────────────────────────────────────────────
# Off until you turn it on. In unit 8, Milestone 1:
#
#   1. Set RATE_LIMITING_ENABLED = True in config.py (or AI201_RATE_LIMITS=1)
#   2. Choose your numbers there
#   3. Uncomment the @limiter.limit(...) line on /submit below
#
# The order doesn't matter. While limiting is off, that decorator is a no-op
# that quietly does nothing, so uncommenting it early costs you nothing — but
# it also means no 429 until you've done step 1.
#
# The storage backend is preconfigured, which stops Flask-Limiter printing a
# warning on every start. In-memory is right for one laptop and wrong for
# anything real — a restart forgets every count.

class _LimiterOff:
    """
    Stands in for the real limiter while rate limiting is off.

    It makes @limiter.limit(...) a decorator that returns the route
    untouched, so uncommenting the line before you flip the setting is
    harmless instead of a crash on startup.
    """

    def limit(self, *args, **kwargs):
        return lambda view: view


limiter = _LimiterOff()
if config.RATE_LIMITING_ENABLED:
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address

    def rate_limit_key():
        """
        Who a request counts against.

        Falling back to the caller's address is the easy version. Unit 8's
        stretch asks about per-creator limits instead — and the difference
        matters: one script can look like a thousand callers, and one household
        can look like one.
        """
        payload = request.get_json(silent=True)
        # A body that parses as JSON but isn't an object — a bare list or
        # string — has no .get. Without this guard the key function raises
        # BEFORE the route runs, and a malformed request becomes a 500 that
        # looks like your handler crashed when your handler never ran.
        if not isinstance(payload, dict):
            return get_remote_address()
        creator = payload.get("creator_id")
        return creator if isinstance(creator, str) and creator.strip() else get_remote_address()

    limiter = Limiter(
        key_func=rate_limit_key,
        app=app,
        storage_uri=config.RATE_LIMIT_STORAGE,
        default_limits=[],
    )

    @app.errorhandler(429)
    def rate_limited(exc):
        """
        A rejected request still leaves a trace.

        ⚠️ An attack that shows up only as an absence is one you'll never find.
        """
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            payload = {}
        audit.log_rejection(
            creator_id=payload.get("creator_id", "unknown"),
            reason="rate_limited",
            limit=str(exc.description),
        )
        return jsonify({
            "error": "rate_limited",
            "message": "Too many submissions. Try again shortly.",
            "limit": str(exc.description),
        }), 429


# ── The worked example. Already works. Don't edit. ────────────────────────────

@app.post("/ping")
def ping():
    """
    Everything a route needs, in six lines.

    JSON arrives as a dict. You pull things out of it. You return a dict and
    the framework turns it into a response. That's the whole idea.
    """
    payload = request.get_json(silent=True) or {}
    return jsonify({
        "ok": True,
        "you_sent": payload.get("message"),
        "service": "provenance-guard",
    })


@app.get("/health")
def health():
    """Is the service up, and has the model been downloaded yet?"""
    import detector

    loaded = detector._model is not None
    return jsonify({
        "ok": True,
        "detector_model": config.DETECTOR_MODEL,
        "detector_loaded": loaded,
        "rate_limiting": config.RATE_LIMITING_ENABLED,
        "log_entries": len(audit.read_entries()),
    })


# ── YOU BUILD THIS ────────────────────────────────────────────────────────────

@app.post("/submit")
# @limiter.limit(f"{config.RATE_LIMIT_PER_MINUTE}/minute;{config.RATE_LIMIT_PER_DAY}/day")
def submit():
    """
    Take a piece of text, decide about it, log the decision, answer.

    Expects JSON {"text": "...", "creator_id": "..."}. Anything the service
    can't judge is refused with a 4xx and logged as a rejection — see the
    endpoint contract in README.md.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _reject("unknown", 400, "invalid_input", "Send a JSON object with text and creator_id.")

    creator_id = payload.get("creator_id")
    if not isinstance(creator_id, str) or not creator_id.strip():
        return _reject("unknown", 400, "invalid_input", "creator_id must be a non-empty string.")

    text = payload.get("text")
    if not isinstance(text, str) or not text.strip():
        return _reject(creator_id, 400, "invalid_input", "text must be a non-empty string.")
    if len(text) > config.MAX_TEXT_CHARS:
        return _reject(creator_id, 413, "too_long", f"text is over {config.MAX_TEXT_CHARS:,} characters.")
    if len(stylometry.words(text)) < config.MIN_WORDS:
        return _reject(creator_id, 422, "too_short", f"text needs at least {config.MIN_WORDS} words to score.")

    content_id = str(uuid.uuid4())
    scores = _score(text)
    guess, label = scoring.score_to_label(scores["confidence"])
    verified = _is_verified(creator_id)
    if verified:
        label += " " + scoring.VERIFIED_NOTE

    audit.log_decision(
        content_id=content_id, creator_id=creator_id, guess=guess,
        model_score=scores["model_score"], style_score=scores["style_score"],
        combined_score=scores["confidence"], label=label,
        marker_score=scores["marker_score"], verified_writer=verified,
    )
    return jsonify({
        "content_id": content_id,
        "creator_id": creator_id,
        "guess": guess,
        "label": label,
        **scores,
        "status": "decided",
        "verified_writer": verified,
    })


def _score(text: str) -> dict:
    """All three signals and the combined score for one text."""
    model_score = detector.model_signal(text)
    style_score = stylometry.style_signal(text)
    marker_score = markers.marker_signal(text)
    return {
        "confidence": scoring.combine_signals(model_score, style_score, marker_score),
        "model_score": model_score,
        "style_score": style_score,
        "marker_score": marker_score,
    }


def _reject(creator_id: str, code: int, error: str, message: str):
    """Refuse a request, and leave a trace of it in the log."""
    audit.log_rejection(creator_id=creator_id, reason=error, http_status=code)
    return jsonify({"error": error, "message": message}), code


@app.post("/appeal")
def appeal():
    """
    A writer says you got it wrong. Expects JSON {"content_id", "reasoning"}.

    Appends the appeal beside the original decision (the log is append-only,
    so the decision is never overwritten) and moves the item to under_review.
    A bad request writes nothing — there's no decision for it to sit beside.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "invalid_input", "message": "Send a JSON object with content_id and reasoning."}), 400

    content_id, reasoning = payload.get("content_id"), payload.get("reasoning")
    if not isinstance(content_id, str) or not content_id.strip():
        return jsonify({"error": "invalid_input", "message": "content_id must be a non-empty string."}), 400
    if not isinstance(reasoning, str) or not reasoning.strip():
        return jsonify({"error": "invalid_input", "message": "reasoning must be a non-empty string."}), 400

    decision = _decision_for(content_id)
    if decision is None:
        return jsonify({"error": "not_found", "message": f"No submission with content_id {content_id}."}), 404

    audit.log_appeal(content_id=content_id, creator_id=decision["creator_id"], reasoning=reasoning)
    return jsonify({
        "content_id": content_id,
        "status": "under_review",
        "message": "Thanks — your appeal is recorded. A person will review this "
                   "piece, and it shows as under review until then.",
    })


@app.get("/content/<content_id>")
def content(content_id):
    """One item's current status, rebuilt from the audit log. (Stretch.)"""
    decision = _decision_for(content_id)
    if decision is None:
        return jsonify({"error": "not_found", "message": f"No submission with content_id {content_id}."}), 404

    entries = audit.entries_for(content_id)
    appeals = [e for e in entries if e.get("event") == "appeal"]
    return jsonify({
        "content_id": content_id,
        "creator_id": decision["creator_id"],
        "status": entries[-1]["status"],
        "guess": decision["guess"],
        "confidence": decision["combined_score"],
        "label": decision["label"],
        "model_score": decision["model_score"],
        "style_score": decision["style_score"],
        "marker_score": decision.get("marker_score"),
        "verified_writer": decision.get("verified_writer", False),
        "submitted_at": decision["timestamp"],
        "appeals": [{"timestamp": e["timestamp"], "reasoning": e["reasoning"]} for e in appeals],
    })


def _decision_for(content_id: str) -> dict | None:
    """The original decision entry for an id, or None if there isn't one."""
    return next((e for e in audit.entries_for(content_id) if e.get("status") == "decided"), None)


# ── Verified writer (stretch) ─────────────────────────────────────────────────

@app.get("/verify/prompt")
def verify_prompt():
    """
    Step 1 of the verified-writer check: issue a fresh prompt.

        curl "http://127.0.0.1:5000/verify/prompt?creator_id=writer_03"
    """
    creator_id = request.args.get("creator_id", "").strip()
    if not creator_id:
        return jsonify({"error": "invalid_input", "message": "creator_id is required."}), 400

    challenge_id, prompt = str(uuid.uuid4()), random.choice(config.VERIFY_PROMPTS)
    audit.log_event("verify_prompt", creator_id, challenge_id=challenge_id, prompt=prompt)
    return jsonify({
        "challenge_id": challenge_id,
        "prompt": prompt,
        "instructions": f"Answer in your own words, at least {config.VERIFY_MIN_WORDS} "
                        f"words, within {config.VERIFY_WINDOW_MINUTES} minutes.",
    })


@app.post("/verify")
def verify():
    """
    Step 2: score the writer's answer. Expects {creator_id, challenge_id, text}.
    Passes if the answer is NOT labeled AI; a pass earns the credential.
    """
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify({"error": "invalid_input", "message": "Send a JSON object."}), 400
    creator_id, challenge_id, text = (payload.get(k) for k in ("creator_id", "challenge_id", "text"))
    if not all(isinstance(v, str) and v.strip() for v in (creator_id, challenge_id, text)):
        return jsonify({"error": "invalid_input", "message": "creator_id, challenge_id and text are required."}), 400

    entries = [e for e in audit.read_entries() if e.get("challenge_id") == challenge_id]
    issued = next((e for e in entries if e["event"] == "verify_prompt" and e["creator_id"] == creator_id), None)
    if issued is None:
        return jsonify({"error": "not_found", "message": "No prompt with that challenge_id for this creator."}), 404
    if any(e["event"] == "verify_result" for e in entries):
        return jsonify({"error": "already_used", "message": "That prompt was already answered. Ask for a new one."}), 409
    deadline = datetime.fromisoformat(issued["timestamp"]) + timedelta(minutes=config.VERIFY_WINDOW_MINUTES)
    if datetime.now(timezone.utc) > deadline:
        return jsonify({"error": "expired", "message": "That prompt has expired. Ask for a new one."}), 410
    if not (config.VERIFY_MIN_WORDS <= len(stylometry.words(text)) and len(text) <= config.MAX_TEXT_CHARS):
        return jsonify({"error": "invalid_length", "message": f"Write at least {config.VERIFY_MIN_WORDS} words."}), 422

    scores = _score(text)
    guess, _ = scoring.score_to_label(scores["confidence"])
    passed = guess != "ai"
    audit.log_event("verify_result", creator_id, challenge_id=challenge_id, passed=passed, guess=guess, **scores)
    return jsonify({
        "creator_id": creator_id,
        "verified_writer": _is_verified(creator_id),
        "passed": passed,
        "message": "Thanks — you're now a verified writer. Your work will show it."
                   if passed else "This sample didn't pass. You can ask for a new prompt and try again.",
    })


def _is_verified(creator_id: str) -> bool:
    """Has this creator ever passed the verified-writer check?"""
    return any(e.get("event") == "verify_result" and e.get("passed") and e.get("creator_id") == creator_id
               for e in audit.read_entries())


# ── Already works ─────────────────────────────────────────────────────────────

@app.get("/log")
def get_log():
    """
    The audit log, most recent last.

        curl "http://127.0.0.1:5000/log?limit=10"

    You need this in unit 8 to paste entries into your README, and you need it
    now to see whether your logging is actually working.
    """
    limit = request.args.get("limit", type=int)
    entries = audit.read_entries(limit=limit)
    return jsonify({"count": len(entries), "entries": entries})


def main():
    print(f"Provenance Guard on http://{config.HOST}:{config.PORT}")
    print(f"  detector model:  {config.DETECTOR_MODEL}")
    print(f"  rate limiting:   {'ON' if config.RATE_LIMITING_ENABLED else 'off (unit 8)'}")
    print(f"  audit log:       {config.AUDIT_LOG}")
    print()
    print("Check it's alive:")
    print(f'  curl -X POST http://{config.HOST}:{config.PORT}/ping \\')
    print('    -H "Content-Type: application/json" \\')
    print("    -d '{\"message\": \"hello\"}'")
    print()
    # debug=True hands out an interactive debugger, so it's local-only — see config.py
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)


if __name__ == "__main__":
    main()
