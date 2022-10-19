from Arduino import *
from Controller import *
from Teleop import *

'''
This class is for Interfacing with the GUI. This is the MAIN PROCESS for Nav
'''

class Robot:  # Robot is a multiprocessing class process?
    def __init__(self, controllername, serialNum) -> None:  # gui creates object bot and interacts with it
        self.controllername = controllername
        self.serialNum = serialNum
        self.arduino = Arduino(serialNum)
        self.controller = Controller(controllername)
        self.teleop = Teleop(self.controller)

    def run(self):  # immediately runs
        self.controller.init()  # controller test
        self.arduino.init()
        self.teleop.init(self.controller)
        
        ## add safeguards if things go wrong / don't initialize correctly. terminate this process

    '''
    ...whatever other functions we need to interface with the GUI
    '''
    
    def getArduinoStatus(self):
        pass

    def getSerialOn(self):
        return self.arduino.getSerial()

    def startTeleop(self):
        self.teleop.start()

    def endTeleop(self):
        pass

    def startAuto(self):
        pass

    def terminate1(self):
        # self.process.terminate() ??
        pass