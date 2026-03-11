from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Observation:
    """Deterministic observation schema used by training/inference."""

    image: np.ndarray  # [H, W, C], uint8
    state: np.ndarray  # [state_dim], float32
    timestamp: float


@dataclass(slots=True)
class Action:
    """Joint-position action schema with clipping handled upstream."""

    joint_targets: np.ndarray  # [arm_dof + hand_dof], float32


EXPECTED_SCHEMA = {
    "observation": {
        "image": "uint8[H,W,C]",
        "state": "float32[state_dim]",
        "timestamp": "float64[]",
    },
    "action": {"joint_targets": "float32[action_dim]"},
}
