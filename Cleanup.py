#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
	GPIO.cleanup()
finally:
        GPIO.cleanup()
        
