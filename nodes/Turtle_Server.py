#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'Turtle_Server'

import rospy
from math import atan2
# roslib.load_manifest('my_pkg_name')
from actionlib import SimpleActionClient, SimpleActionServer
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtle_thing.msg import Turtle_positionAction, Turtle_positionResult

class Turtle_Server :
	def __init__(self) :
		rospy.loginfo("inside __init__")
		self.Server = "/turtle_thing"
		self.threshold = 0.1
		self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
		self.vel_msg = Twist()
		self.turtle_pose = Pose()
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
		self.result = Turtle_positionResult()
		self.turtle_server = SimpleActionServer(self.Server, Turtle_positionAction, execute_cb = self.execute_cb, auto_start = False)
		self.turtle_server.start()

	def execute_cb(self, goal) :
		rospy.loginfo("inside execute_cb")
		goal_x, goal_y, goal_theta = goal.x, goal.y, goal.theta
		print(goal_x, goal_y, goal_theta)
		
		x, y = self.turtle_pose.x, self.turtle_pose.y
		desired_theta = atan2(goal_y - y, goal_x - x)
		print("desired_theta", desired_theta)
		# nothing = input("press 0 (before turning):")

		# turn till facing the goal
		while not self.reached_angle(desired_theta) :
			# print(desired_theta - self.turtle_pose.theta)
			self.vel_msg.angular.z = (desired_theta - self.turtle_pose.theta)/2
			self.velocity_publisher.publish(self.vel_msg)
		# stop turning
		self.reset_vel()

		# nothing = input("press 0 (before moving):")

		# move forward till at goal
		while not self.reached_goal(goal_x, goal_y) :
			speed_x = self.decide_velocity(goal_x, goal_y)
			# print("speed", speed_x)
			self.vel_msg.linear.x = speed_x
			# self.vel_msg.linear.y = speed_y
			self.velocity_publisher.publish(self.vel_msg)
		# stop moving
		self.reset_vel()
		
		# turn till facing the goal theta
		while not self.reached_angle(goal_theta) :
			# print(goal_theta - self.turtle_pose.theta)
			self.vel_msg.angular.z = (goal_theta - self.turtle_pose.theta)/2
			self.velocity_publisher.publish(self.vel_msg)
		# stop turning
		self.reset_vel()

		# return results
		self.result.result = True
		# self.turtle_server.set_succeeded(self.result)
		self.turtle_server.set_aborted(self.result)
		

	def reset_vel(self) :
		self.vel_msg.linear.x = 0
		self.vel_msg.linear.y = 0
		self.vel_msg.angular.z = 0
		self.velocity_publisher.publish(self.vel_msg)
		

	def decide_velocity(self, goal_x, goal_y) :
		rospy.sleep(0.2)
		factor = 2
		x, y, theta = self.turtle_pose.x, self.turtle_pose.y, self.turtle_pose.theta
		# print("pose",x, y, theta)
		speed_x = ((((goal_x - x)**2) + ((goal_y - y)**2))**0.5) / factor
		# speed_y = (goal_y - y) / factor
		# speed_z = (goal_theta - theta) / (factor*2)
		# print("speed", speed_x)
		return speed_x


	def reached_goal(self, goal_x, goal_y) :
		x, y = self.turtle_pose.x, self.turtle_pose.y
		# print("diff", abs(goal_x - x), abs(goal_y - y))
		answer = ((((goal_x - x)**2) + ((goal_y - y)**2))**0.5) < self.threshold
		return answer

	def reached_angle(self, goal_theta) :
		theta = self.turtle_pose.theta
		return abs(goal_theta - theta) < 0.01




	def callback(self, data) :
		self.turtle_pose = data


if __name__ == '__main__':
	rospy.init_node(NODE)	
	n = Turtle_Server()
	rospy.spin()
