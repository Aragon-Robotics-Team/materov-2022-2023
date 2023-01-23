import serial
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
        # self.message = []  # list you eventually send to robot.get_send_arduino
        self.robot = rob

    def teleop_loop(self):

        if self.controller_name == "Wireless Controller":
            self.var_ps4_controller()
        elif self.controller_name == "XBOX":  # XBOX name?
            self.var_xbox_controller()
        else:
            self.var_big_controller()

        print("TELEOP STARTED")

        # ------ MATH CALC FUNCTION CALL ------ #

        message = self.thruster_calculations(self.get_gamepad_states())
        self.robot.get_send_arduino(self.robot.make_string(message))

        # takes the message list (all the thruster values) and separates by comma and period
        # uses arduino function in Robot to send to arduino

    # note: array in [LX, LT, RX, A, B]
    def var_xbox_controller(self):
        #  EXAMPLE :D
        self.numbers.set_controller_vals([0, 1, 3, 6, 7])  # shift x, shift y, yaw x, heave a, heave b

    def var_big_controller(self):
        self.numbers.set_controller_vals([0, 1, 2, 3, 5, 8])


    def var_ps4_controller(self):
        #  SNEAK :D
        pass

    def thruster_calculations(self, gamepad_states):
        message = []
        # gamepad_states = [shift x, shift y, yaw x, heave a, heave b]
        #  SNEAK :D please put math calculations in here and change variable names accordingly, thanks you very much.

        
        # ------ MATH CALCS ------ #

        #  final SIX THRUSTER calculated values stored in "message" list ===>
        return message

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
