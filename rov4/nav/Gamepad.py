
"""
Controller class 
- Test
- Gets Axis values
- Gets button values
"""

import time
import nav.MathFunc
import pygame

# Intialize Joysticks

class Gamepad:  
    def __init__(self, Robot) -> None:
        # holds all axis, button vals
        self.Robot = Robot
        self.message = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def init(self):
        while True:
            print("not detected") # change to queue l8er
            pygame.event.get()
            if pygame.joystick.get_count() > 0:
                break

        controller = pygame.joystick.Joystick(0)
        controller.init()
        print("Controller name:" + controller.get_name())


    def getValueArray(self):
        return self.message

    def MainHandler(self):  # controller test
        
        pygame.init()
        pygame.joystick.init()

        loop = True
        values = []

        time.sleep(1)

        while loop:
            values = [] #clearing the contents of the list with each loop iteration
            
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
                    values.append(joystick.get_axis(index))

                # get joystick button values
                buttons = joystick.get_numbuttons()
                for index in range(buttons):
                    button = joystick.get_button(index)
                    values.append(button)

            self.message = values
            print(self.message)
            


