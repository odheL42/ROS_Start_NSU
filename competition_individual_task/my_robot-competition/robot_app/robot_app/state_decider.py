import numpy as np
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import rclpy
from rclpy.node import Node



class StateDecider(Node):
    def __init__(self):
        super().__init__('state_decider')
        self.state_sub = self.create_subscription(String, '/state', self.decider_callback, 1)

    def decider_callback(self, msg):
        state = msg.data
        if state == "start":
            self.get_logger().info('starting subprocess run')
        elif state == "follow_lane":
            self.get_logger().info('follow_lane subprocess run')
        elif state == "intersection":
            self.get_logger().info('intersection subprocess run')



def main(args=None):
    rclpy.init(args=args)
    node = StateDecider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()