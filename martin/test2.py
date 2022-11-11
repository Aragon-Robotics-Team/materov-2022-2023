import serial                                           
arduino = serial.Serial('COM7', 9600)
while True:                                             
 
        servo = str(input ("Servo position: "))      
        arduino.write(servo)                          
        Yes = str(arduino.readline())           
        print(Yes)                            