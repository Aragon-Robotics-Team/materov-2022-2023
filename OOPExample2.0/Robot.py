import pygame
from time import sleep
import serial


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

    def initialize(self):  # initiates serial connection and "handshakes" with arduino

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
        # do later
        pass

    def get_send_arduino(self, string):
        self.arduino.write(string.encode("ascii"))

        # not sure if this line is needed
        while self.arduino.in_waiting == 0:
            pass

        self.receivedData = self.arduino.readline().decode("ascii")
        # return self.receivedData

        while self.arduino.in_waiting != 0:
            self.receivedData = self.arduino.readline().decode("ascii")
        return self.receivedData

    def make_string(self, list):
        return ','.join(list) + ','


if __name__ == '__main__':
    pass