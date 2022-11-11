import serial
class Arduino: 
    serial = 9
    def __init__(self, serial) -> None:
        self.serial = serial

    def init(self):
        arduino = serial.Serial(port='/dev/cu.usbmodem142201', baudrate=9600, timeout=3)
    def getSerial(self):
        return self.serial