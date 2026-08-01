import rclpy
from rclpy.node import Node

class HelloRobot(Node):
    def __init__(self):
        super().__init__("hello_robot")
        self.get_logger().info("Hello, Robot from MrBessy!")

def main(args=None):
    rclpy.init(args=args)

    node = HelloRobot()

    rclpy.shutdown()

    
if __name__ == "__main__":
    main()


