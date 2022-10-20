import pygame
import Jiaqi
import time

# Initialize pygame modules
pygame.joystick.init()
# pygame.display.init()

# Window setup
WIDTH, HEIGHT = 500, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = pygame.display.set_caption("Yes")

# Intialize Joysticks
joysticks = []
for index in range(pygame.joystick.get_count()):
    joystick = pygame.joystick.Joystick(index)
    joystick.init()

loop = True
joysticks = {}
axis_values = [0, 0, 0, 0, 0, 0]
# [0] = LX
# [1] = LY
# [2] = LT
# [3] = RX
# [4] = RY
# [5] = RT

button_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0] = A
# [1] = B
# [2] = X
# [3] = Y
# [4] = LB
# [5] = RB
# [6] = LJ
# [7] = RJ
# [8] = stuff
# [9] = stuff
# [10] = stuff

# ------------------------------------------------------------------------------------------------------ #
# Start of MAIN LOOP


while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        
        if event.type == pygame.JOYDEVICEADDED:
                # This event will be generated when the program starts for every
                # joystick, filling up the list without needing to create them manually.
                joy = pygame.joystick.Joystick(event.device_index)
                joysticks[joy.get_instance_id()] = joy
                print(f"Joystick {joy.get_instance_id()} connected")
        
        for joystick in joysticks.values():
            
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                axis_values[i] = axis

            buttons = joystick.get_numbuttons()
            print(buttons)
            for i in range(buttons):
                button = joystick.get_button(i)
                button_values[i] = button
        
        print(axis_values)
        print(button_values)
  
