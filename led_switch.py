#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

INPUT_PIN = 7
OUTPUT_PIN = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.output(OUTPUT_PIN, GPIO.LOW)

while True:
	if not GPIO.input(INPUT_PIN):
		print "Button pressed"
		GPIO.output(OUTPUT_PIN, GPIO.HIGH)
	else:
		print "Button not pressed"
		GPIO.output(OUTPUT_PIN, GPIO.LOW)

GPIO.cleanup()