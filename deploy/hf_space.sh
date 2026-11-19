#!/usr/bin/env bash
# Upload the committed code to a Hugging Face Space (unit 9, stretch 3).
#
#   huggingface-cli login                  # once, with a write token
#   ./deploy/hf_space.sh <user>/<space>    # the Space must already exist (SDK: Docker)
#
# The Space builds the Dockerfile itself. A Space reads its settings from the
# header of README.md, so the upload swaps in deploy/space_card.md.
set -euo pipefail
SPACE=${1:?usage: ./deploy/hf_space.sh <user>/<space-name>}
OUT=$(mktemp -d)
git archive HEAD | tar -x -C "$OUT"
cp deploy/space_card.md "$OUT/README.md"
rm -rf "$OUT/results" "$OUT"/logs/*.jsonl
.venv/bin/huggingface-cli upload "$SPACE" "$OUT" . --repo-type space
echo "Uploaded. Build log: https://huggingface.co/spaces/$SPACE  ·  API: https://${SPACE/\//-}.hf.space"
