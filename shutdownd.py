# -*- coding: utf-8 -*-
#!/usr/bin/python
from gpiozero import Button
import os
from command import command
from writeLcd import writeLcd
from lcdInit import lcdInit
from time import sleep
import subprocess
import shlex

shutdown_button = Button(5, hold_time=2)
shutdown_flag = 0
lcd_1stline = 0x80
clear = 0x01


def shutdown():
    global shutdown_flag
    shutdown_flag = 1


def displayEnd():
    command(lcd_1stline)
    writeLcd("See You!")


def shutdown_work():
    while True:
        lcdInit()
        displayEnd()
        sleep(1)
        shutdown_button.when_held = shutdown
        if shutdown_flag == 1:
            print("shutdown start")
            #os.system("sudo shutdown -h now")
        else:
            print("Button is not pressed")
            sleep(1)


try:
    shutdown_work()
finally:
    command(clear)
