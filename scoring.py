"""
Turning three numbers into one, and one number into something a person can read.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float, marker_score: float) -> float:
    """
    Combine three 0–1 signals into one 0–1 score. Higher = more likely AI.

    The rule:
      1. Weighted average — model 0.50, style 0.25, marker 0.25 (config.py).
      2. Agreement: if ANY signal is under AGREEMENT_FLOOR (0.60), the result
         is capped at AI_THRESHOLD − 0.01, so the item can't be labeled AI.
         Disagreeing signals are uncertainty, and uncertainty never accuses.
    """
    scores = (model_score, style_score, marker_score)
    score = (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
        + config.WEIGHT_MARKER_SIGNAL * marker_score
    )
    if min(scores) < config.AGREEMENT_FLOOR:
        score = min(score, config.AI_THRESHOLD - 0.01)
    return round(min(max(score, 0.0), 1.0), 4)


LABELS = {
    "human": "This piece looks like it was written by a person.",
    "unsure": (
        "We couldn't tell whether this piece was written by a person or by an "
        "AI tool. Many people's own writing gets this result, so it is not a "
        "sign that anything was done wrong. If you wrote this, you can ask for "
        "a person to review it."
    ),
    "ai": (
        "Our check found strong signs that this piece may have been written by "
        "an AI tool, but this is not proof and the check can be wrong. Nothing "
        "has been taken down. If you wrote this, you can ask for a person to "
        "review it and tell them how you wrote it."
    ),
}


# Appended to any label on work by a creator who passed the verified-writer
# check (stretch). It adds a fact about the writer; it never changes the guess.
VERIFIED_NOTE = "This writer has completed our live writing check."


def score_to_label(score: float) -> tuple[str, str]:
    """
    Turn a score into (guess, label_text).

        score <  0.40          -> human
        0.40 <= score < 0.85   -> unsure
        score >= 0.85          -> ai

    Every score in 0–1 maps to exactly one band — no gaps at the edges.
    """
    if score >= config.AI_THRESHOLD:
        guess = "ai"
    elif score < config.HUMAN_THRESHOLD:
        guess = "human"
    else:
        guess = "unsure"
    return guess, LABELS[guess]


def label_ranges() -> list[tuple[str, str]]:
    """
    The score range each label covers. Your README needs these beside the
    label text — given to you so the numbers can't drift apart from config.py.
    """
    return [
        ("high-confidence human", f"0.00 – under {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – under {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
