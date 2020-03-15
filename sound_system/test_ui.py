#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import subprocess
import tkinter as tk
import time
import math

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

        self.timer = self.create_timer(0.01, self.render_callback)
        # ウィンドウを作る
        self.root = tk.Tk()
        self.root.update_idletasks()
        self.win_width = self.root.winfo_screenwidth()
        self.win_height = self.root.winfo_screenheight()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        # geometry("(windowの横)✕(windowの縦)+(x方向へ平行移動)+(y方向へ平行移動)")
        self.root.geometry(str(self.win_width) + "x" + str(self.win_height)
                           + "+" + str(int(self.screen_width/2 - self.win_width/2))
                           + "+" + str(int(self.screen_height/2 - self.win_height/2)))

        # Canvasを作る
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(),
                                height=self.root.winfo_screenheight(), bg="white")
        self.canvas.place(x=0, y=0)

        # 変数
        self.radius_circle = 40
        self.multiple = 4
        self.radius_area = self.multiple*100
        self.x = self.win_width/2
        self.y = self.win_height/2
        self.i = 0

        tk.Button(self.root, text="Quit", command=self.root.destroy).pack()
        # Label部品を作る
        self.label = tk.Label(self.root, text="・・・認識中・・・", bg="white", font=("", 40))
        self.label.place(x=self.root.winfo_screenwidth()/2 - 300, y=self.root.winfo_screenheight()/2)
        self.circle = self.canvas.create_oval(self.x - self.radius_circle - self.radius_area,
                                              self.y - self.radius_circle,
                                              self.x + self.radius_circle - self.radius_area,
                                              self.y + self.radius_circle,
                                              fill="blue", width=0)  # 円
        #print(dir(self.circle), flush=True)


    def render_callback(self):
        try:
            self.canvas.coords(self.circle, self.x - self.radius_circle - self.radius_area,
                              self.y - self.radius_circle,
                              self.x + self.radius_circle - self.radius_area,
                              self.y + self.radius_circle,)
        except:
            pass
        #print("OK", flush=True)
        self.i += 0.01
        self.x = self.x + self.multiple*math.sin(self.i)
        self.y = self.y + self.multiple*math.cos(self.i)
        self.root.update()  # ウインド画面を更新

    # recieve a command {Command, Content}
    def command_callback(self, msg):

        if "start" == msg.command:
            self.canvas.itemconfig(self.circle, fill="blue")
            self.label.config(text="・・・認識中・・・")
            # Buttonを作る

        elif "stop" == msg.command:
            self.canvas.itemconfig(self.circle, fill = "white")
            self.label.config(text="・・・認識停止・・・")


def main():
    rclpy.init()
    node = SoundUI()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
