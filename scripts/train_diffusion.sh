#!/usr/bin/env bash
set -euo pipefail
python -m mylerobot.train_commands --config configs/train_diffusion.yaml
