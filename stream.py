#!/usr/bin/env python 
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher(object):
    def __init__(self):
        self.publisher_ = rospy.Publisher('video_frames',Image,10)
        self.loop_rate = rospy.Rate(1)
        self.cap = cv2.VideoCapture(0)
        self.br = CvBridge()

    def start(self):
        ret, frame = self.cap.read()
        while not rospy.is_shutdown():
            if ret == True:
                rospy.loginfo('publishing image')
                # br = CvBridge()
                self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
                self.loop_rate.sleep()


def main(args=None):
    rospy.init_node("imagetimer111", anonymous=True)
    image_publisher = ImagePublisher()
    image_publisher.start()
    rospy.shutdown()


if __name__ == '__main__':
    main()

