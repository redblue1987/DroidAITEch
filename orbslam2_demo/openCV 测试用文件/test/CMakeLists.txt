cmake_minimum_required(VERSION 3.14)
project(test)

set(CMAKE_CXX_STANDARD 11)

find_package(OpenCV REQUIRED)


add_executable(test main.cpp)


target_link_libraries( test ${OpenCV_LIBS} )