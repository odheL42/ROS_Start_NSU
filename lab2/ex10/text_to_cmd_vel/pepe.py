import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class PubliSub(Node):

    def __init__(self):
        super().__init__('publisub_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(String, 'cmd_text', self.timer_callback, 10)

    def timer_callback(self, msg_in):
        pepe = msg_in.data
        #”turn_right”, ”turn_left”, ”move_forward”, ”move_backward”.
        msg = Twist()
        if (pepe=='turn_right'):
            msg.angular.z = -1.5
        elif (pepe=='turn_left'):
            msg.angular.z = 1.5
        elif (pepe == 'move_forward'):
            msg.linear.x = 1.0
        elif (pepe == 'move_backward'):
            msg.linear.x = -1.0
        self.publisher_.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)

    ps = PubliSub()

    rclpy.spin(ps)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ps.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()