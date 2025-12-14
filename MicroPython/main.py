"""
Copyright (c) 2025 Isaac Ip All rights reserved

Created by: Isaac Ip
Created on: Dec 2025
This program sends radio messages
"""

from microbit import *
import radio
from machine import time_pulse_us

# variables
radio.on()
radio.config(group=247)
trig = pin12
echo = pin13
trig.write_digital(0)
echo.read_digital()
dist_cm = 0

# setup
display.clear()
display.show(Image.HAPPY)

while True:
    # Output a pulse to trigger ultrasonic burst
        trig.write_digital(1)
        trig.write_digital(0)

        # Measure the input echo pulse in microseconds, convert to seconds
        micros = time_pulse_us(echo, 1)
        t_echo = micros / 1000000
        # Calculate distance in cm and display on micro:bit
        dist_cm = (t_echo / 2) * 34300
        display.scroll(str(int(dist_cm)))
        if dist_cm < 5:
            radio.send("Too close")
            sleep(1000)
        else:
            radio.send("")
            sleep(1000)
