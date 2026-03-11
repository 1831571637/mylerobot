# mylerobot
# 目标：把 LeRobot 的硬件部分替换成你自己的机械臂 + 执行器平台
# 保持不变：数据采集、回放、训练、推理流程尽量沿用 LeRobot
# 必须新写：robot adapter、teleop adapter、processor、必要的 policy 输入扩展
# 当前硬件：
# 机械臂自由度
# 灵巧手/夹爪自由度
# 相机数量与型号
# 是否有力觉/触觉
# 底层控制接口：ROS1 / ROS2 / TCP / CAN / SDK
# 当前目标任务：
# 先跑通 teleop / record / replay
# 再跑训练
# 最后做真机部署
