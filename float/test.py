#import pygame
from serial import Serial
from time import sleep
arduino = Serial('COM6', 9600)
stringToSend = "red"
print('py send: ' + stringToSend)
while True:
    arduino.write(stringToSend.encode("ascii"))
    print("work????")

arduino.close()

          