#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PubliSubsNode(Node):
    def __init__(self):
          super().__init__("Publisher_and_Subscriber_Node")
          self.counter_ = 0
          self.publicador_ = self.create_publisher(String, 'topic', 10)
          self.recebedor_ = self.create_subscription(String, 'topic', self.listener_callback, 10)
          timer_period = 1.0
          self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
         ownmsg = String()
         ownmsg.data = 'Project EMA: %d'  % self.counter_
         self.publicador_.publish(ownmsg)
         self.get_logger().info('Publishing: "%s" ' %ownmsg.data)
         self.counter_ += 1
    
    def listener_callback(self, ownmsg):
         self.get_logger().info('I heard: "%s" ' %ownmsg.data)

def main (args=None):
    rclpy.init(args=args)
    node = PubliSubsNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == '__main__':
    main()
