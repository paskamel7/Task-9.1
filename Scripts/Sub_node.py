#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(data.data)

if __name__ == '__main__':
    rospy.init_node('chat_subscriber', anonymous=True)
    rospy.Subscriber('/chat', String, callback)
    rospy.spin()
