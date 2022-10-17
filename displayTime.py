# -*- coding: utf-8 -*-
#!/usr/bin/python
import time
import writeLcd as writeLCD
import command

# I2C通信の設定　
LCD_2ndline = 0x40+0x80


def display_time():
    writeLCD(time.strftime("%y/%m/%d"))
    command(LCD_2ndline)
    writeLCD(time.strftime("%H:%M:%S"))
