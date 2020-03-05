#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import subprocess

# Define path
file_path = os.path.abspath(__file__)

import rclpy
from rclpy.node import Node

from rione_msgs.msg import Command

class SoundUI(Node):
    def __init__(self):
        super(SoundUI, self).__init__('SoundUI')

        self.create_subscription(
            Command, 'test/ui',
            self.command_callback,
            10
        )

        self.process = None

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        if self.process != None:
            self.process.kill()
        if "start" == msg.command:
            ui_path = file_path.replace(
                'install/sound_system/lib/python3.6/site-packages/test_ui.py',
                'sound_system/module/start_ui.py')
            self.process = subprocess.Popen(['python3', ui_path])
        elif "stop" == msg.command:
            ui_path = file_path.replace(
                'install/sound_system/lib/python3.6/site-packages/test_ui.py',
                'sound_system/module/stop_ui.py')
            self.process = subprocess.Popen(['python3', ui_path])


def main():
    rclpy.init()
    node = SoundUI()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
