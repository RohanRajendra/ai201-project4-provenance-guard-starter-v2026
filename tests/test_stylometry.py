"""Signal two's pieces, tested as plain functions — no server, no model."""

import unittest

import stylometry as st


class Words(unittest.TestCase):
    def test_cases(self):
        cases = [
            ("Hello, World!", ["hello", "world"]),
            ("I don't know.", ["i", "don't", "know"]),
            ("I don’t know.", ["i", "don’t", "know"]),           # curly apostrophe is one word
            ("A café, naïvely.", ["a", "café", "naïvely"]),       # accented letters stay in the word
            ("مرحبا بالعالم الجميل", ["مرحبا", "بالعالم", "الجميل"]),  # non-Latin script counts
            ("Room 101 opens at 9", ["room", "101", "opens", "at", "9"]),
            ("", []),
            ("... !!! ---", []),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(st.words(text), expected)


class Sentences(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(st.sentences("One. Two! Three?"), ["One.", "Two!", "Three?"])
        self.assertEqual(st.sentences("No full stop"), ["No full stop"])
        self.assertEqual(st.sentences("   "), [])


class Measures(unittest.TestCase):
    def test_spread(self):
        self.assertEqual(st.sentence_length_spread("One sentence only."), 0.0)
        self.assertEqual(st.sentence_length_spread("Two words. Two words. Two words."), 0.0)
        self.assertGreater(st.sentence_length_spread("Short. This one is a good deal longer than that."), 0.6)

    def test_type_token_ratio(self):
        self.assertEqual(st.type_token_ratio(""), 0.0)
        self.assertEqual(st.type_token_ratio("every word here differs"), 1.0)
        self.assertEqual(st.type_token_ratio("the the the the"), 0.25)

    def test_punctuation_density(self):
        cases = [
            ("plain words only here", 0.0),
            ("one; two: three! four?", 100.0),
            ('he said "yes" twice', 50.0),
            ("he said “yes” twice", 50.0),                        # curly quotes are quotes too
            ("", 0.0),
        ]
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertAlmostEqual(st.punctuation_density(text), expected)


class StyleSignal(unittest.TestCase):
    PLAIN = "I went out today. I bought some bread. I came home at six. I ate it all."
    LUMPY = ("I didn't sleep. Not properly, anyway — I lay there listening to the boiler "
             "tick and thinking about what I'd said; it was stupid! Twice now (twice).")

    def test_range_and_direction(self):
        for text in (self.PLAIN, self.LUMPY, "x"):
            with self.subTest(text=text):
                self.assertTrue(0.0 <= st.style_signal(text) <= 1.0)
        self.assertGreater(st.style_signal(self.PLAIN), st.style_signal(self.LUMPY))

    def test_anchors_clamp(self):
        self.assertEqual(st._ai_likeness(0.9, st.SPREAD_ANCHORS), 0.0)
        self.assertEqual(st._ai_likeness(0.1, st.SPREAD_ANCHORS), 1.0)
        self.assertAlmostEqual(st._ai_likeness(0.45, st.SPREAD_ANCHORS), 0.5)


if __name__ == "__main__":
    unittest.main()
