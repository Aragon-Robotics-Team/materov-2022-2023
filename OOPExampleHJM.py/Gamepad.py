
"""
Controller class 
- Test
- Gets Axis status
- Gets button status
"""

import time
import calc
import pygame
import serial

# Intialize Joysticks

class Gamepad:  
    #def __init__(self) -> None:

    def joy_init(self):
        # Initialize pygame modules
        pygame.init()
        pygame.joystick.init()
        pygame.display.init()
        self.loop = True
        self.joysticks = []
        for index in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(index)
            joystick.init()
        self.joysticks = {}
        self.axis_values = [0, 0, 0, 0, 0, 0]
        self.button_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.PWM_values = [0, 0, 0, 0, 0]
        

    def test(self):  # controller test
        while self.loop:

            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                
                if event.type == pygame.JOYDEVICEADDED:
                        # This event will be generated when the program starts for every
                        # joystick, filling up the list without needing to create them manually.
                        joy = pygame.joystick.Joystick(event.device_index)
                        self.joysticks[joy.get_instance_id()] = joy
                        print(f"Joystick {joy.get_instance_id()} connected")
                
                for joystick in self.joysticks.values():  # type: ignore
                    axes = joystick.get_numaxes()
                    for i in range(axes):
                        axis = joystick.get_axis(i)
                        self.axis_values[i] = axis

                    buttons = joystick.get_numbuttons()
                    for i in range(buttons):
                        button = joystick.get_button(i)
                        self.button_values[i] = button

                # vals for makeString() method
                LX = self.axis_values[0]
                LY = self.axis_values[1]
                RX = self.axis_values[3]
                A_button = self.button_values[0]
                B_button = self.button_values[1]
    def listVals(self):
        # vals for makeString() method
        LX = self.axis_values[0]
        LY = self.axis_values[1]
        RX = self.axis_values[3]
        A_button = self.button_values[0]
        B_button = self.button_values[1]
        message = calc.makeString(LX, LY, RX, A_button, B_button)
        print(message)
        # print(axis_values)
        # print(button_values)
