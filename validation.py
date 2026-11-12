"""
What POST /submit accepts — as a plain function, so it can be tested without
Flask, the model or the rate limiter (tests/test_validation.py).

    creator_id, text, removed = parse_submission(payload)   # or raises Refused
"""

import config
import sanitize
import stylometry


class Refused(Exception):
    """A request the service won't judge: the status, error code and message to send back."""

    def __init__(self, code: int, error: str, message: str, creator_id: str = "unknown"):
        super().__init__(message)
        self.code, self.error, self.message, self.creator_id = code, error, message, creator_id


def parse_submission(payload) -> tuple[str, str, int]:
    """
    (creator_id, the text to score, characters stripped from it) — or raise Refused.

    Injected instructions are stripped *before* the 20-word check, so a
    submission that is nothing but instructions is refused as too short.
    """
    if not isinstance(payload, dict):
        raise Refused(400, "invalid_input", "Send a JSON object with text and creator_id.")

    creator_id = payload.get("creator_id")
    if not isinstance(creator_id, str) or not creator_id.strip():
        raise Refused(400, "invalid_input", "creator_id must be a non-empty string.")

    text = payload.get("text")
    if not isinstance(text, str) or not text.strip():
        raise Refused(400, "invalid_input", "text must be a non-empty string.", creator_id)
    if len(text) > config.MAX_TEXT_CHARS:
        raise Refused(413, "too_long", f"text is over {config.MAX_TEXT_CHARS:,} characters.", creator_id)

    text, removed = sanitize.strip_instructions(text)
    if len(stylometry.words(text)) < config.MIN_WORDS:
        raise Refused(422, "too_short", f"text needs at least {config.MIN_WORDS} words to score.", creator_id)
    return creator_id, text, removed
