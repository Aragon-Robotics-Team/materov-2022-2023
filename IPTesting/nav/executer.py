from IPTesting.nav.Robot.Robot import Robot
from IPTesting.nav.Autonomous.Autonomous import Autonomous


def run(queue_in, queue_out):  # initializes and creates Robot object
    rob = Robot(queue_in, queue_out)
    auto = Autonomous(rob)
    auto.beginAndLoop()
