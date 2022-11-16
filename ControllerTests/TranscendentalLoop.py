import pygame
import serial
import MathFunc    
from time import sleep


arduino = serial.Serial('/dev/cu.usbmodem1101', 9600)

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# message contains axis/button values
message = [] 
loop = True

# this make code work instant
sleep(1)

# ---------- MAIN PROGRAM LOOP ---------- #

while loop:
    message = [] #clearing the contents of the list with each loop iteration
    
    
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

        # taking the values list
        Lx = message[0] 
        Ly = message[1]
        Rx = message[3]
        A = message[6]
        B = message[7]
        

        messageToSend = MathFunc.makeString(Lx, Ly, Rx, A, B)
        messageToSend = messageToSend.encode("ascii")

        arduino.write(messageToSend) 

        received = arduino.readline().decode("ascii")
        print(received)
            
# ---------- END MAIN PROGRAM LOOP ---------- #

# quit pygame after user exists
pygame.quit()

# ---------- ARDUINO CODE ---------- #

# //global variables for thruster pwms
# String br = "";
# String fl = "";
# String bl = "";
# String fr = "";
# String v1 = "";
# String v2 = "";

# void setup() {
# Serial.begin(9600); // set the baud rate
# delay(2000);
# Serial.println("Arduino is ready!");
# }

# void loop() {

#   br = Serial.readStringUntil(',').toInt();
#   fl = Serial.readStringUntil(',').toInt();
#   bl = Serial.readStringUntil(',').toInt();
#   fr = Serial.readStringUntil(',').toInt();
#   v1 = Serial.readStringUntil(',').toInt();
#   v2 = Serial.readStringUntil(',').toInt();

#   Serial.println(br + ", " + fl + ", " + bl + ", " + fr + ", " + v1 + ", "+v2);
  
# }