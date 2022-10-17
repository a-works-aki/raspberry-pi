# -*- coding: utf-8 -*-
#!/usr/bin/python
import smbus

# I2C通信の設定　
i2c = smbus.SMBus(1)  # 1 is bus number
i2c_addr = 0x3e  # lcd
resister_aqm0802 = 0x00
data = 0x40


def writeLcd(message):
    mojilist = []
    for moji in message:
        mojilist.append(ord(moji))
    i2c.write_i2c_block_data(i2c_addr, data, mojilist)
