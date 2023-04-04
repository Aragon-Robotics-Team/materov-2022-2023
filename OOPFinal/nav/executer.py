from nav.Robot.Robot import Robot
from nav.Teleop.Teleop import Teleop
from nav.Autonomous.Autonomous import Autonomous


def run(queue_in, queue_out):  # initializes and creates Robot object
    rob = Robot(queue_in, queue_out)  # pass in the arduino, controller, queue
    # teleop = Teleop(rob)
    # teleop.teleop_loop()
    print("rob inititilaiezd")

    auto = Autonomous(rob)

    print("auto initilaized")
    auto.begin_and_loop()
    


if __name__ == '__main__':
    pass
