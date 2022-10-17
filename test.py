# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus
import time
import datetime
from gpiozero import Button
import subprocess
import shlex
from command import command
from writeLcd import writeLcd

# I2C通信の設定　
i2c = smbus.SMBus(1)  # 1 is bus number
i2c_addr = 0x3e  # lcd
resister_aqm0802 = 0x00
data = 0x40
clear = 0x01
home = 0x02
display_On_Cursor_Off = 0x0C
display_On_Cursor_On = 0x0f
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


def init():
    command(0x38)
    command(0x39)
    command(0x14)
    command(0x73)
    command(0x56)
    command(0x6c)
    command(0x38)
    command(clear)
    command(display_On_Cursor_On)


def setting_flag():
    global set_flag
    set_flag = 1


def test():
    global now, year, month, day, hour, minute, second, set_flag
    print(now)

    print(f"{year}/{month}/{day}/{hour}:{minute}:{second}")
    writeLcd(now.strftime(
        f"{str(year % 100)}/{str(month).zfill(2)}/{str(day).zfill(2)}"))
    command(lcd_2ndline)
    writeLcd(now.strftime(
        f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

    while True:
        command(lcd_year)
        if p_button.is_pressed:
            year += 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif m_button.is_pressed:
            year -= 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_month)
        if p_button.is_pressed:
            month += 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif m_button.is_pressed:
            month -= 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_day)
        if p_button.is_pressed:
            day += 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif m_button.is_pressed:
            day -= 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif m_button.is_pressed:
            day -= 1
            command(lcd_1stline)
            writeLcd(now.strftime(
                f"{str(year % 100)}/{str(month).zfill(2)}/{str(day)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_hour)
        if p_button.is_pressed:
            hour += 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif m_button.is_pressed:
            hour -= 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_minute)
        if p_button.is_pressed:
            minute += 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif m_button.is_pressed:
            minute -= 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    while True:
        command(lcd_second)
        if p_button.is_pressed:
            second += 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif m_button.is_pressed:
            second -= 1
            command(lcd_2ndline)
            writeLcd(now.strftime(
                f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"))

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

    set_time = f"sudo hwclock --set --date='{month}/{day}/{year} {hour}:{minute}:{second}'"
    print(set_time)
    subprocess.call(shlex.split(set_time))
    subprocess.call(shlex.split("sudo hwclock -s"))


try:
    init()
    test()
finally:
    print("final")
