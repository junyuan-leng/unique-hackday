#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import bluetooth

target_name = "233"
target_addr = None

nearby_devices = bluetooth.discover_devices()
for bdaddr in nearby_devices:
	if target_name == bluetooth.lookup_name(bdaddr):
		target_addr = bdaddr
		break

if target_addr is not None:
	print "Found target bluetooth device with address ", target_addr
	port = 1
	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
	sock.connect((target_addr, port))
	sock.send("hello")
	sock.close()
else:
	print "Target bluetooth device not found"
