import rclpy
from rclpy.node import Node

class HelloRobot(Node):
    def __init__(self):
        super().__init__("hello_robot")
        self.seconds_passed_since_init = 0 
        self.get_logger().info("Hello, Robot from MrBessy!")

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.seconds_passed_since_init += 1
        self.get_logger().info(f"{self.seconds_passed_since_init} seconds have passed since initializing")

def main(args=None):
    rclpy.init(args=args)

    node = HelloRobot()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

    
if __name__ == "__main__":
    main()


