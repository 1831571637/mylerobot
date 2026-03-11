from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class SafetyConfig:
    action_min: list[float]
    action_max: list[float]
    max_delta_per_step: float = 0.05


@dataclass(slots=True)
class RobotConfig:
    name: str
    control_hz: int
    arm_dof: int
    hand_dof: int
    cameras: list[str]
    units: dict[str, str]
    safety: SafetyConfig


@dataclass(slots=True)
class DatasetConfig:
    raw_data_dir: str
    output_dir: str
    image_key: str
    state_key: str
    action_key: str
    timestamp_key: str
    episode_key: str
    target_hz: int = 20


@dataclass(slots=True)
class TrainingConfig:
    dataset_repo_id: str
    policy: str
    output_dir: str
    batch_size: int
    steps: int


def _load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_robot_config(path: str | Path) -> RobotConfig:
    data = _load_yaml(path)
    safety = SafetyConfig(**data["safety"])
    return RobotConfig(
        name=data["name"],
        control_hz=data["control_hz"],
        arm_dof=data["arm_dof"],
        hand_dof=data["hand_dof"],
        cameras=data["cameras"],
        units=data["units"],
        safety=safety,
    )


def load_dataset_config(path: str | Path) -> DatasetConfig:
    return DatasetConfig(**_load_yaml(path))


def load_training_config(path: str | Path) -> TrainingConfig:
    return TrainingConfig(**_load_yaml(path))
