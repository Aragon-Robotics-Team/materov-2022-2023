from multiprocessing import Queue
from IPTesting.nav.Robot.Robot import Robot
from IPTesting.nav.Robot.MathFunc import PWM, makeString
from time import sleep


class Autonomous():
    def __init__(self, rob: Robot):
        self.rob = rob


    def begin(self):  # Main Loop of Autonomous
        while True:
            qList = self.rob.get_queue()
            whichAuto = qList[0]
            x = round(qList[1], 2)  # round vector component to 2 decimal places
            y = round(qList[2], 2)

            if whichAuto == 0:
                sendStr = self.auto1(x, y)
            elif whichAuto == 1:
                sendStr = self.auto2(x, y)

            self.rob.get_send_arduino(sendStr)  # send to Robot arduino comm function
            sleep(0.1)


    '''
    Transect Line:
    inputs: 
        x = x-component of screen vector (float)
        y = y-component of screen vector (float)
    output: 
        list of size 6: [fr, fl, br, bl, v1, v2]
    '''
    def auto1(self, x: float, y: float) -> list:
        pass


    '''
        Auto Docking:
        inputs: 
            x = x-component of screen vector (float)
            y = y-component of screen vector (float)
        output: 
            list of size 6: [fr, fl, br, bl, v1, v2]
        '''
    def auto2(self, x: float, y: float) -> list:
        pass
