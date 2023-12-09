import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage


class ImageAnalyzer(Node):
    def __init__(self):
        super().__init__('image_analyzer')
        self.img_sub = self.create_subscription(Image, '/color/image', self.img_callback, 1)
        self.st_pub = self.create_publisher(String, '/state', 1)
        self.br = CvBridge()
        self.started = False
        

    def img_callback(self, msg):
        image = self.cvBridge.imgmsg_to_cv2(msg, "bgr8")
        res = self.analyze(image)
        self.get_logger().info("result of iamge analyzing is", res)

    def analyze(self, image):
        pass







def main(args=None):
    rclpy.init(args=args)
    node = ImageAnalyzer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()




if __name__ == "__main__":
    main()
