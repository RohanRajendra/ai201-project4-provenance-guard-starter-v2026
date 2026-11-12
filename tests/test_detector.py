"""Signal one's maths, tested without loading the model."""

import unittest
from unittest import mock

import detector


class Squash(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(detector.squash(45.0), 0.5)      # the midpoint is a coin flip
        self.assertGreater(detector.squash(5.0), 0.95)    # very predictable -> AI-like
        self.assertLess(detector.squash(500.0), 0.03)     # very surprising -> human-like
        values = [detector.squash(p) for p in (2, 10, 30, 45, 80, 200, 1000)]
        self.assertEqual(values, sorted(values, reverse=True))
        for v in values:
            self.assertTrue(0.0 <= v <= 1.0)


class ModelSignal(unittest.TestCase):
    def test_uses_perplexity_without_loading_the_model(self):
        with mock.patch.object(detector, "perplexity", return_value=45.0) as ppl:
            self.assertEqual(detector.model_signal("any text"), 0.5)
            ppl.assert_called_once_with("any text")
        self.assertIsNone(detector._model)


if __name__ == "__main__":
    unittest.main()
