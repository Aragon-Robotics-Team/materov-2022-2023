from Gamepad import Gamepad
from Robot import Robot
from Teleop import Teleop
from Arduino import Arduino

arduino = Arduino(14201, 9600, 1)
arduino.init()


robot = Robot(1, 2, 3)
gamepad = Gamepad(robot)
teleop = Teleop(robot)

gamepad.MainHandler()

# while True:
#     print(gamepad.getValueArray())