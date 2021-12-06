#!/usr/bin/env python
import rospy
#from geometry_msgs.msg import Twist
#from rospy_tutorials.srv import AddTwoIntsResponse
from std_msgs.msg import Int32, String # Messages used in the node must be imported.





def my_callback(msg):
   # res = AddTwoIntsResponse()
    rospy.loginfo("received distance from topic-wall_distance: %d", msg.data)
    
    sum=msg.data
    if sum >= 20:
        print("Robot is moving and is far from obstacle\n\n")

    elif sum < 20:
        print("robot is stopped\n")
        pub = rospy.Publisher('warning_topic', String, queue_size=10)
        rospy.loginfo("publisher part of node2 started and publishing warning on topic warning_topic")
        rate = rospy.Rate(0.5) # 10hz

        while not rospy.is_shutdown():
            pub.publish("Warning: the robot is near the wall\n\n")            
            rate.sleep()
    




rospy.init_node('node2') #initialzing the node 2

rospy.Subscriber("wall_distance", Int32, my_callback, queue_size=10) 

rospy.loginfo("node2a started and subscribed to wall_distance\n") #debug statement


rospy.spin()