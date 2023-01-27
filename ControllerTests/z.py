import pygame
import serial
import MathFunc    
from time import sleep


pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# message contains axis/button values
message = [] 

loop = True

# this make code work instant
sleep(1)

# ---------- MAIN PROGRAM LOOP ---------- #

while loop:
    message = [] #clearing the contents of the list with each loop iteration
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    # Get count of interactables.
    joystick_count = pygame.joystick.get_count()

    # For each interactable:
    for index in range(joystick_count):
        joystick = pygame.joystick.Joystick(index)
        joystick.init()        

        # get joystick axis values
        axes = joystick.get_numaxes()
        for index in range(axes):
            axis = joystick.get_axis(index)
            message.append(joystick.get_axis(index))

        # get joystick button values
        buttons = joystick.get_numbuttons()
        for index in range(buttons):
            button = joystick.get_button(index)
            message.append(button)

    print(message)
            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()