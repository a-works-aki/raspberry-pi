# -*- coding: utf-8 -*-
#!/usr/bin/python
from xml.dom import pulldom
import smbus
import time
import datetime
from gpiozero import Button
from signal import pause
from displayTime import displayTime
from lcdInit import lcdInit
from command import command
from test import test
from test import set_button

# I2C通信の設定　
data = 0x40
clear = 0x01
home = 0x02
display_On_Cursor_Off = 0x0C
display_On_Cursor_On = 0x0f
LCD_2ndline = 0x40+0x80

# セットモードフラグ
setmode = 0


def main():
    global setmode
    lcdInit()

    while True:
        set_button.when_held = setmode = 1
        if setmode == 0:
            displayTime()
        else:
            test()
            setmode = 0
            lcdInit()


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    command(clear)
