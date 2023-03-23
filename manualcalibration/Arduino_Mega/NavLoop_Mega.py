import pygame
import serial
from Arduino_Mega import MathFunc    
from time import sleep

import multiprocessing

# ---------- MAIN PROGRAM LOOP ---------- #

class Navigation:
    def __init__(self, input_queue):
        self.input_queue = input_queue
        pygame.init()

        pygame.joystick.init()


        #pygame.display.init()
        #pygame.display.set_mode((500,500))

        # message contains axis/button values
        self.message = [] 
        # [0] = LX
        # [1] = LY
        # [2] = LT
        # [3] = RX
        # [4] = RY
        # [5] = RT
        # [6] = A
        # [7] = B
        # [8] = X
        # [9] = Y
        # [10] = LB
        # [11] = RB
        # [12] = LJ
        # [13] = RJ

        self.loop = True
        self.linearMode = False
        self.sensitiveMode = False

        self.arduino = serial.Serial('/dev/cu.usbmodem142101', 9600) #might need to adjust the port 
        
        # this make code work instant
        sleep(1)
        print("nav initialized")

    def startNav(self):
        print("starting Nav Loop")
        while self.loop:
            self.message = [] #clearing the contents of the list with each loop iteration
            
            # event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # reset thrusters to prevent them from running after closing program
                    loop = False
                    print("loop = false")

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

                Lx = self.message[0] 
                Ly = self.message[1]
                Rx = self.message[2]
                A = self.message[6]
                B = self.message[7]
                X = self.message[8]
                Y = self.message[9]
                LB_Value = self.message[10]
                RB_Value = self.message[11]

                messageToSend = ""

                # Get controller input, decide whether linearMode is enabled or not
                if RB_Value > 0:
                    linearMode = True
                if LB_Value > 0:
                    linearMode = False

                # Enable Sensitive Mode or Not
                if X > 0:
                    sensitiveMode = True
                if Y > 0:
                    sensitiveMode = False
            
                # Math Calculations
                coeffs = self.queueRecieve()
                messageToSend = MathFunc.makeString(Lx, Ly, Rx, A, B, self.linearMode, self.sensitiveMode, coeffs)
                messageToSend = messageToSend.encode("ascii")
                
                self.arduino.write(messageToSend) 
                
                received = self.arduino.readline().decode("ascii")
                print(received)
                

                print("Linear Mode: " + str(self.linearMode))
                print("Sensitive Mode: " + str(self.sensitiveMode))
                
                pygame.display.update()
                
        # ---------- END MAIN PROGRAM LOOP ---------- #

        # quit pygame after user exists
        pygame.quit()

    def queueRecieve(self):
        global statuses
        while self.input_queue.empty() == False:
            statuses = self.input_queue.get()
            # print(statuses)
        return statuses
        
def startNavClass(input_queue): 
    nav = Navigation(input_queue)
    nav.startNav()