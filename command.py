# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus
import time

# I2C通信の設定　
i2c = smbus.SMBus(1)  # 1 is bus number
i2c_addr = 0x3e  # lcd
resister_aqm0802 = 0x00


def command(code):
    i2c.write_byte_data(i2c_addr, resister_aqm0802, code)
    time.sleep(0.1)
