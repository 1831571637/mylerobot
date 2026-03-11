from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np

from mylerobot.config import load_dataset_config


def convert_episode_file(input_path: Path, output_path: Path) -> None:
    """
    Convert user-collected raw npz into standardized training npz.

    Expected raw keys:
      - image
      - state
      - xyzrpy_action OR action
      - timestamp
      - episode_id
    """
    raw = np.load(input_path, allow_pickle=True)

    images = raw["image"].astype(np.uint8)
    state = raw["state"].astype(np.float32)
    if "action" in raw:
        action = raw["action"].astype(np.float32)
    else:
        # Placeholder: in practice, replace with xyzrpy->joint conversion processor.
        action = raw["xyzrpy_action"].astype(np.float32)

    timestamp = raw["timestamp"].astype(np.float64)
    episode_id = raw["episode_id"]

    np.savez_compressed(
        output_path,
        image=images,
        state=state,
        action=action,
        timestamp=timestamp,
        episode_id=episode_id,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    cfg = load_dataset_config(args.config)
    raw_dir = Path(cfg.raw_data_dir)
    out_dir = Path(cfg.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for src in sorted(raw_dir.glob("*.npz")):
        dst = out_dir / src.name
        convert_episode_file(src, dst)
        print(f"Converted {src.name} -> {dst}")


if __name__ == "__main__":
    main()
