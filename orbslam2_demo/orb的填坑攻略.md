# 复现orb_slam2在仿真环境中运行的填坑之旅
### 问题1 OpenCV 3.2的安装编译问题
* 首先是安装依赖的关系，有一个文件经常出错，就是：`ippicv_linux_20151201.tgz`下载不下来，导致出错。

**解决办法：**将事先下载好的`ippicv_linux_20151201.tgz`复制到`/home/你的路径名字/opencv-3.2.0/3rdparty/ippicv/downloads/linux-808b791a6eac9ed78d32a7666804320e/`下，（如果里面有文件则删除替换，如果没有直接粘贴即可）。

* 原来的教程缺少了很重要的一步（我的锅，应该是大意没写进去） 

**解决办法：** 增加步骤`$ cmake ..`

* 原来的教程没有OpenCV安装好的实例运行测试

**解决办法：**补充`/test`测试文件夹，上传至orbslam2_demo 。

**PS:**OpenCV的依赖库有很多，要按照教程要求的安装基本是OK的，具体出了缺少库，对应安装即可。

### 问题2  安装Pangolin的问题
* 编译过程出现错误 `CMake Error at CMakeModules/FindGLEW.cmake:51 (MESSAGE):18   Could not find GLEW`

**解决办法：** 安装依赖，增加命令`$ sudo apt-get install libglew-dev`安装上GLEW。

* 运行`make -j`导致系统卡崩溃问题。

**解决办法：** 修改编译命令`$ cmake ..   make sudo make install`即可。具体为啥卡原因未知，应该是自己的硬件问题？

### 问题3 编译orb_slam2的问题

* 出现错误如下：

		`/usr/bin/ld: CMakeFiles/RGBD.dir/src/ros_rgbd.cc.o: undefined reference to symbol ‘_ZN5boost6system15system_categoryEv’ 
		/usr/lib/x86_64-linux-gnu/libboost_system.so: error adding symbols: DSO missing from command line 
		collect2: error: ld returned 1 exit status 
		CMakeFiles/RGBD.dir/build.make:218: recipe for target ‘../RGBD’ failed 
		make[2]: * [../RGBD] Error 1 
		CMakeFiles/Makefile2:67: recipe for target ‘CMakeFiles/RGBD.dir/all’ failed 
		make[1]: * [CMakeFiles/RGBD.dir/all] Error 2 
		make[1]: * 正在等待未完成的任务…. 
		/usr/bin/ld: CMakeFiles/Stereo.dir/src/ros_stereo.cc.o: undefined reference to symbol ‘_ZN5boost6system15system_categoryEv’ 
		/usr/lib/x86_64-linux-gnu/libboost_system.so: error adding symbols: DSO missing from command line 
		collect2: error: ld returned 1 exit status 
		CMakeFiles/Stereo.dir/build.make:218: recipe for target ‘../Stereo’ failed 
		make[2]: * [../Stereo] Error 1 
		CMakeFiles/Makefile2:104: recipe for target ‘CMakeFiles/Stereo.dir/all’ failed 
		make[1]: * [CMakeFiles/Stereo.dir/all] Error 2 
		Makefile:127: recipe for target ‘all’ failed 
		make: * [all] Error 2
		
**解决办法：** 出错原因为：libboost_system.so 与libboost_filesystem.so找不到链接目录 ，在Ubuntu计算机目录下搜索文件（右上角放大镜logo）libboost_system.so 与libboost_filesystem.so，并分别复制到ORB_SLAM2的目录lib下，并将并且将ORBSLAM2/Examples/ROS/ORBSLAM2下的Cmakelists.txt中加入库目录，具体为 
在
		set(LIBS 
		${OpenCV_LIBS} 
		${EIGEN3_LIBS} 
		${Pangolin_LIBRARIES} 
		${PROJECT_SOURCE_DIR}/../../../Thirdparty/DBoW2/lib/libDBoW2.so 
		${PROJECT_SOURCE_DIR}/../../../Thirdparty/g2o/lib/libg2o.so 
		${PROJECT_SOURCE_DIR}/../../../lib/libORB_SLAM2.so 
		之后加入${PROJECT_SOURCE_DIR}/../../../lib/libboost_filesystem.so 
		${PROJECT_SOURCE_DIR}/../../../lib/libboost_system.so 
		问题得以解决
		
* 如果编译紧接着出现新的错误如下：

		MakeFiles/Makefile2:718: recipe for target 'CMakeFiles/Mono.dir/all' failed
		make[1]: *** [CMakeFiles/Mono.dir/all] Error 2
		make[1]: *** Waiting for unfinished jobs....
		make[2]: *** No rule to make target '/opt/ros/kinetic/lib/libopencv_calib3d3.so.3.2.0', needed by '../RGBD'. Stop.
		CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/RGBD.dir/all' failed
		make[1]: *** [CMakeFiles/RGBD.dir/all] Error 2
		make[2]: *** No rule to make target '/opt/ros/kinetic/lib/libopencv_calib3d3.so.3.2.0', needed by '../Stereo'. Stop.
		CMakeFiles/Makefile2:104: recipe for target 'CMakeFiles/Stereo.dir/all' failed
		make[1]: *** [CMakeFiles/Stereo.dir/all] Error 2

**解决办法：** 修改ORB_SLAM2/Examples/ROS/ORB_SLAM2中CMakelists.txt,在set那里添加-lboost_system: 

		set(LIBS
		${OpenCV_LIBS}
		${EIGEN3_LIBS}
		${Pangolin_LIBRARIES}
		${PROJECT_SOURCE_DIR}/../../../Thirdparty/DBoW2/lib/libDBoW2.so
		${PROJECT_SOURCE_DIR}/../../../Thirdparty/g2o/lib/libg2o.so
		${PROJECT_SOURCE_DIR}/../../../lib/libORB_SLAM2.so
		-lboost_system
		)
		
然后在编译，就能够成功了.（这里把刚刚添加的语句用#注释掉了）。
