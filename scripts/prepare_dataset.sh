#!/usr/bin/env bash
set -euo pipefail
python -m mylerobot.dataset.prepare_dataset --config configs/dataset.yaml
python -m mylerobot.dataset.check_dataset --config configs/dataset.yaml
