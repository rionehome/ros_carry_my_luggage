import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from rione_msgs.msg import Command


class MakePublisher(Node):

    def __init__(self):
        super().__init__('MakePublisher')
        self.make_pub()

    def make_pub(self):
        while 1:
            #topic = input('topic:')
            topic = 'sound_system/command'
            print('topic:', topic)
            test_command = input('Command:')
            test_content = input('Content:')
            # i = input('enter')
            self.senses_publisher = self.create_publisher(
                Command,
                topic,
                10
            )
            self.cerebrum_publisher(test_command, test_content)

    # Publish a result of an action
    def cerebrum_publisher(self, command, content=""):

        _trans_message = Command()
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "debuger"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = MakePublisher()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
