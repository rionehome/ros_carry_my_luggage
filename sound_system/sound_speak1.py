import rclpy
from rclpy.node import Node

from module import module_arm

from rione_msgs.msg import Command

class SoundSystem2(Node):
    def __init__(self):
        super(SoundSystem2, self).__init__('SoundSystem2')

        self.create_subscription(
            Command, 'sound/speak1',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            'control/follow_me/signal',
            10
        )

        self.senses_publisher2 = self.create_publisher(
            Command,
            'sound/stop',
            10
        )

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "arm" == msg.command:
            if module_arm.arm(msg.content) == 1:
                self.main_publisher("START")
                self.sub_publisher("follow")


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
    def sub_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher2.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = SoundSystem2()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
