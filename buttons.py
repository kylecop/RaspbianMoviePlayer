
#!/usr/bin/python

import sys
sys.path.append('/storage/.kodi/addons/python.RPi.GPIO/lib')

import RPi.GPIO as GPIO
import xbmc

upPin = 17              # board pin 11
downPin = 27    # board pin 13
leftPin = 22    # board pin 15
rightPin = 6    # board pin 31
selectPin = 13  # board pin 33
shiftPin = 19   # board pin 35

def up_callback(channel):
    if(GPIO.input(shiftPin)):
        xbmc.executebuiltin("Action(Up)")
    else:
        xbmc.executebuiltin("Action(Back)")

def down_callback(channel):
    if(GPIO.input(shiftPin)):
        xbmc.executebuiltin("Action(Down)")
    else:
        xbmc.executebuiltin("Action(Info)")

def left_callback(channel):
    if(GPIO.input(shiftPin)):
        xbmc.executebuiltin("Action(Left)")
    else:
        xbmc.executebuiltin("Action(Stop)")

def right_callback(channel):
    if(GPIO.input(shiftPin)):
        xbmc.executebuiltin("Action(Right)")
    else:
        xbmc.executebuiltin("Action(PlayPause)")

def select_callback(channel):
    if(GPIO.input(shiftPin)):
        xbmc.executebuiltin("Action(Select)")
    else:
        xbmc.executebuiltin("Action(ContextMenu)")

class Main:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(upPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(downPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(leftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(rightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(selectPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(shiftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(upPin, GPIO.FALLING, callback=up_callback, bouncetime=300)
    GPIO.add_event_detect(downPin, GPIO.FALLING, callback=down_callback, bouncetime=300)
    GPIO.add_event_detect(leftPin, GPIO.FALLING, callback=left_callback, bouncetime=300)
    GPIO.add_event_detect(rightPin, GPIO.FALLING, callback=right_callback, bouncetime=300)
    GPIO.add_event_detect(selectPin, GPIO.FALLING, callback=select_callback, bouncetime=300)

    while not xbmc.abortRequested:
        xbmc.sleep(5)

class TidyUp:
    GPIO.remove_event_detect(upPin)
    GPIO.remove_event_detect(downPin)
    GPIO.remove_event_detect(leftPin)
    GPIO.remove_event_detect(rightPin)
    GPIO.remove_event_detect(selectPin)
    GPIO.cleanup([upPin,downPin,leftPin,rightPin,selectPin,shiftPin])


if (__name__ == "__main__"):
    Main()
    TidyUp()
