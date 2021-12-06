#!/usr/bin/env python

import rospy
import random
from std_msgs.msg import Int32 

rospy.init_node('node1') # initialzing the node with name "Node1"


pub = rospy.Publisher('wall_distance', Int32, queue_size=10)

rospy.loginfo("Publisher node: node1 started and publishing distance b/w wall & robot on topic wall_distance\n")

rate = rospy.Rate(0.5) # 

r = Int32() # declaring a message variable of type Int32

r.data = random.randint(1,100)

while not rospy.is_shutdown():
    r.data = random.randint(1,100)
    pub.publish(r)
   
    rate.sleep()


