import time
import rclpy
import sys
from rclpy.node import Node

import numpy as np

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class GoTurtle(Node):
    def __init__(self, x, y, theta):
        super().__init__('move_to_goal')
        self.goal_x = x
        self.goal_y = y
        self.goal_theta = theta
        self.subscription = self.create_subscription(Pose, '/turtle1/pose', self.check_pose_callback, 20)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 20)

    def check_pose_callback(self, msg):
        run = Twist()
        dx = self.goal_x - msg.x
        dy = self.goal_y - msg.y
        toMove_theta = np.arctan2(dy, dx)
        vel = np.sqrt(dx**2 + dy**2)
        #accuracy of real destination coordinates == 0.05 
        if vel < 0.05:
            final_theta = self.goal_theta*np.pi/180
            final_dtheta = final_theta - msg.theta
            run.angular.z = final_dtheta
            run.linear.x = 0.0
            self.publisher_.publish(run)
            self.destroy_node()
            rclpy.shutdown()
        dtheta= toMove_theta - msg.theta
        run.angular.z = 6 * dtheta
        run.linear.x = 1.5*vel
        self.publisher_.publish(run)


def main(args=None):
    rclpy.init(args=args)
    move_to_goal = GoTurtle(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    rclpy.spin(move_to_goal)
    move_to_goal.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()