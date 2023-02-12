# -*- coding: utf-8 -*-
#!/usr/bin/python
#from gpiozero import Button
#import os
#from command import command
#from writeLcd import writeLcd
#from lcdInit import lcdInit
#from time import sleep
#import subprocess
#import shlex

#shutdown_button = Button(5, hold_time=2)
#shutdown_flag = 0
#lcd_1stline = 0x80
#clear = 0x01


# def shutdown():
#global shutdown_flag
#shutdown_flag = 1


# def displayEnd():
# command(lcd_1stline)
#writeLcd("See You!")


# def shutdown_work():
# while True:
#shutdown_button.when_held = shutdown
# if shutdown_flag == 1:
# lcdInit()
# displayEnd()
# sleep(1)
#print("shutdown start")
##os.system("sudo shutdown -h now")
# else:
#print("Button is not pressed")
# sleep(1)


# try:
# shutdown_work()
# finally:
# command(clear)

#from gpiozero import Button
#from signal import pause
#from subprocess import call


# def shutdown():
#call("sudo shutdown -h now", shell=True)


#button = Button(5)
#button.when_pressed = shutdown

# pause()

import smbus
import time

# I2C bus number
bus = smbus.SMBus(1)

# AQM0802 address
address = 0x3e

# AQM0802 commands
command_list = [0x38, 0x39, 0x14, 0x70, 0x56, 0x6c]

# AQM0802 initialize


def init_aqm0802():
    for command in command_list:
        bus.write_byte(address, command)
    bus.write_byte(address, 0x38)
    bus.write_byte(address, 0x0c)
    bus.write_byte(address, 0x01)

# Write message to AQM0802


def write_aqm0802(message):
    message = message.ljust(16, " ")
    for i in range(16):
        bus.write_byte(address, 0x80 + i)
        bus.write_byte(address, ord(message[i]))


# AQM0802に"See you!"と表示
write_aqm0802("See you!")

# AQM0802の初期化
init_aqm0802()
