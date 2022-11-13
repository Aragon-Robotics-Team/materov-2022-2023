import pygame    #Read Joystick data
import serial    #communicate with arduino
import Vishal     #Vishal's math stuffs
from time import sleep #the sleep is supa important


arduino = serial.Serial('/dev/cu.usbmodem1101', 9600) #make the serial path...exist

pygame.init()
done = False # Loop until the user clicks the Red X button.
clock = pygame.time.Clock() # Used to manage how fast the screen updates.
pygame.joystick.init() # Initialize the joysticks.
message = [] #message will have all the button info in it

while not done: # Main Program Loop
    message = [] #clearing the contents of the list with each loop iteration
    
    # # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something.
        if event.type == pygame.QUIT: # If user clicked close.
            done = True # Flag that we are done so we exit this loop.
        elif event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        elif event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

    # Get count of interactables.
    joystick_count = pygame.joystick.get_count()

    # For each interactable:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()          

        axes = joystick.get_numaxes() #Lx, Ly, Rx
        for i in range(axes):
            axis = joystick.get_axis(i)
            message.append(joystick.get_axis(i))

        buttons = joystick.get_numbuttons() #A and B
        for i in range(buttons):
            button = joystick.get_button(i)
            message.append(button)

        #print(message)
        
        Lx = message[0] #taking the values from message that we actually need
        Ly = message[1]
        Rx = message[3]
        A = message[6]
        B = message[7]
        #0, 1, 3, 6, 7 are the indices we need

        mensaje = Vishal.makeString(Lx, Ly, Rx, A, B)
        #print(mensaje.encode()) # testing math string

        #if (serial.Serial.inWaiting(arduino) > len(mensaje)):
        arduino.write(str(mensaje).encode()) 
        print(arduino.readline().decode()) # Read the newest output from the Arduino
            
    # Limit to 20 frames per second.
    clock.tick(20)

pygame.quit()

"""
ARDUINO CODE:
String inStr = " ";
String br = " ";
String fl = " ";
String bl = " ";
String fr = " ";
String v1 = " ";
String v2 = " ";

void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
}
void loop() {

  br = Serial.readStringUntil(',');
  fl = Serial.readStringUntil(',');
  bl = Serial.readStringUntil(',');
  fr = Serial.readStringUntil(',');
  v1 = Serial.readStringUntil(',');
  v2 = Serial.readStringUntil(',');

  Serial.println("arduino say yass"+br+","+fl+","+bl+","+fr+","+v1+","+v2);
}
"""


    

"""
-I want to take specific values from the messages array
-put them through the Vishal.py file
-arduino.write 'em
-send them back for verification
"""