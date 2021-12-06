#!/usr/bin/env python
import rospy

from std_msgs.msg import String # Messages used in the node must be imported.

def my_callback(msg):
	rospy.loginfo("received data from warning_topic: %s", msg.data)


rospy.init_node('subscriber_py') #initialzing the node with name "subscriber_py"


rospy.Subscriber("warning_topic", String, my_callback, queue_size=10) 

rospy.loginfo("subscriber node:node3a started and subscribed to warning_topic") #debug statement


rospy.spin() 