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
		something = actionlib.SimpleActionClient(SERVER, Turtle_positionAction)
		print(something)
		# rospy.sleep(1)
		connected = something.wait_for_server()
		print("hello, I am connected")
		print(connected)
    


# yaml file
if __name__ == '__main__':
	# print("inside main")
	rospy.init_node(NODE)
	rospy.loginfo("inside main")
	n = Turtle_Client()
	rospy.spin()