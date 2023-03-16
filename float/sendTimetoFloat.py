#import pygame
from time import sleep
# import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()
# for port,desc, hwid in sorted(ports):
#     print("{}: {} [{}]".format(port, desc, hwid))
import serial
#from serial import Serial
arduino = serial.Serial('COM6', 9600)
if not arduino.isOpen(): # type: ignore
    arduino.open()
print('com6 is open', arduino.isOpen()) # type: ignore

from datetime import datetime
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Current Time =", currentTime)

num = str(currentTime)
hours = str(num[0] + num[1])
mins = str(num[3] + num[4])
secs = str(num[6] + num[7])

params = [hours, mins, secs]

stringToSend = ','.join(str(x) for x in params) + ','
print('py send: ' + stringToSend)
arduino.write(stringToSend.encode('ascii'))
arduino.close()