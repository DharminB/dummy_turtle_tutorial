#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'Turtle_Client'

import rospy
from yaml import load
from actionlib import SimpleActionClient, SimpleActionServer
from geometry_msgs.msg import Twist
from turtle_thing.msg import Turtle_positionGoal, Turtle_positionAction
file = "/home/dharmin/catkin_ws/src/turtle_thing/config/poses.yaml"


class Turtle_Client :
	def __init__(self) :
		rospy.loginfo("hello there")
		# print("inside __init__")
		SERVER = "/turtle_thing"
		self.something = SimpleActionClient(SERVER, Turtle_positionAction)
		print(self.something)
		# rospy.sleep(1)
		connected = self.something.wait_for_server()
		print("hello, I am connected")
		print(connected)
		self.lock = False
		with open(file, "r") as f :
			# print(f.read())
			self.yaml_file = load(f.read())
			print (self.yaml_file)
			# print(yaml_file["a"]["x"])
		self.ask_user()

	def ask_user(self) :
		while True :
			# print("inside while")
			if self.lock :
				continue
			# x =  int(input("Enter x : "))
			# y =  int(input("Enter y : "))
			# theta =  int(input("Enter theta : "))
			char = raw_input("enter a, b, c or d : ")
			print(char)
			x, y, theta = self.yaml_file[char]["x"], self.yaml_file[char]["y"], self.yaml_file[char]["theta"]
			print(x, y, theta)
			# garbage = input("press 0")
			# x, y, theta = 7,7,0
			msg = Turtle_positionGoal()
			msg.x = x
			msg.y = y
			msg.theta = theta
			self.something.send_goal(msg, done_cb=self.done_cb)
			self.lock = True

	def done_cb(self, status, result):
		rospy.loginfo("inside done_cb")
		print(status)
		print(result)
		self.lock = False
    


# yaml file
if __name__ == '__main__':
	# print("inside main")
	rospy.init_node(NODE)
	rospy.loginfo("inside main")
	n = Turtle_Client()
	rospy.spin()