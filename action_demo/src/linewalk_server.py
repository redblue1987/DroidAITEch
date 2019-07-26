#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# action_test服务器端
# 导入action_test中的文件
import roslib; roslib.load_manifest('action_demo')
# 导入rospy,进行python编写
import rospy
# 导入actionlib进行action通信
import actionlib
# 导入action_test中的msg,用于Goal、Feedback、Result的调用
import action_demo.msg
# Twist用于控制Xbot进行移动
from geometry_msgs.msg import Twist

# 定义LinewalkAction类，建立LinewalkAction服务器端
class LinewalkAction(object):
  # 定义变量_feedback用于查看任务进度,result查看完成的指令个数
  _feedback = action_demo.msg.LinewalkFeedback()
  _result = action_demo.msg.LinewalkResult()
  # 初始化对应变量
  _result.finished = 0
  _feedback.processing = 0

  # 初始化服务器
  def __init__(self,name):
      # 打印提示信息
      rospy.loginfo('Initing!')
      # 获取action名称
      self._action_name = name
      # 设置action服务器，四个参数分别为（action名称、action类型、Callback函数、自启动设置）
      self._as = actionlib.SimpleActionServer(self._action_name, action_demo.msg.LinewalkAction, execute_cb=self.move, auto_start = False)
      # 启动服务器
      self._as.start()
      # 显示提示信息
      rospy.loginfo('Start the server')

  # 定义函数move，实现Xbot直线行走
  def move(self,goal):
      # 状态标识，如果通信失败，则进行修改
      success = True
      # 输出服务器总任务进度
      rospy.loginfo('total finished order: %s' %self._result.finished)
      rospy.loginfo('total process: %.1f%%' %self._feedback.processing)
      # 输出提示信息
      rospy.loginfo('moving!')

      # 如果服务被占用
      if self._as.is_preempt_requested():
          # 输出提示信息
          rospy.loginfo('Too busy!!!')
          # 设置占用状态
          self._as.set_preempted()
          # 停止Xbot移动
          twist = Twist()
          twist.linear.x = 0;
          pub.publish(twist)
          # 修改通信标识
          success = False
      # 如果通信成功
      if success:
          # 输出提示信息，进行指令判断
          rospy.loginfo('Success! Checking order/...')

          # 指令0，停止Xbot运动
          if goal.order==0:
              # 输出提示信息
              rospy.loginfo('Stop!!')
              # 停止Xbot移动
              twist = Twist()
              twist.linear.x = 0;
              pub.publish(twist)
              # 修改服务器状态
              self._feedback.processing += 33.4
              self._result.finished += 1
              # 输出服务器状态
              rospy.loginfo('total finished order: %s' %self._result.finished)
              rospy.loginfo('total process: %.1f%%' %self._feedback.processing)

          # 指令1，使Xbot向前直线行驶
          if goal.order==1:
              # 输出提示信息
              rospy.loginfo('Move!!')
              # 控制Xbot移动
              twist = Twist()
              twist.linear.x = 0.25;
              pub.publish(twist)
              # 修改服务器状态
              self._feedback.processing += 33.3
              self._result.finished += 1
              # 输出服务器状态
              rospy.loginfo('total finished order: %s' %self._result.finished)
              rospy.loginfo('total process: %.1f%%' %self._feedback.processing)

          # 指令2，使Xbot向后直线行驶
          if goal.order==2:
              # 输出提示信息
              rospy.loginfo('Goback!!')
              # 控制Xbot移动
              twist = Twist()
              twist.linear.x = -0.25;
              pub.publish(twist)
              # 修改服务器状态
              self._feedback.processing += 33.3
              self._result.finished += 1
              # 输出服务器状态
              rospy.loginfo('total finished order: %s' %self._result.finished)
              rospy.loginfo('total process: %.1f%%' %self._feedback.processing)

      # 报告错误指令提示
      else:
           rospy.loginfo('Error order!!')

# 主函数
if __name__ == '__main__':
   # 初始化linewalk节点
   rospy.init_node('linewalk')
   # 发布Xbot控制
   pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=5)
   # 建立Linewalk服务器
   server = LinewalkAction(rospy.get_name())
   # 等待关闭服务器
   rospy.spin()
