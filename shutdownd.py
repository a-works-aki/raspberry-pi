# -*- coding: utf-8 -*-
#!/usr/bin/python
from gpiozero import Button
import os

set_button = Button(5, hold_time=2)
shutdown_flag = 0


def shutdown():
    global shutdown_flag
    shutdown_flag = 1


while True:
    set_button.when_held = shutdown
    if shutdown_flag == 1:
        print("shutdown start")
        os.system("sudo shutdown -h now")
    else:
        print("Button is not pressed")
