
class Teleop:
    def __init__(self, Robot) -> None:
        self.Robot = Robot

    def init(self):
        pass

    def start(self):
        print(self.Robot.arduino.getSerial())
        #start telop()

    def teleop(self):
        pass