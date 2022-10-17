# -*- coding: utf-8 -*-
#!/usr/bin/python
from command import command

# I2C通信の設定　
clear = 0x01
display_On_Cursor_On = 0x0f


def setLcdInit():
    command(0x38)
    command(0x39)
    command(0x14)
    command(0x73)
    command(0x56)
    command(0x6c)
    command(0x38)
    command(clear)
    command(display_On_Cursor_On)
