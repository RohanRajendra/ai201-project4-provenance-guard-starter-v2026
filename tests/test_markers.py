"""Signal three, tested as plain functions."""

import unittest

import markers


class MarkerHits(unittest.TestCase):
    def test_cases(self):
        cases = [
            ("Moreover, it is important to note this.", ["moreover", "it is important to note"]),
            ("MOREOVER", ["moreover"]),                           # case-insensitive
            ("Overall, fine.", ["overall,"]),
            ("Overall it was fine.", []),                         # "overall," needs its comma
            ("We delved into it.", []),                           # whole phrases only
            ("A rich tapestry of a wide range of ideas.", ["tapestry", "a wide range of"]),
            ("Nothing to see here.", []),
            ("", []),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(markers.marker_hits(text), expected)


class MarkerSignal(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(markers.marker_signal(""), 0.0)
        self.assertEqual(markers.marker_signal("plain words with no stock phrases at all"), 0.0)
        # 1 marker in 100 words = 1/3 of saturation
        self.assertAlmostEqual(markers.marker_signal("moreover " + "word " * 99), round(1 / 3, 4))
        # 3+ per 100 words saturates
        self.assertEqual(markers.marker_signal("moreover furthermore additionally " + "word " * 7), 1.0)

    def test_non_latin_text_counts_words(self):
        # 1 marker across 1 + 99 Arabic words must be diluted like any other text
        text = "moreover " + "كلمة " * 99
        self.assertAlmostEqual(markers.marker_signal(text), round(1 / 3, 4))


if __name__ == "__main__":
    unittest.main()
