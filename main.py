# -*- coding: utf-8 -*-
#!/usr/bin/python
import datetime
from displayTime import displayTime
from lcdInit import lcdInit
from command import command
from test import test
from test import set_button
from gpiozero import Button
import os

# I2C通信の設定　
data = 0x40
clear = 0x01
home = 0x02
display_On_Cursor_Off = 0x0C
display_On_Cursor_On = 0x0f
LCD_2ndline = 0x40+0x80

# セットモードフラグ
setmode = 0

# shutdown変数
shutdown_button = Button(5, hold_time=2)
shutdown_flag = 0


def set_mode_change():
    global setmode
    setmode = 1


def shutdown():
    global shutdown_flag
    shutdown_flag = 1


def main():
    global setmode

    lcdInit()

    while True:
        set_button.when_held = set_mode_change
        shutdown_button.when_held = shutdown
        if setmode == 0:
            displayTime()
            if shutdown_flag == 1:
                print("shutdown start")
                os.system("sudo shutdown -h now")
        else:
            test()
            setmode = 0
            lcdInit()


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    command(clear)
