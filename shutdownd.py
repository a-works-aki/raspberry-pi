#!/usr/bin/python
# coding:utf-8
import time
import RPi.GPIO as GPIO
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(29, GPIO.FALLING)

    while True:
        sw_status = GPIO.input(27)
        if sw_status == 0:
            os.system("sudo shutdown -h now")
            print("shutdown start")
            break
