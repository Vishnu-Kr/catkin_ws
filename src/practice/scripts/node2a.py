#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from rospy_tutorials.srv import AddTwoIntsResponse
from std_msgs.msg import Int32, String # Messages used in the node must be imported.

d = Int32

print(d)

def my_callback(msg):
    res = AddTwoIntsResponse()
    rospy.loginfo("received data from topic-wall_distance: %d", msg.data)
    
    sum=msg.data
    if sum >= 20:
        print("it is at safe distance")
    elif sum < 20:
        print("Warning.... it may collide")
        pub = rospy.Publisher('warning_topic', String, queue_size=10)
        rospy.loginfo("publisher node:node2a started and publishing data on topic warning_topic")
        rate = rospy.Rate(0.5) # 10hz
        while not rospy.is_shutdown():
            pub.publish("warning hai")
            print("warning hai bhai")
            rate.sleep()
    



        












rospy.init_node('node2a') #initialzing the node with name "subscriber_py"

rospy.Subscriber("wall_distance", Int32, my_callback, queue_size=10) 

rospy.loginfo("subscriber_py node:node2a started and subscribed to wall_distance") #debug statement













rospy.spin()