#https://stackoverflow.com/questions/67428827/stream-pygame-joystick-input-over-socket-by-sending-joystick-values-to-array

import os           #gain control of command prompt features
import pygame       #Read Joystick data
import array
from serial import Serial
import time

from ControllerTests.Math import *
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
x = 4
y = ConvertString(1, 1, 1, 1, 1)

global FL_PWM
global FR_PWM
global BL_PWM
global BR_PWM

FL_PWM, FR_PWM, BL_PWM, BR_PWM = 1500


arduino = Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=1)

def convert(vals): #go from (-1, 1) to PWM Values
    vals = 1500 - (vals * 400)
    return round(vals) #integer pwm

#change modem number accordingly(currently 142101)
#arduino = serial.Serial(port='/dev/cu.usbmodem142101', baudrate=9600, timeout=1)

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
        joystick_LY = convert(message[1])
        joystick_RX = convert(message[3])
        # joystick_RY = convert(message[4])

        # joystick2_FL, joystick2_BR = 1500 - (message[] * 400)
        # joystick2_FR, joystick2_BL = 1500 - (message[] * 400)

        
        stringVals = str(joystick_LY) + ", " + str(joystick_RX) + "."
        
        
        stringVals = stringVals.encode("ascii")
        arduino.write(stringVals)
        print(stringVals)

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