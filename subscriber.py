import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import math
from std_msgs.msg import Float32

class DistanceFromOrigin(Node):
    def __init__(self):
        super().__init__('distance_from_origin')
        self.pose_subscriber = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.publisher = self.create_publisher(Float32 , '/turtle1/distance_from_origin', 10)

    def pose_callback(self, msg):
        x = msg.x
        y = msg.y
        distance = math.sqrt(x**2 + y**2)
        distance_msg = Float32()
        distance_msg.data = distance
        self.publisher.publish(distance_msg)


def main(args=None):
    rclpy.init(args=args)

    node=DistanceFromOrigin()
    rclpy.spin(node)
    rclpy.shutdown()

        