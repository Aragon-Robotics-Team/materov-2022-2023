#https://stackoverflow.com/questions/67428827/stream-pygame-joystick-input-over-socket-by-sending-joystick-values-to-array

import os           #gain control of command prompt features
import pygame       #Read Joystick data
import serial

#the message array has all the values needed(that can then be stringified)
#funcs.py
#arduino.write(funcs.mathify(message)) line is near line 188
"""
Objectives:
 - Connect to Arduino port
 - Read thruster values and mathify 
 - Construct String
 - Encode String(ASCII)
 - Write string to Arduino
"""


#change modem number accordingly(currently 101)
#arduino = serial.Serial(port='/dev/cu.usbmodem101', baudrate=9600, timeout=1) 

os.system('title client')  #rename command prompt
os.system('cls')           #clear command prompt screen



# Define some colors.
TextColor = pygame.Color('blue')
BackgroundColor= pygame.Color('pink')


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.



pygame.init()

# Initialize the joysticks.
pygame.joystick.init()


# -------- Main Program Loop -----------
done = False
while not done:
    
    #clear message
    message = []
    #
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION

    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            if event.button == 0: #button A
                print("Button A was pressed bois")  #up
            if event.button == 1:
                print("Button B")  #down
            if event.button == 2:
                print("Button X")  #claw
            if event.button == 3:
                print("Button Y")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")


    #
    # DRAWING STEP
    #
    # First, clear the screen to BackgroundColor. Don't put other drawing commands
    # above this, or they will be erased with this command.
    


    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    

    # For each joystick:
    for i in range(joystick_count): #initializing joysticks
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()
       

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        

        # try:
        #     guid = joystick.get_guid()
        # except AttributeError:
        #     # get_guid() is an SDL2 method
        #     pass
        # else:
        #     textPrint.tprint(screen, "GUID: {}".format(guid))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        

        for i in range(axes):
            axis = joystick.get_axis(i)
            
            message.append(joystick.get_axis(i))
      

        buttons = joystick.get_numbuttons()
        

        for i in range(buttons):
            button = joystick.get_button(i)      
            message.append(button)
       

        #print(vish.makeString(Lx, Ly, Rx, A, B))
        print(vish.makeString(5, 5, 5, 5, 5))
        print("hi")
            


        i = range(len(message))

       
        
        joystick
        #arduino.write(funcs.mathify(message).encode("utf--8")) #write the arduino the instructions
        for i in range(len(message)):  
            value = message[int(i)]
            

            
            


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()