# -*- coding: utf-8 -*-
#!/usr/bin/python
from gpiozero import Button

button = Button(5)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
