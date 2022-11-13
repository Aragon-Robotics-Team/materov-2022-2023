from time import sleep, time 
import pygame 
import serial 


def joy_tests_mac():
    # while  joyTestsOn:
    while  True:
        sleep(0.1)
        # getting latest queue status
        for event in pygame.event.get():
            # The 0 button is the 'a' button, 1 is the 'b' button, 2 is the 'x' button, 3 is the 'y' button
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                    print(event.button, "Select Has Been Pressed")
                if event.button == 1:
                    print(event.button, "Left Joystick button has been pressed")
                if event.button == 2:
                    print(event.button, "Right Joystick button has been pressed")
                if event.button == 3:
                    print(event.button, "Start has been pressed. Will exit joytests.")
                    print("statuses sent")
                if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                    print(event.button, "Triangle Has Been Pressed")
                if event.button == 13:
                    print(event.button, "Circle has been pressed")
                if event.button == 14:
                    print(event.button, "X has been pressed")
                if event.button == 15:
                    print(event.button, "Square has been pressed")
                if event.button == 16:
                    print(event.button, "Center PS has been pressed")
                    #  NonLinearLoop()
            elif event.type == pygame.JOYBUTTONUP:
                if event.button == 0:  # event.type == pygame.JOYBUTTONUP:
                    print(event.button, "Select Has Been Released")
 
                if event.button == 1:
                    print(event.button, "Left Joystick button has been released")
                if event.button == 2:
                    print(event.button, "Right Joystick button has been released")

                if event.button == 3:
                    print(event.button, "Start has been released.")

                if event.button == 12:  # event.type == pygame.JOYBUTTONUP:
                    print(event.button, "Triangle Has Been released")
                if event.button == 13:
                    print(event.button, "Circle has been released")
                if event.button == 14:
                    print(event.button, "X has been released")
                if event.button == 15:
                    print(event.button, "Square has been released")
                if event.button == 16:
                    print(event.button, "Center PS has been released")

if __name__ == '__main__':
    pygame.init()  # Initiate the pygame functions
    pygame.joystick.init()
    pygame.display.init()
    j = pygame.joystick.Joystick(0)  # Define a joystick object to read from
    j.init()  # Initiate the joystick or controller

    joy_tests_mac()