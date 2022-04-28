#!/usr/bin/python
# //////////////////////////////////////
# 	blink.py
# 	Blinks one LED wired to P9_14.
# 	Wiring:	P9_14 connects to the plus lead of an LED.  The negative lead of the
# 			LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
# 			to ground.
# 	Setup:
# 	See:
# //////////////////////////////////////
import time

import Adafruit_BBIO.GPIO as GPIO  # type: ignore

from morse_messages.morse_code.morse_code import InternationalMorseCode

out = "P9_14"

GPIO.setup(out, GPIO.OUT)
TIME_UNIT_S = 0.5

while True:
    GPIO.output(out, GPIO.HIGH)
    time.sleep(InternationalMorseCode.UNIT * TIME_UNIT_S)
    GPIO.output(out, GPIO.LOW)
    time.sleep(0.5)
