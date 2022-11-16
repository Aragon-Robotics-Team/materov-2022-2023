import MathFunc
from Gamepad import Gamepad

class Teleop:
    def __init__(self, Robot) -> None:
        self.Robot = Robot
        self.Gamepad = Gamepad(Robot)

    def init(self):
        pass

    def start(self):
        print(self.Robot.arduino.getSerial())
        #start telop()

    def teleop(self):
        teleop = True

        while teleop:
            
            valueArray = self.Gamepad.getValueArray()
            Lx = valueArray[0] 
            Ly = valueArray[1]
            Rx = valueArray[3]
            A = valueArray[6]
            B = valueArray[7]

            stringToSend = MathFunc.makeString(Lx, Ly, Rx, A, B)


