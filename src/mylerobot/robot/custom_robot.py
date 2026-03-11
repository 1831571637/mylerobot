from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from mylerobot.config import RobotConfig
from mylerobot.schemas import Observation


@dataclass(slots=True)
class ConnectionState:
    connected: bool = False


class CustomRobot:
    """Minimal custom robot adapter skeleton for LeRobot integration."""

    def __init__(self, config: RobotConfig) -> None:
        self.config = config
        self.connection = ConnectionState(connected=False)
        self._last_action = np.zeros(config.arm_dof + config.hand_dof, dtype=np.float32)
        self._step = 0

    def connect(self) -> None:
        # TODO: initialize ROS2 nodes and vendor SDK handles.
        self.connection.connected = True

    def disconnect(self) -> None:
        self.connection.connected = False

    def get_observation(self) -> Observation:
        if not self.connection.connected:
            raise RuntimeError("Robot is not connected")

        # TODO: replace with live camera + state acquisition.
        image = np.zeros((480, 640, 3), dtype=np.uint8)
        state = np.zeros(self.config.arm_dof + self.config.hand_dof, dtype=np.float32)
        ts = self._step / float(self.config.control_hz)
        self._step += 1
        return Observation(image=image, state=state, timestamp=ts)

    def send_action(self, action: np.ndarray) -> np.ndarray:
        if not self.connection.connected:
            raise RuntimeError("Robot is not connected")
        clipped = np.clip(action, self.config.safety.action_min, self.config.safety.action_max)
        self._last_action = clipped.astype(np.float32)
        # TODO: publish/command through ROS2 + SDK.
        return self._last_action
