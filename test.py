# -*- coding: utf-8 -*-
#!/usr/bin/python
from re import I
from displayTime import displayTime
import smbus
import time
import datetime
import subprocess
import shlex
from gpiozero import Button
from command import command
from writeLcd import writeLcd
from setLcdInit import setLcdInit

# lcdカーソルアドレス
lcd_year = 0x81
lcd_month = 0x84
lcd_day = 0x87
lcd_hour = 0xc1
lcd_minute = 0xc4
lcd_second = 0xc7
lcd_1stline = 0x80
lcd_2ndline = 0xc0

# 入力ボタン設定
set_button = Button(1, hold_time=2)
p_button = Button(8)
m_button = Button(7)


# 時刻取得と変数設定
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
set_flag = 0


def setting_flag():
    global set_flag
    set_flag = 1


def displayDate():
    command(lcd_1stline)
    writeLcd(now.strftime(
        f"{str(year % 100)}/{str(month).zfill(2)}/{str(day).zfill(2)}"))


def diplayTime():
    command(lcd_2ndline)
    writeLcd(now.strftime(
        f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))


def changeYear(x):
    while True:
        command("lcd_" + x)
        if p_button.is_pressed:
            x += 1
            displayDate()

        elif m_button.is_pressed:
            x -= 1
            displayDate()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)


def test():
    global now, year, month, day, hour, minute, second, set_flag
    print(now)
    setLcdInit()

    print(f"{year}/{month}/{day}/{hour}:{minute}:{second}")
    displayDate()
    displayTime()

    changeYear(year)

    while True:
        command(lcd_month)
        if p_button.is_pressed:
            month += 1
            displayDate()

        elif m_button.is_pressed:
            month -= 1
            displayDate()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_day)
        if p_button.is_pressed:
            day += 1
            displayDate()

        elif m_button.is_pressed:
            day -= 1
            displayDate()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_hour)
        if p_button.is_pressed:
            hour += 1
            displayTime()

        elif m_button.is_pressed:
            hour -= 1
            displayTime()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_minute)
        if p_button.is_pressed:
            minute += 1
            displayTime()

        elif m_button.is_pressed:
            minute -= 1
            displayTime()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_second)
        if p_button.is_pressed:
            second += 1
            displayTime()

        elif m_button.is_pressed:
            second -= 1
            displayTime()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    set_time = f"sudo hwclock --set --date='{month}/{day}/{year} {hour}:{minute}:{second}'"
    print(set_time)
    subprocess.call(shlex.split(set_time))
    subprocess.call(shlex.split("sudo hwclock -s"))
    print("final")
