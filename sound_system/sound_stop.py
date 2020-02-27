import rclpy
from rclpy.node import Node

from module import module_follow
from time import sleep

from rione_msgs.msg import Command

class SoundSystem3(Node):
    def __init__(self):
        super(SoundSystem3, self).__init__('SoundSystem3')

        self.create_subscription(
            Command, 'sound/stop',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            '/signal',
            10
        )

        self.senses_publisher2 = self.create_publisher(
            Command,
            '/control_manipulator',
            10
        )

        self.senses_publisher3 = self.create_publisher(
            Command,
            '/sound/speak2',
            10
        )

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "follow" == msg.command:
            if module_follow.follow() == 1:
                self.main_publisher("STOP")
                self.arm_publisher("OPEN")
                self.sub_publisher("arm", "end")


    # Publish a result of an action
    def main_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

    # Publish a result of an action
    def arm_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher2.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

    # Publish a result of an action
    def sub_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher3.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)


def main():
    rclpy.init()
    node = SoundSystem3()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
