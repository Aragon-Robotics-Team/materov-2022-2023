import pygame
from time import sleep
import serial
from multiprocessing import Queue


"""
Robot runs the main loop, starts the tasks such as Teleop and Autonomous
Initializes Arduino, Controller, and Tests Controller
This class is for Interfacing with the GUI. This is the MAIN PROCESS for Nav

"""
class Robot:  # Robot is a multiprocessing class process?

    def __init__(self, queue_in: Queue, queue_out: Queue) -> None:  # gui creates object bot and interacts with it
        # self.gamepad = pygame.joystick.Joystick(0)
        # self.gamepad.init()
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.portNum = 142101
        self.baudRate = 115200
        self.receivedData = None
        self.delay = 0.1
        self.arduino = serial.Serial(port=f'/dev/cu.usbmodem{self.portNum}',
                                     baudrate=self.baudRate,
                                     timeout=1)
        sleep(0.5)

    def get_send_arduino(self, ls: list):
        sendStr = (str(ls[0]) + "-" +
                   str(ls[1]) + "=" +
                   str(ls[2]) + "+" +
                   str(ls[3]) + "*" +
                   str(ls[4]) + "," +
                   str(ls[5]) + ".")
        self.arduino.write(sendStr.encode("ascii"))  # write (output) to arduino
        while self.arduino.in_waiting == 0:
            pass
        self.receivedData = self.arduino.readline()  # read input from arduino

        # self.arduino.reset_input_buffer()  # clear the input buffer
        # self.arduino.reset_output_buffer()  # clear the output buffer
        # return self.receivedData.decode("ascii")

    def get_queue(self):
        return self.queue_in.get()


if __name__ == '__main__':
    pass