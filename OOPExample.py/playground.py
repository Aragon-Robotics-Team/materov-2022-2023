from Gamepad import Gamepad
from Robot import Robot
from Teleop import Teleop

robot = Robot(1, 2, 3)
gamepad = Gamepad(robot)
teleop = Teleop(robot)

gamepad.MainHandler()

# while True:
#     print(gamepad.getValueArray())