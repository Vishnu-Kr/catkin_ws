#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int32 

rospy.init_node('node1a') # initialzing the node with name "Node 1"



pub = rospy.Publisher('wall_distance', Int32, queue_size=10)

rospy.loginfo("publisher node:node1a started and publishing data on topic wall_distance")

rate = rospy.Rate(0.5) # 10hz

r = Int32() # declaring a message variable of type Int32

 # Initializing count
r.data = random.randint(1,100)
while not rospy.is_shutdown():
    r.data = random.randint(1,100)
    pub.publish(r)
    print(r)
    rate.sleep()


