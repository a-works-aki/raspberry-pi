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
from gpiozero import Button
from time import sleep
from subprocess import call

shutdown_button = Button(5)

while True:
    shutdown_button.wait_for_press()
    print("See you!")
    sleep(2)
    if shutdown_button.is_pressed:
        call("sudo shutdown -h now", shell=True)
        break
