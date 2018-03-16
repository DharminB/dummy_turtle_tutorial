#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'Turtle_Client'

import rospy
import actionlib
# from actionlib import SimpleActionClient, SimpleActionServer
from geometry_msgs.msg import Twist
from turtle_thing.msg import Turtle_positionGoal, Turtle_positionAction

class Turtle_Client :
	def __init__(self) :
		rospy.loginfo("hello there")
		# print("inside __init__")
		SERVER = "/turtle_thing"
		self.something = actionlib.SimpleActionClient(SERVER, Turtle_positionAction)
		print(self.something)
		# rospy.sleep(1)
		connected = self.something.wait_for_server()
		print("hello, I am connected")
		print(connected)
		self.ask_user()

	def ask_user(self) :
		while True :
			# print("inside while")
			# x =  int(input("Enter x"))
			# y =  int(input("Enter y"))
			# theta =  int(input("Enter theta"))
			garbage = input("press 0")
			x, y, theta = 5,5,5
			msg = Turtle_positionGoal()
			msg.x = x
			msg.y = y
			msg.theta = theta
			self.something.send_goal(msg, done_cb=self.done_cb)

	def done_cb(self, status, result):
		rospy.loginfo("inside done_cb")
		print(status)
		print(result)
    


# yaml file
if __name__ == '__main__':
	# print("inside main")
	rospy.init_node(NODE)
	rospy.loginfo("inside main")
	n = Turtle_Client()
	rospy.spin()