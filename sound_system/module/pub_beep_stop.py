#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import subprocess
from time import sleep

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from rione_msgs.msg import Command


class UIcontroler2(Node):

    def __init__(self):
        super().__init__('UIcontroler2')
        self.make_pub()

    def make_pub(self):
            self.senses_publisher = self.create_publisher(
                Command,
                'test/ui',
                10
            )
            sleep(0.5)
            self.cerebrum_publisher("stop")

    # Publish a result of an action
    def cerebrum_publisher(self, command, content=""):

        _trans_message = Command()
        _trans_message.command = command
        _trans_message.content = content
        _trans_message.sender = "UIcontroler2"

        self.senses_publisher.publish(_trans_message)
        # self.destroy_publisher(self.senses_publisher)

def main():
    rclpy.init()
    node = UIcontroler2()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

