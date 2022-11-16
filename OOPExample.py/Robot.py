from Arduino import Arduino
from Teleop import *
from Gamepad import *

"""
Robot runs the main loop, starts the tasks such as Teleop and Autonomous
Initializes Arduino, Controller, and Tests Controller
This class is for Interfacing with the GUI. This is the MAIN PROCESS for Nav

"""
class Robot:  # Robot is a multiprocessing class process?
    arduino = None
    def __init__(self, controllername, serialNum, queue) -> None:  # gui creates object bot and interacts with it
        self.controllername = controllername
        self.serialNum = serialNum
        self.queue = queue
        self.arduino = Arduino(serialNum)
        # self.gamepad = Gamepad(self.controllername, self.queue)

    def run(self):  # immediately runs
        self.arduino.init()
        self.gamepad.init()
        pass
    def testGamepad(self):
        while True:  
            # Ensures that every time each task terminates, it will always
            # circle back to controller.test (default starting place).
            # Each task (controller test, teleop, auto1, auto2) will be given the Queue so that they can Exit if 
            # the Queue tells it to, and go back to controller.test

            # Controller.test is merely a place to wait for the GUI to send tasks through the Queue
            # Once it recieves something, it will return it, and the Loop will perform the necessary task

            '''
            x = self.controller.test()
            if x = teleop:  # enters a loop
                self.teleop.start()
            else if x = auto1:
                self.auto1.start()
            else if x = auto2:
                self.auto2.start()
            
            '''



        ## add safeguards if things go wrong / don't initialize correctly. if so, terminate this process

    
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

    '''
    ...whatever other functions we need to interface with the GUI
    '''


if __name__ == '__main__':
    pass