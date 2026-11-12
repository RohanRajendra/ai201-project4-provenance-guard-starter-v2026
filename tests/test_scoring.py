"""The combining rule and the label mapping, tested as plain functions."""

import unittest

import config
import scoring


class CombineSignals(unittest.TestCase):
    def test_cases(self):
        cases = [
            # (model, style, marker) -> expected combined score
            ((0.9, 0.9, 0.9), 0.9),       # all agree on AI: plain weighted average
            ((1.0, 1.0, 1.0), 1.0),
            ((0.0, 0.0, 0.0), 0.0),       # all agree on human
            ((0.2, 0.2, 0.2), 0.2),
            ((1.0, 1.0, 0.5), 0.84),      # marker disagrees: capped one point under the AI band
            ((0.16, 0.80, 0.0), 0.40),    # EV01: style says AI, so it can't be labeled human
            ((0.67, 0.23, 0.0), 0.40),    # EV03
            ((0.59, 0.59, 0.0), 0.4425),  # nothing reaches the floor: average stands
        ]
        for signals, expected in cases:
            with self.subTest(signals=signals):
                self.assertAlmostEqual(scoring.combine_signals(*signals), expected)

    def test_disagreement_always_lands_unsure(self):
        for signals in [(0.0, 0.0, 0.6), (0.6, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 1.0)]:
            with self.subTest(signals=signals):
                guess, _ = scoring.score_to_label(scoring.combine_signals(*signals))
                self.assertEqual(guess, "unsure")


class ScoreToLabel(unittest.TestCase):
    def test_boundaries(self):
        cases = [(0.0, "human"), (0.3999, "human"), (0.40, "unsure"), (0.8499, "unsure"),
                 (0.85, "ai"), (1.0, "ai")]
        for score, guess in cases:
            with self.subTest(score=score):
                self.assertEqual(scoring.score_to_label(score), (guess, scoring.LABELS[guess]))

    def test_no_gaps(self):
        for i in range(1001):
            self.assertIn(scoring.score_to_label(i / 1000)[0], scoring.LABELS)

    def test_thresholds_match_config(self):
        self.assertEqual(config.HUMAN_THRESHOLD, 0.40)
        self.assertEqual(config.AI_THRESHOLD, 0.85)


if __name__ == "__main__":
    unittest.main()
