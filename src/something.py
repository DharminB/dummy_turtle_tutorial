#!/usr/bin/env python

PACKAGE = 'turtle_thing'
NODE = 'something'
from yaml import load
import rospy
file = "/home/dharmin/catkin_ws/src/turtle_thing/config/poses.yaml"

class Something :
	def __init__(self) :
		rospy.init_node(NODE)
		rospy.loginfo('Hello world')
		print("hello world")
		with open(file, "r") as f :
			# print(f.read())
			yaml_file = load(f.read())
			print (yaml_file)
			print(yaml_file["a"]["x"])
		# print(load("""- Hesperiidae"""))

if __name__ == '__main__':
	n = Something()
	# rospy.spin()