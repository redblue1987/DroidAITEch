#!/bin/bash
##################
#
#部署cartographer
#
##################
sudo apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build
mkdir ~/catkin_cartographer
cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/googlecartographer/cartographer_ros/master/cartographer_ros.rosinstall
sed -i 's@https://ceres-solver.googlesource.com/ceres-solver.git@https://github.com/ceres-solver/ceres-solver.git@' ~/catkin_cartographer/src/.rosinstall
wstool update -t src
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
catkin_make_isolated --install --use-ninja
cd ~/catkin_cartographer//src/cartographer_ros/cartographer_ros/launch
cp demo_revo_lds.launch cartographer_demo.launch
sed -i 's@remap from="scan" to="horizontal_laser_2d"@remap from="scan" to="scan"@' ~/catkin_cartographer/src/cartographer_ros/cartographer_ros/launch/cartographer_demo.launch
sed -i 's@tracking_frame = "horizontal_laser_link"@tracking_frame = "base_link"@' ~/catkin_cartographer/src/cartographer_ros/cartographer_ros/configuration_files/revo_lds.lua
sed -i 's@published_frame = "horizontal_laser_link"@published_frame = "base_link"@' ~/catkin_cartographer/src/cartographer_ros/cartographer_ros/configuration_files/revo_lds.lua
##################
#
#先启动Xbot再启动cartographer
#
##################
read -p "自行启动Xobt仿真平台并按y/Y继续" answer
	if [ $answer = "y" -o $answer = "Y" ] ; then 
		cd ~/catkin_cartographer
		source install_isolated/setup.bash
		roslaunch cartographer_ros cartographer_demo.launch
	fi



