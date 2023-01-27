import pygame
import serial
import MathFunc    
from time import sleep

serialOn = True
delay = 0.2

if serialOn:
    arduino = serial.Serial('/dev/cu.usbmodem1421401', 9600)

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# message contains axis/button values
message = [] 
loop = True

# this make code work instant
sleep(1)

# ---------- MAIN PROGRAM LOOP ---------- #

pygame.init()
pygame.joystick.init()
pygame.display.init()

while True:
    print("not detected")
    pygame.event.get()
    if pygame.joystick.get_count() > 0:
        break

controller = pygame.joystick.Joystick(0)
controller.init()
print("Controller name:" + controller.get_name())
# lx = 0
# ly = 1
# rx = 3
# ry = 4

while True:
    sleep(delay)
    pygame.event.pump()
    Lx = controller.get_axis(0) * -1
    Ly = controller.get_axis(1)   # y is inverted on joystick
    Rx = controller.get_axis(3) * -1
    A = controller.get_button(0)
    B = controller.get_button(3)

    print(Lx, Ly, Rx, A, B)

    # construct string, send to arduino, received info back

    messageToSend = MathFunc.makeString(Lx, Ly, Rx, A, B, 1)
    print("sending: ", messageToSend)

    if serialOn:
        messageToSend = messageToSend.encode("ascii")

        arduino.write(messageToSend)

        received = arduino.readline().decode("ascii")
        print("received: " + received)
            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()
