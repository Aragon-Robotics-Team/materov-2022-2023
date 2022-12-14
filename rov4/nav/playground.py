from nav.Gamepad import Gamepad
from nav.Robot import Robot
from nav.Teleop import Teleop
from nav.Arduino import Arduino

def teleopStart():

    #arduino = Arduino(14201, 9600, 1)
    arduino = Arduino(101, 9600, 1)
    arduino.init()


    robot = Robot(1, 2, 3)
    gamepad = Gamepad(robot)
    teleop = Teleop(robot)

    gamepad.MainHandler()

# while True:
#     print(gamepad.getValueArray())