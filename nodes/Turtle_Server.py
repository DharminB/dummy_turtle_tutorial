#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'something'

import rospy
from actionlib import SimpleActionClient, SimpleActionServer
from geometry_msgs.msg import Twist
from turtle_thing.msg import Turtle_positionAction, Turtle_positionResult

class Something :
	def __init__(self) :
		rospy.init_node(NODE)
		rospy.loginfo('Hello world')
		print("hello world")

if __name__ == '__main__':
	n = Something()
	rospy.spin()
