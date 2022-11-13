import pygame
from time import sleep
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

while True:
    pygame.event.pump()
    print(str(controller.get_axis(0)))
    print(str(controller.get_axis(1)))
    print(str(controller.get_axis(2)))
    print(str(controller.get_axis(3)))
    print(str(controller.get_axis(4)))
    print(str(controller.get_axis(5)))

    sleep(0.3)