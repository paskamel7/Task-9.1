#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    pub = rospy.Publisher('/chat', String, queue_size=10)
    rospy.init_node('chat_publisher', anonymous=True)
    rate = rospy.Rate(1)  
    while not rospy.is_shutdown():
        message = "HI This is Team MIA"
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()


