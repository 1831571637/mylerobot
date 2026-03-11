# AGENTS.md

## Project goal
Port LeRobot hardware integration to our custom real robot platform while preserving the LeRobot workflow:
teleoperation -> record -> replay -> train -> inference.

## Hardware summary
- Arm: 6-DoF industrial arm
- End-effector: 16-DoF dexterous hand
- Cameras: 2 RGB cameras
- Optional sensors: wrist force/torque, tactile arrays
- Middleware: ROS2 + vendor SDK
- Control rate target: 20-30 Hz initially

## Non-goals
- Do not redesign LeRobot training stack unless necessary.
- Do not modify upstream LeRobot source unless unavoidable.
- Prefer plugin/adaptor structure over forking core files.

## Code rules
- Write Python 3.10+.
- Keep adapters modular.
- Separate hardware driver layer from LeRobot interface layer.
- Avoid hardcoding IPs, ports, calibration constants in source files.
- Put all robot-specific config into YAML or dataclass config.

## Migration rules
- Phase 1: joint-state observation + joint-position action + RGB cameras only.
- Phase 2: add teleoperator adapter.
- Phase 3: add processors for action-space conversion.
- Phase 4: add force/tactile observations.
- Phase 5: extend policy input only after replay is stable.

## Acceptance criteria
- Can instantiate custom Robot class.
- Can connect/disconnect cleanly.
- get_observation() returns deterministic schema.
- send_action() supports safe action clipping.
- replay works on recorded episodes.
- record/replay timestamps are aligned.

## Review guidelines
- Prioritize minimal, high-confidence changes.
- Flag unsafe robot motion logic.
- Flag blocking calls in control loops.
- Flag schema mismatches between observation_features and get_observation().
- Flag unit inconsistencies (deg vs rad, mm vs m).
