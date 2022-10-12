#https://stackoverflow.com/questions/67428827/stream-pygame-joystick-input-over-socket-by-sending-joystick-values-to-array

import os           #gain control of command prompt features
import pygame       #Read Joystick data
import array
from serial import Serial
import time
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

global FL_PWM
global FR_PWM
global BL_PWM
global BR_PWM

# FL_PWM, FR_PWM, BL_PWM, BR_PWM = 1500

def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1= v2= fr= fl= br= bl = 1500
    sendStr = "" #constructed string to be sent to the arduino

    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0
    

    turn = PWM(Rx/6)
    br += round(PWM((Lx+Ly)/4) - turn)
    fl -= round(PWM((Lx+Ly)/4) - turn)
    bl += round(PWM((Ly-Lx)/4) - turn)
    fr -= round(PWM((Lx-Ly)/4) - turn)
    

    Vstrength = 200 #vertical thruster code chunks
    if(A): #if A is pressed
        v1 += Vstrength
        v2 += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength
        v2 -= Vstrength
        #v1 and v2 go down

    
    
    sendStr  = str(br)+","+str(fl)+","+str(bl)+","+str(fr)+","+str(v1)+","+str(v2) + ","
    return sendStr

arduino = Serial(port='/dev/cu.usbmodem14201', baudrate=9600, timeout=1)

#change modem number accordingly


os.system('title client')  #rename command prompt
os.system('cls')           #clear command prompt screen



# Define some colors.
TextColor = pygame.Color('blue')
BackgroundColor= pygame.Color('pink')


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, TextColor)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10


pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((500, 700))

pygame.display.set_caption("The Name Is Bob")  # the top of the Python window

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint()

#message = array.array('d',[])

# -------- Main Program Loop -----------
while not done:
    
    #clear message
    #message = array.array('d', [])
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
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BackgroundColor)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count): #initializing joysticks
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        try:
            jid = joystick.get_instance_id()
        except AttributeError:
            # get_instance_id() is an SDL2 method
            jid = joystick.get_id()
        textPrint.tprint(screen, "Joystick {}".format(jid))
        textPrint.indent()

        # Get the name from the OS for the controller/joystick.
        name = joystick.get_name()
        textPrint.tprint(screen, "Joystick name: {}".format(name))

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
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            message.append(joystick.get_axis(i))
        textPrint.unindent()  #are these the axes?

        buttons = joystick.get_numbuttons()
        textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.tprint(screen, "Button {:>2} value: {}".format(i, button))
            message.append(button)
        textPrint.unindent()
        hats = joystick.get_numhats()
        textPrint.tprint(screen, "Number of hats: {}".format(hats))
        textPrint.indent()
        
        # Hat position. All or nothing for direction, not a float like
        # get_axis(). Position is a tuple of int values (x, y).
        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.tprint(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()

        textPrint.unindent()

        i = range(len(message))

        textPrint.tprint(screen, "array length {}".format(i))
        
        # joystick_LX = convert(message[0])
        
        # joystick_RY = convert(message[4])

        # joystick2_FL, joystick2_BR = 1500 - (message[] * 400)
        # joystick2_FR, joystick2_BL = 1500 - (message[] * 400)

        
        arduino.write(makeString(message[0], message[1], message[3], 1, 0.5).encode("ascii"))

        #arduino.write(funcs.mathify(message)) #write the arduino the instructions
        for i in range(len(message)):  
            value = message[int(i)]
            textPrint.tprint(screen, "value {}: {}".format(i, value))

            
            

    #
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    #

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()