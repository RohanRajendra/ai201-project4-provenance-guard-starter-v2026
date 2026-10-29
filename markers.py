"""
Signal three: the marker signal. (Stretch — a third signal.)

Signal one asks how predictable the text is; signal two measures its shape.
This one asks a narrower question: **does it use the stock phrases chat models
lean on?** Signposting and hedging — "it is important to note", "moreover",
"plays a crucial role", "in conclusion" — show up in generated prose far more
often than in most people's writing.

⚠️ **The blind spot.** It only sees its own list. One pass of paraphrasing
removes every marker, and a person who writes formal essays with those
connectives gets marked up.

    python markers.py "some text to look at"
"""

import re

from stylometry import words

MARKERS = [
    "it is important to note", "it's important to note", "it is worth noting",
    "moreover", "furthermore", "additionally", "in conclusion", "overall,",
    "in today's", "plays a crucial role", "plays a vital role", "crucial",
    "delve", "tapestry", "navigate the", "landscape", "a testament to",
    "foster", "leverage", "seamless", "robust", "holistic", "multifaceted",
    "ultimately", "in summary", "not only", "a wide range of", "various",
    "significant", "essential", "ensure", "enhance", "valuable insights",
]

# Markers per 100 words that scores 1.0. Two in a 100-word paragraph is already
# a lot for a person; stock AI paragraphs in calibration ran 3–6.
SATURATION_RATE = 3.0

_PATTERN = re.compile(
    "|".join(r"\b" + re.escape(m) + (r"\b" if m[-1].isalnum() else "") for m in MARKERS),
    re.IGNORECASE,
)


def marker_hits(text: str) -> list[str]:
    """Every marker found, in order, lowercased."""
    return [m.lower() for m in _PATTERN.findall(text)]


def marker_signal(text: str) -> float:
    """Marker rate per 100 words, scaled to 0–1. **Higher means more likely AI.**"""
    w = words(text)
    if not w:
        return 0.0
    rate = 100 * len(marker_hits(text)) / len(w)
    return round(min(rate / SATURATION_RATE, 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "It is important to note that technology plays a crucial role in "
        "today's world. Moreover, it offers significant benefits."
    )
    print(f"hits           {marker_hits(text)}")
    print(f"marker_signal  {marker_signal(text)}   (higher = more likely AI)")
