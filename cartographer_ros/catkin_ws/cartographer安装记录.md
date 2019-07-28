## Cartographer安装记录

本次安装参考[官网教程](https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html)和师兄给的[教程](https://blog.csdn.net/rjasd1128hf/article/details/79888305)。我的Ubuntu只安装了ROS，可能是系统环境比较干净所以安装过程中遇到的问题并不多（问题记录和解决方法在下面），不知道有没有参考意义。
### 1.install wstool rosdep ninja

~~~sh
apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build
~~~
### 2.Create cartographer workspace 

~~~sh
mkdir catkin_ws
cd catkin_ws
wstool init src
wstool merge -t src https://raw.githubusercontent.com/googlecartographer/cartographer_ros/master/cartographer_ros.rosinstall
wstool update -t src
~~~

执行 `wstool update -t src` 报出ceres-solver无法获取错误。解决方法：
将catkin_ws/src/.rosinstall.rosinstall文件最后一个git来源网址 `https://ceres-solver.googlesource.com/ceres-solver.git` 改为`https://github.com/ceres-solver/ceres-solver.git`

### 3.Install cartographer_ros’ dependencies 

~~~sh
src/cartographer/scripts/install_proto3.sh
sudo rosdep init
rosdep update
~~~
执行sudo rosdep init报错。因为之前安装ROS是执行过所以可以忽略。以下为官方解释：`The command ‘sudo rosdep init’ will print an error if you have already executed it since installing ROS. This error can be ignored.`

~~~sh
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
~~~

漫长的安装后，正确安装则会出现：

All required rosdeps installed successfully

### 4.Build and install

~~~sh
catkin_make_isolated --install --use-ninja
source install_isolated/setup.bash
~~~

### 5.Download and launch the 2D backpack demo

~~~sh
wget -P ~/Downloads https://storage.googleapis.com/cartographer-public-data/bags/backpack_2d/cartographer_paper_deutsches_museum.bag
roslaunch cartographer_ros demo_backpack_2d.launch bag_filename:=${HOME}/Downloads/cartographer_paper_deutsches_museum.bag
~~~

### 6.Download and launch the 3D backpack demo

~~~sh
wget -P ~/Downloads https://storage.googleapis.com/cartographer-public-data/bags/backpack_3d/with_intensities/b3-2016-04-05-14-14-00.bag
roslaunch cartographer_ros demo_backpack_3d.launch bag_filename:=${HOME}/Downloads/b3-2016-04-05-14-14-00.bag
~~~

因为demo的文件较大（9.1G），所以目前还没有测试这个demo。



