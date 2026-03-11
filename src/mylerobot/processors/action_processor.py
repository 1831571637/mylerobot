from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class ActionBounds:
    lower: np.ndarray
    upper: np.ndarray


class XYZRPYToJointProcessor:
    """
    Converts xyzrpy action vectors to joint actions.

    Note:
        This is intentionally a lightweight placeholder. Plug in your vendor IK solver
        / ROS2 service in `solve_ik` for production use.
    """

    def __init__(self, arm_dof: int, hand_dof: int, bounds: ActionBounds) -> None:
        self.arm_dof = arm_dof
        self.hand_dof = hand_dof
        self.bounds = bounds

    def solve_ik(self, xyzrpy: np.ndarray, current_joints: np.ndarray) -> np.ndarray:
        if xyzrpy.shape != (6,):
            raise ValueError(f"Expected xyzrpy shape (6,), got {xyzrpy.shape}")
        if current_joints.shape[0] != self.arm_dof:
            raise ValueError("Current arm joint size does not match arm_dof")

        # TODO: replace with vendor SDK / MoveIt IK.
        # Fallback behavior keeps arm unchanged until IK is wired.
        return current_joints.copy()

    def process(self, xyzrpy: np.ndarray, current_arm: np.ndarray, hand_targets: np.ndarray) -> np.ndarray:
        arm_targets = self.solve_ik(xyzrpy, current_arm)
        full = np.concatenate([arm_targets, hand_targets], axis=0)
        return np.clip(full, self.bounds.lower, self.bounds.upper)
