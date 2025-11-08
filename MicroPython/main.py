"""
Created by: Isaac Ip
Created on: Nov 2025
This module is a Micro:bit MicroPython program
"""

from microbit import *
import radio

# variables
distanceToObject = 0

radio.on()
radio.config(channel=7)

while True:
    
