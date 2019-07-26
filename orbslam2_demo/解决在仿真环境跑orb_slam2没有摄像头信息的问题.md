# 解决在仿真环境跑orb_slam2的时候没有摄像头信息的问题

### 问题描述
这个问题出现在之前的代码包中，目前可更新codes包，解决该问题。问题大概长这样：

![orb1.png](https://i.loli.net/2018/10/24/5bd0890775d85.png)

### 问题原因
gazebo已经发布了D415摄像头的信息，可是orb没有接受到，因为在原来的代码包中还依然camera,没有换成我们使用的D415，导致没有图像。

### 解决办法
* step1: 在`//home/本机/catkin_ws/src/ORB_SLAM2/Examples/ROS/ORB_SLAM2/src`下找到`ros_rgbd.cc`
* step2:line68和line69用下列代码替换：

    		message_filters::Subscriber<sensor_msgs::Image> rgb_sub(nh, "/camera/rgb/image_raw", 1);
    		message_filters::Subscriber<sensor_msgs::Image> depth_sub(nh, "/camera/depth/image_raw", 1);
    		
 * step3:重新编译，回到ORB_SLAM2/下执行：`./build_ros.sh`
 
 * 重新开始运行即可。效果图如下：
 
 ![orb2.png](https://i.loli.net/2018/10/24/5bd08bbab3fbb.png)
