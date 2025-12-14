"""
Copyright (c) 2025 Isaac Ip All rights reserved

Created by: Isaac Ip
Created on: Dec 2025
This program receives radio messages
"""

from microbit import *
import radio

# variables
radio.on()
radio.config(group=247)

# setup
display.clear()
display.show(Image.HAPPY)

while True:
    message = radio.receive()
    if message:
        display.clear()
        display.scroll(message)
    display.show(Image.HAPPY)
