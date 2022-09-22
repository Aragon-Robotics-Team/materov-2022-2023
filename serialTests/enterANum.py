import serial
import time


if __name__ == '__main__':
    arduino = serial.Serial(port='/dev/cu.usbmodem142101', baudrate=9600, timeout=1)
    # while not arduino.is_open:
    #     print("not open")
    # print("open, starting string sending")
    time.sleep(1)
    
    while True:

        stringToSend =  "input" + "\n"
        arduino.write(stringToSend.encode("ascii"))
        # data sent to arduino
        # waits for arduino to do something
        while (arduino.in_waiting == 0):
            pass
        recieved = arduino.readline().decode("ascii")  # read arduino data with timeout = 1
        print(recieved)
        
        time.sleep(1)