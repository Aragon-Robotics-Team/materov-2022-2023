from multiprocessing import Queue
from IPTesting.nav.Robot.Robot import Robot
from IPTesting.nav.Robot.MathFunc import PWM, makeString


class Autonomous():
    def __init__(self, rob: Robot):
        self.rob = rob

    def begin(self):
        while True:
            qList = self.rob.get_queue()
            whichAuto = qList[0]
            x = round(qList[1], 2)
            y = round(qList[2], 2)

            if whichAuto == 0:
                sendStr = self.auto1(x, y)
            elif whichAuto == 1:
                sendStr = self.auto2(x, y)

            self.rob.get_send_arduino(sendStr)

    '''
    Transect Line auto function:
    inputs: 
        x = x-component of screen vector (float)
        y = y-component of screen vector (float)
    output: 
        list of size 6: [thruster
    '''
    def auto1(self, x: float, y: float) -> list:
        pass

    def auto2(self, x: float, y: float) -> list:
        pass
