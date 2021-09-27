#!/bin/env python
import serial
print('Serial read is running')
arduino = serial.Serial('/dev/ttyUSB0', baudrate=115200, timeout=1.0)   
while(True):
 line = arduino.readline().decode('utf-8')
 print(line)
