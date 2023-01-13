import serial
import time

class Arduino:

    def __init__(self, portNum, baudRate, timeOut) -> None:
        self.portNum = portNum
        self.baudRate = baudRate
        self.timeOut = timeOut
        
    def init(self):
        self.arduino = serial.Serial(port=f'/dev/cu.usbmodem{self.portNum}', baudrate=self.baudRate, timeout=self.timeOut)
        time.sleep(1)

        # ensures a proper connection between the arduino and computer is established
        message = "Arduino Connected" + ","
        message = message.encode("ascii")
        self.arduino.write(message)

        while (self.arduino.in_waiting == 0):
            pass

        received = self.arduino.readline().decode("ascii")
        print(received)

    # REMINDER: INIT() FUNC MUST BE USED BEFORE GETTING SERIAL, AS IT IS INTIALIZED IN THE INIT() FUNC
    def getSerial(self):
        return self.arduino

arduino = Arduino(14201, 9600, 1)
arduino.init()
print(arduino.getSerial())


