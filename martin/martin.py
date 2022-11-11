from tkinter import W
import serial #imports serial libary
import time 
from turtle import end_fill


if __name__ == '__main__': # looking for main class to run
    print("Enter str:")
    number = input()
        
    arduino = serial.Serial(port='COM7', baudrate=9600, timeout=1) #connects to arduino
    # while not arduino.is_open:
    #     print("not open")
    # print("open, starting string sending")
    time.sleep(1) #sleepy joe
    
    while True: 

        #number = input()
        
        stringToSend = number + "\n" #sets stringToSend as "input" and indents
        arduino.write(stringToSend.encode("ascii")) #encodes stringToSend in American Standard Code for Information Interchange
        # data sent to arduino
        # waits for arduino to do something
        while (arduino.in_waiting == 0): #while loopie
            pass 
        recieved = arduino.readline().decode("ascii")  # sets recieved (var) as arduino read(decode) American Standard Code for Information Interchange
        print(recieved) # prints recieved
        
        time.sleep(1) #sleepy sleep sleep



        



        

