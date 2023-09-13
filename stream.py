#!/usr/bin/env python 
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher(object):
    def __init__(self):
        rospy.loginfo('[STARTING NODE]====>>>>>>>>')
        self.publisher_ = rospy.Publisher('video_frames', Image, queue_size=10)
        self.loop_rate = rospy.Rate(1)
        self.cap = cv2.VideoCapture(0)
        self.br = CvBridge()

    def start(self):
        rospy.loginfo('[GETTING IMAGE]=====>>>>>>>')
        ret, frame = self.cap.read()
        while not rospy.is_shutdown():
            if ret:
                rospy.loginfo('[PUBLISHING iMAGE]=====>>>>>>>>>>>>>>>>')
                self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
                self.loop_rate.sleep()


if __name__ == '__main__':
    rospy.init_node("camera_node", anonymous=True)
    image_publisher = ImagePublisher()
    image_publisher.start()
    rospy.signal_shutdown("Exited")
