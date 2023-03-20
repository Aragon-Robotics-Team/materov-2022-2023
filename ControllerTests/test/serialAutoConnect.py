import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem142401', 9600)

time.sleep(1)

#connect with arduino

#check if arduino prints back (every 5 secs or something)
#if not, attempt to reconnect 
counter = 1
timer = 5
start = time.time()
end = time.time()
isConnected = False
message = "HELLO"

#timer, ends 
while True:
    message = message.encode("ascii")
    arduino.write(message)
    received = arduino.readline().decode("ascii")

    if received == message:
        isConnected = True

    counter += 1
    end = time.time()

    if (end - start) > timer:
        end = time.time() # if 5 secs has elapsed, break out of the loop
        start = time.time() #reset timer
        
        if isConnected == False:
            #RECONNECT ARDUINO
            pass

    break



    

    

print(end-start)