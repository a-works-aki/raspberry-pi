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


# I2C通信の設定　
data = 0x40
clear = 0x01
home = 0x02
display_On_Cursor_Off = 0x0C
display_On_Cursor_On = 0x0f
LCD_2ndline = 0x40+0x80

# ボタン設定
set_button = Button(1, hold_time=2)
p_button = Button(8)
m_button = Button(7)

# セットモードフラグ
setmode = 0


def set_mode_change():
    global setmode
    setmode = 1


def main():
    global setmode
    lcdInit()

    while True:
        set_button.when_held = set_mode_change
        if setmode == 0:
            displayTime()
        else:
            test()
            setmode = 0


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    command(clear)
