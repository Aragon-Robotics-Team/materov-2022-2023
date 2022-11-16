
"""
Controller class 
- Test
- Gets Axis values
- Gets button values
"""

import time
import MathFunc
import pygame

# Intialize Joysticks

class Gamepad:  
    def __init__(self, Robot) -> None:
        # holds all axis, button vals
        self.Robot = Robot
        self.message = []

    def getValueArray(self):
        return self.message

    def MainHandler(self):  # controller test
        # pretend code that updates array goes here 
        pygame.init()
        pygame.joystick.init()

        loop = True

        time.sleep(1)

        while loop:
            self.message = [] #clearing the contents of the list with each loop iteration
            
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                # elif event.type == pygame.JOYBUTTONDOWN:
                #     print("Joystick button pressed.")
                # elif event.type == pygame.JOYBUTTONUP:
                #     print("Joystick button released.")

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
                    self.message.append(joystick.get_axis(index))

                # get joystick button values
                buttons = joystick.get_numbuttons()
                for index in range(buttons):
                    button = joystick.get_button(index)
                    self.message.append(button)
            


