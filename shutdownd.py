# -*- coding: utf-8 -*-
#!/usr/bin/python
from gpiozero import Button
import os
from command import command
from writeLcd import writeLcd
from lcdInit import lcdInit
from time import sleep

shutdown_button = Button(5, hold_time=2)
shutdown_flag = 0
lcd_1stline = 0x80


def shutdown():
    global shutdown_flag
    shutdown_flag = 1


def displayEnd():
    command(lcd_1stline)
    writeLcd("See You!")


while True:
    shutdown_button.when_held = shutdown
    if shutdown_flag == 1:
        lcdInit()
        displayEnd()
        sleep(1)
        print("shutdown start")
        #os.system("sudo shutdown -h now")
    else:
        print("Button is not pressed")
        sleep(1)
