# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus
import time
import datetime
import subprocess
import shlex
from gpiozero import Button, LED
from command import command
from writeLcd import writeLcd
from setLcdInit import setLcdInit
from time import sleep

# LCDのカーソルアドレスの定義
lcd_addresses = {
    "year": 0x81,
    "month": 0x84,
    "day": 0x87,
    "hour": 0xc1,
    "minute": 0xc4,
    "second": 0xc7,
    "1stline": 0x80,
    "2ndline": 0xc0
}

# 入力ボタンの設定
set_button = Button(1, hold_time=2)
p_button = Button(8)
m_button = Button(7)

# 現在の日時の取得と変数の設定
now = datetime.datetime.now()
time_components = {
    "year": now.year,
    "month": now.month,
    "day": now.day,
    "hour": now.hour,
    "minute": now.minute,
    "second": now.second
}

# 日時の最小値と最大値の設定
ranges = {
    "year": (2000, 2099),
    "month": (1, 12),
    "day": (1, 31),
    "hour": (0, 23),
    "minute": (0, 59),
    "second": (0, 59)
}

# セットフラグの初期化
set_flag = 0
# LCDのLEDの設定
lcdLed = LED(4)
# LCDの1行目のアドレス
lcd_1stline = 0x80

# セットフラグの設定関数


def setting_flag():
    global set_flag
    set_flag = 1

# 日付の表示関数


def displayDate():
    command(lcd_addresses["1stline"])
    writeLcd(now.strftime(
        f"{str(time_components['year'] % 100).zfill(2)}/{str(time_components['month']).zfill(2)}/{str(time_components['day']).zfill(2)}"))

# 時刻の表示関数


def displayTime():
    command(lcd_addresses["2ndline"])
    writeLcd(now.strftime(
        f"{str(time_components['hour']).zfill(2)}:{str(time_components['minute']).zfill(2)}:{str(time_components['second']).zfill(2)}"))

# "SET OK"の表示関数


def displayOk():
    command(lcd_1stline)
    writeLcd("SET OK")

# 日時部分の変更関数


def changeTimeComponent(component_name):
    global set_flag
    min_value, max_value = ranges[component_name]
    while True:
        command(lcd_addresses[component_name])
        if p_button.is_pressed:
            time_components[component_name] += 1
            if time_components[component_name] > max_value:
                time_components[component_name] = min_value
            displayDate()

        elif m_button.is_pressed:
            time_components[component_name] -= 1
            if time_components[component_name] < min_value:
                time_components[component_name] = max_value
            displayDate()

        elif set_flag == 1:
            set_flag = 0
            break

        set_button.when_pressed = setting_flag

        time.sleep(0.2)

# 日時設定のメイン関数


def setDateTime():
    global time_components
    lcdLed.on()
    setLcdInit()

    displayDate()
    displayTime()
    sleep(1)

    for component_name in ["year", "month", "day", "hour", "minute", "second"]:
        changeTimeComponent(component_name)

    set_time = f"sudo hwclock --set --date='{time_components['month']}/{time_components['day']}/{time_components['year']} {time_components['hour']}:{time_components['minute']}:{time_components['second']}'"
    setLcdInit()
    print(set_time)
    displayOk()
    sleep(1)
    lcdLed.off()

    try:
        subprocess.call(shlex.split(set_time))
    except ValueError:
        setLcdInit()
        command(lcd_addresses["1stline"])
        writeLcd("date")
        command(lcd_addresses["2ndline"])
        writeLcd("  error")
        time.sleep(1)

    subprocess.call(shlex.split("sudo hwclock -s"))
    print("final")
