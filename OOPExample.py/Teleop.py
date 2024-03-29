import serial
import MathFunc
import pygame
from time import sleep
from Numbers import Numbers

class Teleop:
    def __init__(self, rob) -> None:
        #### Pygame initialization
        pygame.init()
        pygame.joystick.init()
        pygame.display.init()
        while True:
            pygame.event.get()
            if pygame.joystick.get_count() > 0:
                break
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        self.controller_name = self.gamepad.get_name()
        print("Pygame initialized. Controller name:" + self.controller_name)

        self.numbers = Numbers()
        self.gamepad_states = [] # list you send to math calcs
        self.message = []  # list you send to robot.get_send_arduino
        self.robot = rob


    def start(self):

        self.var_ps4_controller() if self.controller_name == "Wireless Controller" else self.var_big_controller()
        print("TELEOP STARTED")

        self.thruster_calculations(self.get_gamepad_states())

    def var_xbox_controller(self):
        self.numbers.set_controller_vals([0, 1, 3, 6, 7])  # shift x, shift y, yaw x, heave a, heave b

    def var_big_controller(self):
        #  SNEAK :D
        pass

    def var_ps4_controller(self):
        #  SNEAK :D
        pass
    def thruster_calculations(self, gamepad_states):   # gamepad_states = [shift x, shift y, yaw x, heave a, heave b]
        #  SNEAK :D
        pass

    def get_gamepad_states(self):
        while True:
            all_states = []  # clearing the contents of the list with each loop iteration

            # get joystick axis values
            axes = self.gamepad.get_numaxes()
            for index in range(axes):
                axis = self.gamepad.get_axis(index)
                all_states.append(axis)

            # get joystick button values
            buttons = self.gamepad.get_numbuttons()
            for index in range(buttons):
                button = self.gamepad.get_button(index)
                all_states.append(button)

            # taking only the values that we need
            temp = [self.numbers.shift_x, self.numbers.shift_y, self.numbers.yaw_x, self.numbers.heave_a,
                    self.numbers.heave_b]

            for i in range(len(self.gamepad_states)):
                self.gamepad_states.append(all_states[temp[i]])

            return self.gamepad_states

