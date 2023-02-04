import pygame
import serial
import MathTest    
from time import sleep

pygame.init()
pygame.joystick.init()
pygame.display.init()
pygame.display.set_mode((500,500))


# message contains axis/button values
message = [] 
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

loop = True
linearMode = False
sensitiveMode = False
arduino = serial.Serial('/dev/cu.usbmodem14201', 9600)

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

        Lx = message[0] 
        Ly = message[1]
        Rx = message[3]
        A = message[6]
        B = message[7]
        X = message[8]
        Y = message[9]
        LB_Value = message[10]
        RB_Value = message[11]

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
        messageToSend = MathTest.makeString(Lx, Ly, Rx, A, B, linearMode, sensitiveMode)
        messageToSend = messageToSend.encode("ascii")
        
        arduino.write(messageToSend) 
        
        received = arduino.readline().decode("ascii")
        print(received)
        print("Linear Mode: " + str(linearMode))
        print("Sensitive Mode: " + str(sensitiveMode))



        

            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()
