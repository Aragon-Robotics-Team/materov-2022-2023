from multiprocessing import Queue
from OOPFinal.nav.Robot.Robot import Robot

class Autonomous1():
    def __init__(self, rob: Robot):
        self.rob = rob

    def begin(self):
        while True:
            qList = self.rob.get_queue()
            whichAuto = qList[0]
            x = round(qList[1], 2)
            y = round(qList[2], 2)

            if whichAuto == 0:
                self.auto1(x, y)
            elif whichAuto == 1:
                self.auto2(x, y)

            self.rob.


    def auto1(self, x: float, y: float):
        pass
    def auto2(self, x: float, y: float):
        pass