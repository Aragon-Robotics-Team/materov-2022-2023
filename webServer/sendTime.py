import pygame
from serial import Serial
arduino = Serial('/dev/cu.usbmodem141201', 9600)
while True:
    command = str(input("Time: "))
    #arduino.write(command)
    time = str(arduino.readline())
    print(time)