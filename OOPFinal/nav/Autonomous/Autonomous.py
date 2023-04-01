from multiprocessing import Queue
from OOPFinal.nav.Robot.Robot import Robot
from OOPFinal.nav.Robot.MathFunc import PWM, makeString
from time import sleep


class Autonomous():
    def __init__(self, rob: Robot):
        self.rob = rob

    def begin_and_loop(self):  # Main Loop of Autonomous
        while True:
            qList = self.rob.get_queue()
            whichAuto = qList[0]
            x = round(qList[1], 2)  # round vector component to 2 decimal places
            y = round(qList[2], 2)

            if whichAuto == 0:  # exit autonomous
                break
            if whichAuto == 1:
                sendStr = self.transectLine(x, y)
            elif whichAuto == 2:
                sendStr = self.autoDocking(x, y)

            self.rob.get_send_arduino(sendStr)  # send to Robot arduino comm function
            sleep(self.rob.delay)


    '''
    Transect Line:
    inputs: 
        x = x-component of screen vector (float)
        y = y-component of screen vector (float)
    output: 
        list of size 6: [fr, fl, br, bl, v1, v2]
    '''
    def transectLine(self, x: float, y: float) -> list:
        pass


    '''
        Auto Docking:
        inputs: 
            x = x-component of screen vector (float)
            y = y-component of screen vector (float)
        output: 
            list of size 6: [fr, fl, br, bl, v1, v2]
        '''
    def autoDocking(self, x: float, y: float) -> list:
        pass
