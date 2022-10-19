from cProfile import run
from Robot import *

class MainNavProcess:
    def __init__(self) -> None:
        Megalodon = Robot()  # make new robot
        
        if(Megalodon.init()):  # if everything is initialized correctly
            pass
            # run

        else:  # if there is a problem
            # terminate process

            pass

    def run():
        '''
        Loop:
            - get gui commands
            - 

        '''


        #  if button is pressed:

        Megalodon = Robot()  # make new robot
        Megalodon.init()  # start new robot

        #  if teleop button is pressed: 
        Megalodon.startTeleop()

        #  if auto button is pressed: 
        Megalodon.startAuto()


if __name__ == '__main__':
    pass