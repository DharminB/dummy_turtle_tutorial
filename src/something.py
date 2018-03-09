#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'something'

import rospy

class Something :
	def __init__(self) :
		rospy.init_node(NODE)
		rospy.loginfo('Hello world')
		print("hello world")

if __name__ == '__main__':
	n = Something()
	rospy.spin()