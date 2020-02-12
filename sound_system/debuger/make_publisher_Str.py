import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from std_msgs.msg import String
from std_msgs.msg import Bool

class MakePublisher_str(Node):

    def __init__(self):
        super().__init__('MakePublisher_Str')
        self.make_pub()

    def make_pub(self):
        while 1:
            #topic = input('topic:')
            topic = 'turtlebot/_bottun0'
            print('topic:', topic)
            Command = input('Command:')
            Content = input('Content:')
            if Command == "True":
                self.pub = self.create_publisher(
                    Bool, topic)
                msg = Bool()
                msg.data = True
                self.pub.publish(msg)
            else:
                message = 'Command:' + Command + ',Content:' + Content
                # i = input('enter')
                self.pub = self.create_publisher(
                    String, topic, 10)
                msg = String()
                msg.data = message
                self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = MakePublisher_str()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
