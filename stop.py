#!/usr/bin/env python
import os
import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')
import xbmc


import datetime
from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)

while True:
    if (GPIO.input(26) == False):
        xbmc.Player().stop()

    sleep(0.1);