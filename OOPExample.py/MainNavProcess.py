from cProfile import run
from Robot import *

class MainNavProcess:  # this would be the process that the gui starts
    def __init__(self) -> None:
        megalobob = Robot("joystick", "123123123")  # make new robot

        if(megalobob.run()):  # if everything is initialized correctly (something like a timeout)
            pass
            # run

        else:  # if there is a problem
            # terminate process

            pass

    def run():
        '''
        Loop:
            - get gui commands
            - call respective functions
        - 

        '''


        #  if button is pressed:

        Megalodon = Robot()  # make new robot
        Megalodon.run()  # start new robot

        #  if teleop button is pressed: 
        Megalodon.startTeleop()

        #  if auto button is pressed: 
        Megalodon.startAuto()


if __name__ == '__main__':
    pass