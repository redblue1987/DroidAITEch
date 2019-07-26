# rtabmap在仿真环境下的运行操作指南[melodic为例]
### 操作过程
##### 1. 根据自己的ROS版本,安装对应的rtabmap-ros

 * melodic
 ```
 $ sudo apt install ros-melodic-rtabmap-ros
 ```    

 * 	Kinetic
```
$ sudo apt-get install ros-kinetic-rtabmap-ros
```
	其他版本类似.

##### 2. 检查环境变量配置

  检查 `~/.bashrc`文件是否包含下面两句:

    	```
      $ source /opt/ros/melodic/setup.bash
      $ source ~/catkin_ws/devel/setup.bash
      ```

##### 3. 输入指令,开始进行rtabmap rgbd_mapping

		终端1:$ roslaunch robot_sim_demo robot_spawn.launch #启动仿真环境
		终端2:$ roslaunch rtabmap_demo rgbd.launch #启动rtabmap
		终端3:$ rosrun robot_sim_demo robot_keyboard_teleop.py #启动键盘控制


##### 4. 查看地图

```
rtabmap -databaseViewer ~/.ros/rtabmap.db

```

##### 5.可以用/scan进行2D地图的构建,这里不主要演示.

```
终端1:$ roslaunch robot_sim_demo robot_spawn.launch #启动仿真环境
终端2:$ roslaunch rtabmap_demo scan_mapping.launch #启动rtabmap
终端3:$ rosrun robot_sim_demo robot_keyboard_teleop.py #启动键盘控制
```
###### ps:运行结束,虽然rviz中没有显示三维点云地图,但是rtabmap还是订阅了相机的话题,所以最终保存的地图会是2D+3D,占用较大内存,所以谨慎保存每次建的图.
