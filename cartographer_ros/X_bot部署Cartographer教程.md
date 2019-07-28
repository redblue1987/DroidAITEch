## X_bot部署Cartographer教程

机器上部署Cartographer后
### 修改代码：
- 1./src/cartographer_ros/cartographer_ros/launch/`demo_revo_lds.launch`文件：
 <br>将`<remap from="scan" to="horizontal_laser_2d" />`修改为`<remap from="scan" to="scan" />`<remap from="scan" to="scan" />

- 2 ./src/cartographer_ros/cartographer_ros/configuration_files/`revo_lds.lua`文件用[revo_lds.lua](/uploads/ffb6c51da11556041c2fb0fcf3f64803/revo_lds.lua)替换
### 启动X_bot及Cartographer
- 1.启动X_bot：
```
cd ~/ROS #~/ROS为X_bot代码工作空间
source devel/setup.bash
roslaunch robot_sim_demo robot_spawn.launch
```
- 2.启动Cartographer
```
cd ~/catkin_ws #~/catkin_ws为Cartographer代码工作空间
source install_isolated/setup.bash
roslaunch cartographer_ros demo_revo_lds.launch
```
- 3.启动机器人控制代码，控制建图
```
cd ~/ROS #~/ROS为X_bot代码工作空间
source devel/setup.bash
rosrun robot_sim_demo robot_keyboard_teleop.py
```
启动效果如下：
![image](/uploads/b25a5e234f9b3cb6d3b61b2b9d10f5c4/image.png)

建图完成后截图如下：
![image](/uploads/e9c54b604a81dd93d1c6eee25bc5d9bc/image.png)

保存地图：
![image](/uploads/7b8d531647c0b6c0c9eb24727e973deb/image.png)
