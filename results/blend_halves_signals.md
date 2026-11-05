# Criterion 3 blends — each half scored alone — 2026-11-04 22:53

Scored offline with the service's own signal functions
(`detector.model_signal`, `stylometry.style_signal`, `markers.marker_signal`).
Neither unit 8 improvement changed a signal, so these match what `/submit`
would compute. Halves are built by `scenarios.py::_half`, the same way the
blends are.

| Blend | Half | Words | model | style | marker |
|---|---|---|---|---|---|
| my #5 + AI on ant colonies | my first half | 130 | 0.456 | 0.686 | 0.0 |
| | AI second half | 143 | 0.236 | 0.499 | 0.0 |
| | whole blend (from the 2214 run) | 273 | 0.331 | 0.556 | 0.0 |
| my #3 + AI on a daily routine | my first half | 143 | 0.504 | 0.494 | 0.0 |
| | AI second half | 149 | 0.273 | 0.609 | 0.0 |
| | whole blend (from the 2214 run) | 292 | 0.370 | 0.463 | 0.0 |
