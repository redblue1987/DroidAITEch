# action_demo

### introduce

本demo在课程仿真场景下,演示一个简单的action通讯.运行action之后,会看到xbot在场景中简单的"折返跑".同时,终端打印实时进度,反馈通信进程状态.

### run

1.  打开一个终端:$ roslaunch robot_sim_demo robot_spawn.launch

2. 打开一个新终端:$ rosrun action_test linewalk_server.py

3. 打开一个新终端 $ rosrun action_test linewalk_client.py
