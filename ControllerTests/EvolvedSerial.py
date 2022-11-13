
import serial
from time import sleep  #the sleep is supa important
import Vishal

arduino = serial.Serial('/dev/cu.usbmodem101', 9600)


while True:
    message = [] #already defined in main file
    mensaje = Vishal.makeString() #in () put the stuff you want from message
    arduino.write(str(mensaje).encode('utf-8')) 
    print(arduino.readline()) # Read the newest output from the Arduino
    
    sleep(0.1) # Delay for one tenth of a second
    

"""
-I want to take specific values from the messages array
-put them through the Vishal.py file
-arduino.write 'em
-send them back for verification
"""