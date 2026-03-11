# Practice Guide: 从现有数据到 LeRobot 训练

本文档对应你当前数据形态：单目图像 + 机械臂/执行器位姿（xyzrpy）。

## 1. 数据准备

将原始 episode 以 `npz` 放入 `data/raw/`，每个文件至少包含：

- `image`: `[T, H, W, C]`, `uint8`
- `state`: `[T, state_dim]`, `float32`
- `action` 或 `xyzrpy_action`: `[T, action_dim]`, `float32`
- `timestamp`: `[T]`, `float64`
- `episode_id`: `[T]` 或标量

运行：

```bash
scripts/prepare_dataset.sh
```

输出到 `data/processed/`，并进行一致性检查。

## 2. 你必须自行接入的部分

由于机器人、IK 与控制器强平台相关，以下逻辑无法在通用模板中自动补齐，已在代码中留出 TODO：

1. `src/mylerobot/processors/action_processor.py`
   - `solve_ik` 需要接你自己的 IK（MoveIt、厂商 SDK、或自定义求解器）。
2. `src/mylerobot/robot/custom_robot.py`
   - `connect/disconnect/get_observation/send_action` 需要接 ROS2 topic/service 与厂商 SDK。

## 3. 训练模板

先生成命令：

```bash
scripts/train_act.sh
scripts/train_diffusion.sh
scripts/train_pi05.sh
```

再复制命令到已安装 LeRobot 的环境执行。

## 4. 推荐实践顺序

1. 先 ACT 跑通（验证数据链路）。
2. 再 Diffusion（验证时序建模能力）。
3. 最后 PI05（迁移到更强泛化模型）。

## 5. 安全注意事项

- 统一单位（m/rad）。
- 实机推理前必须启用动作 clipping、关节限位和速度限位。
- 若当前 `action` 仍是 xyzrpy，请先转换为 joint-space action 再上实机。
