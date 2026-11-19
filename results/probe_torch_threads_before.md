`loss_type=None` was set in the config but it is unrecognized. Using the default loss: `ForCausalLMLoss`.
# Probe: model stage vs torch threads (diagnosis for C5)

Produced by: inline probe calling `detector.perplexity` directly, no server. BOUNDARY_TEXT = 400 tokens (the cap). Default torch threads: 4, CPUs: 10. 10 runs each after 2 warm-ups.

| threads | wall ms (median) | CPU ms (median) | CPU / wall | score |
|---|---|---|---|---|
| 8 | 187.6 | 483.0 | 2.57 | 0.5214 |
| 4 (default) | 203.1 | 431.1 | 2.12 | 0.5214 |
| 2 | 217.9 | 370.4 | 1.70 | 0.5214 |
| 1 | 308.7 | 369.8 | 1.20 | 0.5214 |
