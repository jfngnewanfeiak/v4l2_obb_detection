#! /usr/bin/env python3
from ultralytics import YOLO
import rclpy.logging
from sensor_msgs.msg import Image
from rclpy.node import Node
import rclpy
from cv_bridge import CvBridge

class v4l2Subscriber(Node):
    def __init__(self):
        super().__init__('v4l2Subscriber')
        self.bridge = CvBridge()
        self.model = YOLO("yolo11n-obb.pt")  # load an official model

        self.subscription = self.create_subscription(
            msg_type=Image,
            topic="image_raw",
            callback=self.callback,
            qos_profile=10
        )

        self.pub = self.create_publisher(
            msg_type=Image,
            topic="result_data",
            qos_profile=10
        )
    
    def callback(self,msg):
        cv_image = self.bridge.imgmsg_to_cv2(img_msg=msg,desired_encoding="rgb8")
        result = self.model.predict(cv_image)[0].cpu()
        result_ros_image = self.bridge.cv2_to_imgmsg(result.plot(),"rgb8")
        self.pub.publish(result_ros_image)
    
def main():
    rclpy.init()
    sub = v4l2Subscriber()
    rclpy.spin(node=sub)


if __name__ == "__main__":
    main()
    