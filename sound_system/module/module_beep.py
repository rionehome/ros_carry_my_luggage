#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
import subprocess

# Define path
file_path = os.path.abspath(__file__)
process = False
def beep(when):
    ###############
    #
    # use this module to make beep sound
    #
    # param >> when >> start or stop
    #
    # return >> None
    #
    ###############
    beep_wave = file_path.replace(
        'module/module_beep.py', 'beep/{}.wav').format(when)
    ui_path = file_path.replace(
        'module_beep.py', 'pub_beep_{}.py').format(when)

    # uiのコードをバックグラウンド再生
    subprocess.Popen(['python3', ui_path])
    # ビープ音
    subprocess.call('aplay -q --quiet {}'.format(beep_wave), shell=True)




if __name__ == '__main__':
    beep("start")

