# -*- coding: utf-8 -*-
#!/usr/bin/python
import datetime
import displayTime
from gpiozero import Button

clear = 0x01

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
    displayTime.init_lcd()

    while True:
        set_button.when_held = set_mode_change
        if setmode == 0:
            displayTime.display_time()
        else:
            print("set mode")


try:
    print("start;"+str(datetime.datetime.now()))
    main()
finally:
    displayTime.command(clear)
