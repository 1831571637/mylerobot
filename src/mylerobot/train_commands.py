from __future__ import annotations

import argparse

from mylerobot.config import load_training_config


def build_command(cfg_path: str) -> str:
    cfg = load_training_config(cfg_path)
    return (
        "lerobot-train "
        f"--policy.type={cfg.policy} "
        f"--dataset.repo_id={cfg.dataset_repo_id} "
        f"--output_dir={cfg.output_dir} "
        f"--training.batch_size={cfg.batch_size} "
        f"--training.steps={cfg.steps}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    print(build_command(args.config))


if __name__ == "__main__":
    main()
