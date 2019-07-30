## Cartographer安装编译

教程如下：

### 1.install wstool rosdep ninja

~~~sh
apt-get update
sudo apt-get install -y python-wstool python-rosdep ninja-build
~~~
### 2.Create cartographer workspace

由于编译方式的差异,我们另建一个carto的工作空间来单独编译和运行算法.

~~~sh
mkdir  ~/catkin_carto
解压本仓库的src.zip到 ~/catkin_carto/
#安装依赖
rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y
~~~

漫长的安装后，正确安装则会出现：

All required rosdeps installed successfully

### 3.Build and install

~~~sh
catkin_make_isolated --install --use-ninja
source install_isolated/setup.bash
~~~
