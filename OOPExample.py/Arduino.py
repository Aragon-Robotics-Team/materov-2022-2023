import serial
class Arduino: 
    serial = 9
    def __init__(self, serial) -> None:
        self.serial = serial

    def getSerial(self):
        return self.serial