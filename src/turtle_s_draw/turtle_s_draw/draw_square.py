import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class TurtleSquare(Node):
    def __init__(self):
        super().__init__('turtle_square_drawer')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.linear_speed = 2.0
        self.angular_speed = math.pi / 2
        self.side_length = 2.0

    def move_straight(self, distance):
        try:
            msg = Twist()
            msg.linear.x = self.linear_speed
            self.publisher_.publish(msg)
            duration = distance / self.linear_speed
            time.sleep(duration)
            msg.linear.x = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.1)
        except Exception as e:
            pass

    def turn_90(self):
        try:
            msg = Twist()
            msg.angular.z = self.angular_speed
            self.publisher_.publish(msg)
            duration = (math.pi / 2) / self.angular_speed
            time.sleep(duration)
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            time.sleep(0.1)
        except Exception as e:
            pass

    def draw_square(self):
        for i in range(4):
            try:
                self.move_straight(self.side_length)
                self.turn_90()
            except Exception as e:
                break

def main(args=None):
    try:
        rclpy.init(args=args)
        turtle = TurtleSquare()
        time.sleep(1.0)
        turtle.draw_square()
        turtle.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        pass
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
