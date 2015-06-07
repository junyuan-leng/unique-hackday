#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write("233")
try:
	while True:
		response = ser.readline()
		print response
except KeyboardInterrupt:
	ser.close()