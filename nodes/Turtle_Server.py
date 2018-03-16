#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'Turtle_Server'

import rospy
#here
# roslib.load_manifest('my_pkg_name')
from actionlib import SimpleActionClient, SimpleActionServer
from geometry_msgs.msg import Twist
from turtle_thing.msg import Turtle_positionAction, Turtle_positionResult

class Turtle_Server :
	def __init__(self) :
		rospy.loginfo("inside __init__")
		self.Server = "/turtle_thing"
		print(self.Server)
		self.result = Turtle_positionResult()
		self.turtle_server = SimpleActionServer(self.Server, Turtle_positionAction, execute_cb = self.execute_cb, auto_start = False)
		self.turtle_server.start()

	def execute_cb(self, goal) :
		rospy.loginfo("inside execute_cb")
		print(goal.x, goal.y, goal.theta)
		self.result.result = True
		# self.turtle_server.set_succeeded(self.result)
		self.turtle_server.set_aborted(self.result)

if __name__ == '__main__':
	rospy.init_node(NODE)	
	n = Turtle_Server()
	rospy.spin()
