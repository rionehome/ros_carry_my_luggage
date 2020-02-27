import rclpy
from rclpy.node import Node

from module import module_arm
from time import sleep

from rione_msgs.msg import Command, Location
from rione_msgs.srv import RequestLocation


class SoundSystem4(Node):
    def __init__(self):
        super(SoundSystem4, self).__init__('SoundSystem4')

        self.create_subscription(
            Command, 'sound/speak2',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            '/control_manipulator',
            10
        )

        self.cli = self.create_client(
            RequestLocation,
            '/location_register'
        )

        self.req = RequestLocation.Request()
        self.location = Location()

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "arm" == msg.command:
            if module_arm.arm(msg.content) == 1:
                self.arm_publisher("CLOSE")
                self.publish_regist_location()
                self.send_goal_position()

    # Publish a result of an action
    def arm_publisher(self, command, content=""):

        _trans_message = Command()
        # _trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

    #
    # Publish to location register to regist current position
    #
    def send_goal_position(self):
        self.req.command = "SEND_GOAL"
        self.req.file = "carry_my_luggage"
        self.location.name = "start_position"
        self.req.locations.append(self.location)
        self.future = self.cli.call_async(self.req)


def main():
    rclpy.init()
    node = SoundSystem4()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
