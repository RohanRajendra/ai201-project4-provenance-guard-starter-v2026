"""
Signal two: the style signal.

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures, each mapped to 0–1 AI-likeness and weighted into one score.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures ───────────────────────────────────────────────────────

# Punctuation that varies between writers. Full stops and commas don't — every
# writer uses them — so they're left out.
EXPRESSIVE_PUNCTUATION = re.compile(r"[;:!?()\u2014\u2013\u2026\"]|--")

# Window for the moving-average type-token ratio. Plain TTR falls as text gets
# longer; averaging over fixed windows makes a 60-word and a 600-word text
# comparable.
TTR_WINDOW = 50


def sentence_length_spread(text: str) -> float:
    """
    Coefficient of variation of sentence lengths in words (stdev / mean).
    0.0 = every sentence the same length. **Higher = more human.**

    Fewer than two sentences has no spread to measure, so it returns 0.0 —
    and `style_signal` treats that case as no evidence rather than as AI.
    """
    lengths = [len(words(s)) for s in sentences(text)]
    lengths = [n for n in lengths if n]
    if len(lengths) < 2:
        return 0.0
    return statistics.stdev(lengths) / statistics.mean(lengths)


def type_token_ratio(text: str) -> float:
    """
    Moving-average type-token ratio over 50-word windows, 0–1.
    **Higher = more varied vocabulary = more human.** Under 50 words it falls
    back to plain unique/total.
    """
    w = words(text)
    if not w:
        return 0.0
    if len(w) <= TTR_WINDOW:
        return len(set(w)) / len(w)
    windows = [w[i:i + TTR_WINDOW] for i in range(len(w) - TTR_WINDOW + 1)]
    return statistics.mean(len(set(win)) / TTR_WINDOW for win in windows)


def punctuation_density(text: str) -> float:
    """
    Expressive punctuation marks (; : ! ? ( ) dashes ellipses quotes) per 100
    words. **Higher = more human.**
    """
    w = words(text)
    if not w:
        return 0.0
    return 100 * len(EXPRESSIVE_PUNCTUATION.findall(text)) / len(w)


# ── Combining them ───────────────────────────────────────────────────────────

# Each measure is mapped onto 0–1 AI-likeness with a straight line between two
# anchors: at or past the "human" anchor it scores 0, at or past the "AI"
# anchor it scores 1. Anchors set from the Milestone 4 calibration inputs.
SPREAD_ANCHORS = (0.65, 0.25)   # (human, AI) coefficient of variation
TTR_ANCHORS = (0.86, 0.72)      # (human, AI) moving-average TTR
PUNCT_ANCHORS = (4.0, 0.0)      # (human, AI) marks per 100 words


def _ai_likeness(value: float, anchors: tuple[float, float]) -> float:
    human, ai = anchors
    return min(max((value - human) / (ai - human), 0.0), 1.0)


def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    All three measures point the same way raw (higher = more human), so each
    is flipped by `_ai_likeness`, then weighted 0.4 spread / 0.2 TTR / 0.4
    punctuation. TTR gets half weight because it ran *backwards* in
    calibration: the stock AI paragraph had the most varied vocabulary (0.92)
    of the five inputs. With fewer than 3 sentences the spread measure is
    unreliable and is replaced by a neutral 0.5.
    """
    spread = (
        _ai_likeness(sentence_length_spread(text), SPREAD_ANCHORS)
        if len(sentences(text)) >= 3 else 0.5
    )
    ttr = _ai_likeness(type_token_ratio(text), TTR_ANCHORS)
    punct = _ai_likeness(punctuation_density(text), PUNCT_ANCHORS)
    return round(0.4 * spread + 0.2 * ttr + 0.4 * punct, 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
