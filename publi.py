import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PubliNode(Node):

    def __init__(self):
        super().__init__('Publisher_Node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter_ = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Project EMA: %d' % self.counter_
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    node = PubliNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == '__main__':
    main()