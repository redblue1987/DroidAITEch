#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# action_test客户端
# 导入action_test中的文件
import roslib; roslib.load_manifest('action_demo')
# 导入rospy,进行python编写
import rospy
# 导入actionlib.进行action通信
import actionlib
# 导入action_test中的msg,用于Goal、Feedback、Result的调用
import action_demo.msg
# 导入time，控制Xbot运动时间
import time

# 定义linewalk客户端函数，与服务器端建立连接并控制Xbot移动
def linewalk_client():

    # 建立客户端，包含两个参数(服务器名称，action类型)
    client = actionlib.SimpleActionClient('linewalk', action_demo.msg.LinewalkAction)
    # 输出请求服务提示信息
    rospy.loginfo('Waiting for server/...')
    # 请求服务
    client.wait_for_server()
    # 输出建立服务提示信息
    rospy.loginfo('***Connected***')
    # 输出Xbot控制提示
    rospy.loginfo('Xbot: I am going to linewalking')
    # 输出客户端请求进度
    rospy.loginfo('task process: 0%')
    # 定义指令1
    goal = action_demo.msg.LinewalkGoal(order=1)
    # 向服务器发送指令1,控制Xbot向前直线行驶
    client.send_goal(goal)
    # 保持Xbot向前移动5s
    time.sleep(5)
    # 等待服务结果
    client.wait_for_result()
    # 输出Xbot移动提示
    rospy.loginfo('Xbot: All ready moving!!')
    # 更新客户端进度
    rospy.loginfo('task process: 33.3%')

    # 等待下个指令
    time.sleep(2)
    # 输出新的指令提示
    rospy.loginfo('Xbot: New order moving back!!')
    # 定义指令2
    goal = action_demo.msg.LinewalkGoal(order=2)
    # 向服务器发送指令1,控制Xbot向后直线行驶
    client.send_goal(goal)
    # 保持Xbot向后移动5s
    time.sleep(5)
    # 等待服务结果
    client.wait_for_result()
    # 输出Xbot移动提示
    rospy.loginfo('Xbot: Back home!!')
    # 更新客户端进度
    rospy.loginfo('task process: 66.6%')

    # 等待下个指令
    time.sleep(2)
    # 定义指令0
    goal = action_demo.msg.LinewalkGoal(order=0)
    # 向服务器发送指令0,停止Xbot移动
    client.send_goal(goal)
    # 输出Xbot提示
    rospy.loginfo('Xbot: I am tired now!!')
    # 更新客户端进度
    rospy.loginfo('task process: 100%')

    # 等待下个指令
    time.sleep(2)
    # 等待服务结果
    client.wait_for_result()
    # 返回服务结果
    return client.get_result()

# 主函数
if __name__ == '__main__':
    # 初始化客户端节点
    rospy.init_node('linewalk_client')
    # 调用客户端请求
    feedback = linewalk_client()
    # 输出终止信息
    print("Ending processing\....")
