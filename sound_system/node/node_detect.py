import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

import os
from pocketsphinx import LiveSpeech, get_model_path

from . import module_beep

import datetime
from time import sleep

from rione_msgs.msg import Command


class MakePublisher(Node):

    def __init__(self):
        super().__init__('SoundDetect')

        self.create_subscription(
            Command,
            'sound_system/detect',
            self.command_callback,
            10
        )

        self.senses_publisher = self.create_publisher(
            Command,
            'node/detect',
            10
        )


    # recieve a command {Command, Content}
    def command_callback(self, msg):

        noise_words = []
        file_path = os.path.abspath(__file__)

        # pocketsphinx path
        model_path = get_model_path()

        # Define order path
        follow_dic_path = file_path.replace(
            '.py', 'dictionary/follow_me.dict')
        follow_gram_path = file_path.replace(
            'module/module_follow.py', 'dictionary/follow_me.gram')

        # log file
        result_path = file_path.replace(
            'module/module_follow.py', 'log/folllow-{}.txt').format(str(datetime.datetime.now()))


        # Speak a content
        if 'speak' == msg.command:
            if module_pico.speak(msg.content) == 1:
                self.cerebrum_publisher("speak")

        # Start the test and start follow me
        if 'start' == msg.command:
            if module_start.start() == 1:
                self.sub_publisher("START")

        # grab a bag
        if 'arm' == msg.command:
            content = msg.content
            if content == "first":
                if module_arm.arm(content) == 1:
                    self.cerebrum_publisher("arm_first")
            elif content == "end":
                if module_arm.arm(content) == 1:
                    self.cerebrum_publisher("arm_end")

        # Stop follow me
        if 'follow' == msg.command:
            if str(module_follow.follow()) == "car":
                self.sub_publisher("STOP")

        # Make map
        content = None
        if 'make_map' == msg.command:
            content = msg.content
            if content == "go":
                self.cerebrum_publisher("make_map_go", str(module_make_map.make_map(content)))
            else:
                self.cerebrum_publisher("make_map_else", (module_make_map.make_map()))

    # Publish a result of an action
    def cerebrum_publisher(self, command, content=""):

        _trans_message = Command()
        # _trans_message.flag = flag
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "sound"

        self.senses_publisher.publish(_trans_message)

        # self.destroy_publisher(self.senses_publisher)

        # Publish START or STOP
        def sub_publisher(self, command, content=""):
            _trans_message = Command()
            # _trans_message.flag = flag
            _trans_message.command = command
            _trans_message.content = content
            _trans_message.sender = "sound"

            self.signal_publisher.publish(_trans_message)
            # self.destroy_publisher(self.signal_publisher)

def main():
    rclpy.init()
    node = SoundDetect()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
