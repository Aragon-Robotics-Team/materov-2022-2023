#simple ASCII serial template for new nav trainees to use

import serial
from time import sleep  #the sleep is supa important

ser = serial.Serial('/dev/cu.usbmodem1411401', 9600)

counter = 32 # Below 32 everything in ASCII is gibberish
while True:
    counter +=1
    ser.write(str(chr(counter)+",").encode('utf-8')) # Convert the decimal number to ASCII then send it to the Arduino
    print(ser.readline()) # Read the newest output from the Arduino
    sleep(.1) # Delay for one tenth of a second
    if counter == 255:
        counter = 32

"""
ARDUINO CODE:
void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
}
void loop() {
char inByte = ' ';
if(Serial.available()){ // only send data back if data has been sent
char inByte = Serial.read(); // read the incoming data
Serial.println(inByte); // send the data back in a new line so that it is not all one long line
}
delay(100); // delay for 1/10 of a second
}

Modified from code at:
https://www.instructables.com/Interface-Python-and-Arduino-with-pySerial/
"""
