from calendar import c
from multiprocessing.forkserver import connect_to_new_process
import pygame 
pygame.init()
pygame.joystick.init()
pygame.display.init()
controller = pygame.joystick.Joystick(0)
controller.init()

print(controller.name)