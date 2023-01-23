import pygame
from time import sleep
pygame.init()
pygame.joystick.init()
pygame.display.init()

while True:
    print("not detected")
    pygame.event.get()
    if pygame.joystick.get_count() > 0:
        break

controller = pygame.joystick.Joystick(0)
controller.init()
print("Controller name:" + controller.get_name())

while True:
    pygame.event.pump()

    sleep(0.3)
    for event in pygame.event.get():
                    # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
                    if event.type == pygame.JOYBUTTONDOWN:
                        if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                            print(event.button, "X Has Been Pressed")
                        if event.button == 1:
                            print(event.button, "Circle has been pressed")
                        if event.button == 2:
                            print(event.button, "Triangle has been pressed")
                        if event.button == 3:
                            print(event.button, "Square has been pressed.")
                        if event.button == 4:
                            print(event.button, "Surface left button has been pressed")
                        if event.button == 5:
                            print(event.button, "Surface right button has been pressed")
                        if event.button == 6:
                            print(event.button, "Surface Bottom Has Been Pressed")
                        if event.button == 7:
                            print(event.button, "Surface left button has been pressed")
                        if event.button == 8:
                            print(event.button, "Share has been pressed")
                        if event.button == 9:
                            print(event.button, "Start has been pressed. will start linear teleop")
                        if event.button == 10:
                            print(event.button, "PS Center has been pressed. will start NON linear teleop")
                        if event.button == 11:
                            print(event.button, "Left joystick has been pressed")
                        if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                            print(event.button, "Right joystick Has Been Pressed")
                        if event.button == 13:
                            print(event.button, "cross top")
                        if event.button == 14:
                            print(event.button, "cross bottom")
                        if event.button == 15:
                            print(event.button, "cross left")
                        if event.button == 16:
                            print(event.button, "cross right")
                    elif event.type == pygame.JOYAXISMOTION:
                        if event.axis == 0 and abs(controller.get_axis(0)) > 0.2:
                            zero = controller.get_axis(0)
                            print('0 has been moved ' + str(zero))
                        if event.axis == 1 and abs(controller.get_axis(1)) > 0.2:
                            one = controller.get_axis(1)
                            print('1 has been moved ' + str(one))
                        if event.axis == 2 and abs(controller.get_axis(2)) > 0.2:
                            two = controller.get_axis(2)
                            print('Top Left trigger axis has been moved ' + str(two))
                        if event.axis == 3 and abs(controller.get_axis(3)) > 0.2:
                            three = controller.get_axis(3)
                            print('3 has been moved ' + str(three))
                        if event.axis == 4 and abs(controller.get_axis(4)) > 0.2:
                            four = controller.get_axis(4)
                            print('4 has been moved ' + str(four))
                        if event.axis == 5 and abs(controller.get_axis(5)) > 0.2:
                            five = controller.get_axis(5)
                            print('5 has been moved ' + str(five))  # right trigger axis
                        if event.axis == 6 and abs(controller.get_axis(6)) > 0.2:
                            six = controller.get_axis(6)
                            print('6 has been moved ' + str(six))
                        if event.axis == 7 and abs(controller.get_axis(7)) > 0.2:
                            seven = controller.get_axis(7)
                            print('7 has been moved ' + str(seven))
    pygame.event.clear()
                # self.queuereciever()
    # lx = 0
    # ly = 1
    # rx = 3
    # ry = 4