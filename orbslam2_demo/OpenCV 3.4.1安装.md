## OpenCV 3.4.1安装
安装环境：ubuntu18.04
第一步 安装依赖
```
 $ sudo apt-get install build-essential  //[compiler]
$ sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev //[required] 
$ sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev  //[optional] 
```
安装错误提示：
```
errorE: unable to locate libjasper-dev
```
解决办法：
```
sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo apt update
sudo apt install libjasper1 libjasper-dev
```
此步骤通过。
第二步 下载安装包
```
cd ~/<my_working_directory>
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```
第三步 编译及安装
```
cd ~/<my_working_directory>/opencv
mkdir build
cd build
cmake ..     //没加参数，貌似之前安装加参数会一堆报错
make   //别加参数，加了会出错
```
安装错误提示：
```
In file included from /home/pxx/OpenCV/opencv/modules/core/test/test_precomp.hpp:12:0,
                 from /home/pxx/OpenCV/opencv/build/modules/core/opencv_test_core_pch_dephelp.cxx:1:
/home/pxx/OpenCV/opencv/modules/core/include/opencv2/core/private.hpp:66:12: fatal error: Eigen/Core: No such file or directory
 #  include <Eigen/Core>
            ^~~~~~~~~~~~
compilation terminated.
modules/core/CMakeFiles/opencv_test_core_pch_dephelp.dir/build.make:62: recipe for target 'modules/core/CMakeFiles/opencv_test_core_pch_dephelp.dir/opencv_test_core_pch_dephelp.cxx.o' failed
make[2]: *** [modules/core/CMakeFiles/opencv_test_core_pch_dephelp.dir/opencv_test_core_pch_dephelp.cxx.o] Error 1
CMakeFiles/Makefile2:1229: recipe for target 'modules/core/CMakeFiles/opencv_test_core_pch_dephelp.dir/all' failed
make[1]: *** [modules/core/CMakeFiles/opencv_test_core_pch_dephelp.dir/all] Error 2
Makefile:162: recipe for target 'all' failed
make: *** [all] Error 2
```
解决方法：
报错说找不到这个头文件，Eigen只有头文件，没有库文件，我们使用
```
sudo apt-get install libeigen3-dev
```
安装Eigen,在使用的时候，编译器会直接去`/usr/local/include`或者`/usr/include`目录找头文件，但是找到的是eigen3，并没有Eigen和unsupported。所以我们可以建立一个软连接到这两个文件夹。
```
#要先确定你的Eigen安装在/usr/local/include还是/usr/include
cd /usr/local/include
sudo ln -sf eigen3/Eigen Eigen
sudo ln -sf eigen3/unsupported unsupported
```
此步通过。

再执行
```
sudo make install
```
第四步 配置OpenCV
```
sudo gedit  /etc/ld.so.conf.d/opencv.conf
```
打开可能是一个空白文件，写入
```
/usr/local/lib
```
使得上面的配置生效：
```
sudo ldconfig
```
配置bash环境
```
sudo gedit /etc/bash.bashrc
```
写入
```
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
export PKG_CONFIG_PATH
```
再执行使得上面配置生效
```
source /etc/bash.bashrc
sudo updatedb
```
第四步 测试 
利用orbslam2_demo下的test文件测试openCV。
在终端执行
   ```
			$ cd test

   $mkdir build

   $ cd build

			$ cmake ..

			$ make
    ```

			生成DisplayImage,再执行
     ```
     $ cd ..

			   $ ./test zdzn.png
      
    ```
如果显示出zdzn的LOGO，则说明安装成功！
