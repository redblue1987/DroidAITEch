## Cartographer安装记录

catkin_ws文件夹是部署Cartographer后的代码包。因为每个机器需要安装依赖，所以不能直接运行。安装教程如下：
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




