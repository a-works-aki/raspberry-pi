# -*- coding: utf-8 -*-
#!/usr/bin/python


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
