import rclpy
from rclpy.node import Node

from module import module_start

from rione_msgs.msg import Command, Location
from rione_msgs.srv import RequestLocation
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

        self.cli = self.create_client(
            RequestLocation,
            '/location_register'
        )

        self.req = RequestLocation.Request()
        self.location = Location()

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        # Start the test and start follow me
        if True == msg.data:
            if module_start.start() == 1:
                self.main_publisher("arm","first")
                self.send_start_position()


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
    def send_start_position(self):
        self.req.command = "REGIST"
        self.req.file = "carry_my_luggage"
        self.location.name = "start_position"
        self.req.locations.append(self.location)
        self.future = self.cli.call_async(self.req)

def main():
    rclpy.init()
    node = SoundSystem1()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
