# mylerobot

面向自定义真机平台的 LeRobot 适配工程，目标是尽量保持 LeRobot 原始流程：

`teleoperation -> record -> replay -> train -> inference`

## 已补齐的工程骨架

- `configs/`：机器人、数据、训练配置（全部 YAML）。
- `src/mylerobot/robot/`：自定义 `CustomRobot` 适配器骨架（connect/disconnect/get_observation/send_action）。
- `src/mylerobot/processors/`：`XYZRPYToJointProcessor` 占位实现（待接入 IK/SDK）。
- `src/mylerobot/dataset/`：数据转换与完整性检查脚本。
- `scripts/`：一键准备数据与生成训练命令脚本（ACT / Diffusion / PI05）。
- `docs/practice_guide.md`：从原始数据到训练的实践步骤。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

准备数据并检查：

```bash
scripts/prepare_dataset.sh
```

生成训练命令：

```bash
scripts/train_act.sh
scripts/train_diffusion.sh
scripts/train_pi05.sh
```

> 注意：脚本只生成 `lerobot-train` 命令模板。你需要在本机安装并配置好 `lerobot` 环境，然后执行生成的命令。
