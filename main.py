# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus
import time
import datetime
from gpiozero import Button
from signal import pause
import displayTime
import lcdInit

# I2C通信の設定　
i2c = smbus.SMBus(1)  # 1 is bus number
i2c_addr = 0x3e  # lcd
resister_aqm0802 = 0x00
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
    lcdInit()

    while True:
        set_button.when_held = set_mode_change
        if setmode == 0:
            displayTime()
        else:
            print("set mode")


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    displayTime.command(clear)
