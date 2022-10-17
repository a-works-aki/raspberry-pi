# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus
import time
import datetime
from gpiozero import LED, Button
from signal import pause
import displayTime

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


def command(code):
    i2c.write_byte_data(i2c_addr, resister_aqm0802, code)
    time.sleep(0.1)


def writeLCD(message):
    mojilist = []
    for moji in message:
        mojilist.append(ord(moji))
    i2c.write_i2c_block_data(i2c_addr, data, mojilist)
    # time.sleep(0.1)


def init_lcd():
    command(0x38)
    command(0x39)
    command(0x14)
    command(0x73)
    command(0x56)
    command(0x6c)
    command(0x38)
    command(clear)
    command(display_On_Cursor_Off)


def display_lcd():
    writeLCD(time.strftime("%y/%m/%d"))
    command(LCD_2ndline)
    writeLCD(time.strftime("%H:%M:%S"))


def display_time():
    writeLCD(time.strftime("%y/%m/%d"))
    command(LCD_2ndline)
    writeLCD(time.strftime("%H:%M:%S"))
