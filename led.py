#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

OUTPUT_PIN = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(OUTPUT_PIN, GPIO.OUT)
GPIO.output(OUTPUT_PIN, GPIO.HIGH)

for i in range(20):
	GPIO.output(OUTPUT_PIN, GPIO.LOW)
	time.sleep(1)
	GPIO.output(OUTPUT_PIN, GPIO.HIGH)
	time.sleep(1)

GPIO.cleanup()