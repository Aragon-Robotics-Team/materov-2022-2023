from OOPFinal.nav.Robot.Robot import Robot
from OOPFinal.nav.Teleop.Teleop import Teleop

def run(queue_in, queue_out):  # initializes and creates Robot object

    queue = None

    rob = Robot(queue_in, queue_out)  # pass in the arduino, controller, queue
    rob.initialize()
    teleop = Teleop(rob)
    teleop.teleop_loop()


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
#receive stuff from gui

    queue_data = queue.recieve()

    if nextTask = teleop:  # enters a loop
        teleopPeriod = Teleop(rob)
        nextTask = teleopPeriod.start()
    else if nextTask = auto1:
        auto1 = Auto(rob)
        nextTask = auto1.start()
    else if nextTask = auto2:
        auto2 = Auto2(rob)
        nextTask = auto2.start()
    else if nextTask = test gamepad:
        nextTask = rob.testGamepad()
"""


if __name__ == '__main__':
    run(1, 2)
