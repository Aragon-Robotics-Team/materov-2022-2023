import serial
class Arduino: 
    serial = 9
    def __init__(self, serial) -> None:
        self.serial = serial

    def init(self):
        pass

    def getSerial(self):
        return self.serial