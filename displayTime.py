# -*- coding: utf-8 -*-
#!/usr/bin/python
import time
from writeLcd import writeLcd
from command import command

# I2C通信の設定　
LCD_1stline = 0x80
LCD_2ndline = 0x40+0x80


def displayTime():
    command(LCD_1stline)
    writeLcd(time.strftime("%y/%m/%d"))
    command(LCD_2ndline)
    writeLcd(time.strftime("%H:%M:%S"))
