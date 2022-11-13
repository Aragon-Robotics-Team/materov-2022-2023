import pygame    #Read Joystick data
import serial    #communicate with arduino
import Vishal     #Vishal's math stuffs
from time import sleep #the sleep is supa important

arduino = serial.Serial('/dev/cu.usbmodem1101', 9600)
#make the serial path...exist

# Define some colors.
BLACK = pygame.Color('blue')  #test
WHITE = pygame.Color('pink')  #window-color


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
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
screen = pygame.display.set_mode((500, 700)) #500, 700

pygame.display.set_caption("Vishal's Dominion")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates.
clock = pygame.time.Clock()

# Initialize the joysticks.
pygame.joystick.init()

# Get ready to print.
textPrint = TextPrint() #textPrint is initialized as a TextPrint Object

message = []
# -------- Main Program Loop -----------
while not done:
    
    #message here is going to have ALL the information in 
    #it's smooth lil brain so make sure to treat it well
    message = [] #clearing the contents of the list with each loop iteration
    
    # EVENT PROCESSING STEP
    #
    # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
    # JOYBUTTONUP, JOYHATMOTION
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    #
    # DRAWING STEP
    #
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    textPrint.reset()

    # Get count of joysticks.
    joystick_count = pygame.joystick.get_count()

    textPrint.tprint(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()

    # For each joystick:
    for i in range(joystick_count):
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

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        textPrint.tprint(screen, "Number of axes: {}".format(axes))
        textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.tprint(screen, "Axis {} value: {:>6.3f}".format(i, axis))
            message.append(joystick.get_axis(i))
        textPrint.unindent()

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

        
        for i in range(len(message)):
            print(message)
            value = message[int(i)]
            textPrint.tprint(screen, "value {}: {}".format(i, value))

        #taking the values from message that we actually need
            Lx = message[0]
            Ly = message[1]
            Rx = message[3]
            A = message[6]
            B = message[7]
            #0, 1, 3, 6, 7 are the indices we need

            mensaje = Vishal.makeString(Lx, Ly, Rx, A, B)
            if (serial.Serial.inWaiting(arduino) > len(mensaje)):
             arduino.write(str(mensaje).encode('utf-8')) 
             print(arduino.readline()) # Read the newest output from the Arduino
            
            #sleep(0.00001) # Delay for one tenth of a second   

    
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second.
    clock.tick(20)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()

"""
ARDUINO CODE:
void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
}
void loop() {
String inStr = " ";
if(Serial.available()){ // only send data back if data has been sent
  String inStr = String(Serial.read()); // read the incoming data
  if (Serial.availableForWrite() > inStr.length()) {
  Serial.println(inStr); // send the data back in a new line so that it is not all one long line
  //delay(0.00001);
  }
}
}




"""

