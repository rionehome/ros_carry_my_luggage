import rclpy
from rclpy.node import Node

from module import module_start

from rione_msgs.msg import Command, Location, Request
from std_msgs.msg import Bool

class SoundSystem1(Node):
    def __init__(self):
        super(SoundSystem1, self).__init__('SoundSystem1')

        self.create_subscription(
            Bool,
            'turtlebot2/button0',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            'sound/speak1',
            10
        )

        self.current_position_publisher = self.create_publisher(
            Request,
            "/location/register_current_location",
            10
        )


    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if True == msg.data:
            if module_start.start() == 1:
                self.main_publisher("arm","first")
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

    #
    # Publish to location register to regist current position
    # 
    def publish_regist_location(self):
        _location = Location()
        _location.name = "start_position"
        _request = Request()
        _request.file = "carry_my_luggage"
        _request.locations.append(_location)
        self.current_position_publisher.publish(_request)

def main():
    rclpy.init()
    node = SoundSystem1()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
