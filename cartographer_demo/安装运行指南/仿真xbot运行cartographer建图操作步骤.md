## 仿真xbot运行cartographer建图操作步骤

- 1.启动仿真xbot：
```
cd ~/catkin_ws   #~/为ROS-Academy-for-Beginners-melodic代码工作空间
source devel/setup.bash
roslaunch robot_sim_demo robot_spawn.launch
```
- 2.启动Cartographer
```
cd ~/catkin_carto #~/catkin_carto为Cartographer代码工作空间
source install_isolated/setup.bash
roslaunch cartographer_ros cartographer_demo.launch
```
- 3.启动机器人控制代码，控制建图
```
cd ~/catkin_ws   #~/为ROS-Academy-for-Beginners-melodic代码工作空间
source devel/setup.bash
rosrun robot_sim_demo robot_keyboard_teleop.py
```
启动效果如下：
![image](/uploads/b25a5e234f9b3cb6d3b61b2b9d10f5c4/image.png)

建图完成后截图如下：
![image](/uploads/e9c54b604a81dd93d1c6eee25bc5d9bc/image.png)

保存地图：
![image](/uploads/7b8d531647c0b6c0c9eb24727e973deb/image.png)
