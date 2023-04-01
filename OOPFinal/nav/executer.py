from OOPFinal.nav.Robot.Robot import Robot
from OOPFinal.nav.Teleop.Teleop import Teleop


def run(queue_in, queue_out):  # initializes and creates Robot object
    rob = Robot(queue_in, queue_out)  # pass in the arduino, controller, queue
    teleop = Teleop(rob)
    teleop.teleop_loop()


if __name__ == '__main__':
    pass
