# -*- coding: utf-8 -*-
#!/usr/bin/python

# ------------------------------------------------
#  概　要：文字列の送信
#  引  数：str     送信したい文字列
#  戻り値：0   正常
#          -1  異常
# ------------------------------------------------
import datetime
from displayTime import displayTime
from lcdInit import lcdInit
from command import command
from test import test
from test import set_button
from test import lcdLed
from gpiozero import LED, Button
from command import command
from writeLcd import writeLcd
from time import sleep
from subprocess import call

# I2C通信の設定　
data = 0x40
clear = 0x01
home = 0x02
display_On_Cursor_Off = 0x0C
display_On_Cursor_On = 0x0f
lcd_1stline = 0x80
LCD_2ndline = 0x40+0x80
shutdown_button = Button(5, hold_time=2)

# セットモードフラグ
setmode = 0


def set_mode_change():
    global setmode
    setmode = 1


def displayStart():
    command(lcd_1stline)
    writeLcd("START")


def shutdown():
    global shutdown_flag
    shutdown_flag = 1


def main():
    global setmode
    lcdLed.on()
    lcdInit()
    displayStart()
    sleep(1)
    lcdLed.off()
    lcdInit()

    while True:
        set_button.when_held = set_mode_change
        shutdown_button.when_held = shutdown
        if setmode == 0:
            displayTime()
            if shutdown_flag == 1:
                print("See you!")
                call("sudo shutdown -h now", shell=True)
                break
        else:
            test()
            setmode = 0
            lcdInit()


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    command(clear)
