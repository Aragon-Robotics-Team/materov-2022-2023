import pygame
import time

# Initiate the pygame modules
pygame.init()  
pygame.joystick.init()
pygame.display.init()

WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))




while True:
    print(pygame.joystick.get_count())
    for event in pygame.event.get():
        print(event)
  
