import pygame
from OOPFinal.nav.Robot import MathFunc
from time import sleep
from OOPFinal.nav.Teleop.Numbers import Numbers
from OOPFinal.nav.Robot.Robot import Robot
from OOPFinal.nav.Autonomous.Autonomous import Autonomous

class Teleop:
    def __init__(self, rob: Robot) -> None:
        #### Pygame initialization
        pygame.init()
        pygame.joystick.init()
        pygame.display.init()
        while True:
            pygame.event.get()
            print("Gamepad is disconnected")
            if pygame.joystick.get_count() > 0:
                break
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        self.controller_name = self.gamepad.get_name()
        print("Pygame initialized. Controller name:" + self.controller_name)

        self.numbers = Numbers()
        # self.gamepad_states = [] # list you send to MathFunc
        # self.message = []  # list you eventually send to robot.get_send_arduino
        self.robot = rob

    def teleop_loop(self):  # determines what controller we have and sets Numbers object accordingly
        gp_name = self.gamepad.get_name()
        if gp_name == "Wireless Controller":
            self.var_ps4_controller()
        elif gp_name.find("BOX") != -1:  # XBOX name?
            self.var_xbox_controller()
        else:
            self.var_big_controller()
        self.var_xbox_controller()
        print(gp_name, self.numbers.heave_b)

        print("TELEOP STARTED")

        # ------ MATH CALC FUNCTION CALL ------ #
        while True:
            pygame.event.pump()

            # if self.switch_to_auto():  # if the queue is saying to switch to auto
            #     auto = Autonomous(self.robot)
            #     auto.begin_and_loop()
            all_gp_states = self.get_gamepad_states()  # stores all the states of the gamepad into an array

            shift_x = all_gp_states[self.numbers.shift_x]  # calculates the states of the speecified things we need based on what controller we have
            shift_y = all_gp_states[self.numbers.shift_y]
            yaw_x = all_gp_states[self.numbers.yaw_x]
            heave_a = all_gp_states[self.numbers.heave_a]
            heave_b = all_gp_states[self.numbers.heave_b]
            drive_straight = -(all_gp_states[2])  # temporary thing to try with the straight forward/back on big gp

            # ------ MATH CALCS ------ #
            pwmArray = MathFunc.makeString(shift_x, shift_y, yaw_x, heave_a, heave_b, 100, 100)

            ds_pwm = 1500 + (pow(drive_straight, 1.5) * 350)

            print(ds_pwm)
            pwmArray[0] = ds_pwm
            pwmArray[1] = ds_pwm
            pwmArray[2] = ds_pwm
            pwmArray[3] = ds_pwm
            print(pwmArray)

            #  final SIX THRUSTER calculated values stored in "message" list ===>
            sendStr = (str(pwmArray[0]) + "-" +
                       str(pwmArray[1]) + "=" +
                       str(pwmArray[2]) + "+" +
                       str(pwmArray[3]) + "*" +
                       str(pwmArray[4]) + "," +
                       str(pwmArray[5]) + ".")

            # self.robot.get_send_arduino(sendStr)

            pygame.event.clear()
            sleep(self.robot.delay)

    def switch_to_auto(self) -> bool:
        period = self.robot.get_queue()[0]
        if period != 0:
            return True
        return False

    def var_xbox_controller(self):
        #  EXAMPLE :D
        self.numbers.set_controller_vals([0, 1, 3, 6, 7])  # shift x, shift y, yaw x, heave a, heave b

    def var_big_controller(self):
        self.numbers.set_controller_vals([0, 1, 3, 5, 6])

    def var_ps4_controller(self):
        self.numbers.set_controller_vals([0, 1, 2, 6, 7]) 

    def get_gamepad_states(self) -> list:
        gp_states = []  # clear every iteration

        joystick_count = pygame.joystick.get_count()
        # For each interactable:
        for index in range(joystick_count):
            joystick = pygame.joystick.Joystick(index)
            joystick.init()

            # get joystick axis values
            axes = joystick.get_numaxes()
            for index in range(axes):
                axis = joystick.get_axis(index)
                gp_states.append(round(joystick.get_axis(index), 4))

            # get joystick button values
            buttons = joystick.get_numbuttons()
            for index in range(buttons):
                button = joystick.get_button(index)
                gp_states.append(button)

        return gp_states

    def check_queue(self):
        array = self.robot.get_queue()
        return array[0]
