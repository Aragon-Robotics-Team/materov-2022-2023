from Teleop import *
import pygame
from time import sleep

"""
Robot runs the main loop, starts the tasks such as Teleop and Autonomous
Initializes Arduino, Controller, and Tests Controller
This class is for Interfacing with the GUI. This is the MAIN PROCESS for Nav

"""
class Robot:  # Robot is a multiprocessing class process?
    def __init__(self, queue) -> None:  # gui creates object bot and interacts with it
        self.gamepad = pygame.joystick.Joystick(0)
        self.gamepad.init()
        self.arduino = None
        self.queue = queue
        self.portNum = 142101
        self.baudRate = 115200
        self.receivedData = None

    def initialize(self):

        self.arduino = serial.Serial(port=f'/dev/cu.usbmodem{self.portNum}',
                                     baudrate=self.baudRate,
                                     timeout=1)
        sleep(1)
        message = "Arduino Connected" + ","
        message = message.encode("ascii")
        self.arduino.write(message)
        while (self.arduino.in_waiting == 0):
            pass
        received = self.arduino.readline().decode("ascii")
        print(received)

        return "initialized"

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
    def get_send_arduino(self, data):
        message = ','.join(data) + '.'
        self.arduino.write(message.encode("ascii"))
        while (self.arduino.in_waiting == 0):
            pass
        self.receivedData = self.arduino.readline().decode("ascii")

    def getSerialOn(self):
        return self.arduino.getSerial()

    def startTeleop(self):
        self.teleop.teleop_loop()

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