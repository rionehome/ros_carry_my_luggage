import rclpy
from rclpy.node import Node

from module import module_follow
from time import sleep

from rione_msgs.msg import Command, Location, Request

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

        """
        self.senses_publisher2 = self.create_publisher(
            Command,
            'control/arm2',
            10
        )
        """

        self.send_return_signal = self.create_publisher(
            Request,
            "/location/send_goal_location",
            10
        )


    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if "follow" == msg.command:
            if module_follow.follow() == 1:
                self.main_publisher("STOP")
                sleep(5)
                self.publish_regist_location()


    # Publish a result of an action
    def main_publisher(self, command, content=""):

        _trans_message = Command()
        #_trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

    def publish_regist_location(self):
        _location = Location()
        _location.name = "start_position"
        _request = Request()
        _request.locations.append(_location)
        _request.file = "carry_my_luggage"

        self.send_return_signal.publish(_request)

    

def main():
    rclpy.init()
    node = SoundSystem3()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
