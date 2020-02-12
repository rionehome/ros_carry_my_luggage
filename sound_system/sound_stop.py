import rclpy
from rclpy.node import Node

from module import module_follow

from rione_msgs.msg import Command

class SoundSystem3(Node):
    def __init__(self):
        super(SoundSystem3, self).__init__('SoundSystem3')

        self.create_subscription(
            Command, 'sound/stop',
            self.command_callback,
            10
        )

        """
        self.senses_publisher = self.create_publisher(
            Command,
            'control/arm2',
            10
        )
        """


    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "follow" == msg.command:
            module_follow.follow()


    # Publish a result of an action
    def main_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = SoundSystem3()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
