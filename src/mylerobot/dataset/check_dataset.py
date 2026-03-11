from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from mylerobot.config import DatasetConfig, load_dataset_config


REQUIRED_KEYS = {"image", "state", "action", "timestamp", "episode_id"}


def validate_file(path: Path) -> tuple[bool, str]:
    data = np.load(path, allow_pickle=True)
    keys = set(data.files)
    missing = REQUIRED_KEYS - keys
    if missing:
        return False, f"missing keys: {sorted(missing)}"

    n = len(data["timestamp"])
    for key in ("image", "state", "action", "episode_id"):
        if len(data[key]) != n:
            return False, f"length mismatch in {key}: {len(data[key])} != {n}"

    ts = np.asarray(data["timestamp"], dtype=np.float64)
    if np.any(np.diff(ts) < 0):
        return False, "timestamps are not monotonic"

    return True, "ok"


def run(cfg: DatasetConfig) -> int:
    folder = Path(cfg.output_dir)
    files = sorted(folder.glob("*.npz"))
    if not files:
        print(f"No .npz files found in {folder}")
        return 1

    report: dict[str, str] = {}
    failed = 0
    for f in files:
        ok, msg = validate_file(f)
        report[f.name] = msg
        if not ok:
            failed += 1

    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failed else 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to dataset config yaml")
    args = parser.parse_args()

    cfg = load_dataset_config(args.config)
    raise SystemExit(run(cfg))


if __name__ == "__main__":
    main()
