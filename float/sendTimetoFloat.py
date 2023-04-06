#import pygame
from serial import Serial
from time import sleep
arduino = Serial('COM6', 9600, timeout = 0)

from datetime import datetime

while True:

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print("Current Time =", currentTime)

    num = str(currentTime)
    hours = str(num[0] + num[1])
    mins = str(num[3] + num[4])
    secs = str(num[6] + num[7])

    params = [hours, mins, secs]
    print(":")

    stringToSend = ','.join(str(x) for x in params) + '.'
    print('py send: ' + stringToSend)
    arduino.write(stringToSend.encode("ascii"))
    sleep(0.2)
