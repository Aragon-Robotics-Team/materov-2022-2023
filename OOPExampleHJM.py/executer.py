from Robot import *
from Teleop import Teleop
from Arduino import Arduino
from Gamepad import Gamepad

def run():  # initializes and creates Robot object
    rob = Gamepad()  # pass in the arduino, controller, queue
    #rob.run()
    # print(rob.arduino.getSerial())
    # nextTask = rob.testGamepad()
""" 
Ensures that every time each task terminates, it will always
circle back to controller.test (default starting place).
Each task (controller test, teleop, auto1, auto2) will be given the Queue so that they can Exit if
the Queue tells it to, and go back to controller.test

Controller.test is merely a place to wait for the GUI to send tasks through the Queue
Once it recieves something, it will return it, and the Loop will perform the necessary task


while True:
//receive stuff from gui
list qeuestuff
queue.recieve() =  queuestuff

        if nextTask = teleop:  # enters a loop
            teleopPeriod = Teleop(rob)
            nextTask = teleopPeriod.start()  will return the next GUI command
        else if nextTask = auto1:
            auto1 = Auto(rob)
            nextTask = auto1.start()  will return the next GUI command
        else if nextTask = auto2:
            auto2 = Auto2(rob)
            nextTask = auto2.start()  will return the next GUI command
        else if nextTask = test gamepad:
            nextTask = rob.testGamepad()  will return the next GUI command

"""

if __name__ == '__main__':
    run()
