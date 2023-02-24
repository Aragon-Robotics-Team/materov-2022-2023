import pygame
import serial
import MathFunc    
from time import sleep

pygame.init()
pygame.joystick.init()
pygame.display.init()
pygame.display.set_mode((500,500))

autoTransect = False
autoDock = False
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
arduino = serial.Serial('/dev/cu.usbmodem142101', 9600)

# this make code work instant
sleep(1)

# ---------- MAIN PROGRAM LOOP ---------- #

while loop:
    message = [] #clearing the contents of the list with each loop iteration
    
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # reset thrusters to prevent them from running after closing program
            arduino.write(str(1500) + "-" + 
                str(1500) + "=" + 
                str(1500) + "+" + 
                str(1500) + "*" + 
                str(1500) + "," + 
                str(1500) + ".") 

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
        Rx = message[2]
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

        if(autoDock): #add in button number(LT-2 and RT-5)
            #request ip process autodock to begin
            #take data from ip process autodock
            #Lx = get x-vector fromqueue
            #Ly = make it some constant that can be easily changed
            #Rx = getfromqueue
            #A = convert y-vector to vertical thrust
            #B = getfromqueue
            pass
        if(autoTransect):
            #request ip process autoTransect to begin
            #take data from ip process autoTransect
            #Lx = get x vector from queue
            #Ly = some constant speed forward that can be easily changed
            #Rx = getfromqueue(optional: if not straight go turn the center)
            #A = getfromqueue(optional: if too big go make A higher)
            #B = getfromqueue(optional: if too small make B lower)
            pass
        #Vishal: ask how nav tells IP to start calculating things

    
        # Math Calculations
        messageToSend = MathFunc.makeString(Lx, Ly, Rx, A, B, linearMode, sensitiveMode)
        messageToSend = messageToSend.encode("ascii")
        
        arduino.write(messageToSend) 
        
        received = arduino.readline().decode("ascii")
        print(received)
        print("Linear Mode: " + str(linearMode))
        print("Sensitive Mode: " + str(sensitiveMode))
        
        pygame.display.update()





            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()
