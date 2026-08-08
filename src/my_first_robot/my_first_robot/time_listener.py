import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class TimeListener(Node):
    def __init__(self):
        super().__init__("time_listener") 

        self.subscription = self.create_subscription(Int32, "seconds_elapsed", self.listener_callback, 10 )

    def listener_callback(self, msg):
        self.get_logger().info(f"I heard: {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    time_listener = TimeListener()

    rclpy.spin(time_listener)

    time_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()