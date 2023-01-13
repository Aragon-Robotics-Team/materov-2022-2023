import pygame
import serial
from time import sleep
pygame.init()
pygame.joystick.init()
pygame.display.init()

# initialize arduino
arduino = serial.Serial(port='/dev/cu.usbmodem141201', baudrate=9600, timeout=1)

sleep(1)  # important
print("ready")

while True:  # waits for joysticks to be detected
    print("not detected")
    pygame.event.get()
    if pygame.joystick.get_count() > 0:
        break

# initialize joystick
controller = pygame.joystick.Joystick(0)
controller.init()
print("Controller name:" + controller.get_name())

while True:
    pygame.event.pump()  # or get()

    stringToSend = str(controller.get_axis(5)) + ","
    arduino.write(stringToSend.encode("ascii"))
    # data sent to arduino
    # waits for arduino to do something
    # print("string ready")
    while arduino.in_waiting == 0:
        pass
    recieved = arduino.readline().decode("ascii")  # read arduino data with timeout = 1
    print(recieved)

    sleep(0.1)
