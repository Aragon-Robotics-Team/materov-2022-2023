## USE CAMEL CASE GUYS 
## lower dot case for packages (e.g. java.net)
## upper camel case for classes and interfaces (e.g. WriteOperations)
## lower camel case for variables and methods (e.g. firstName)
## Screaming Snake Case for constants (e.g. INTEREST_RATE)

import multiprocessing 

from nav.teleop import teleopMain  # RPI IMPORTS
import martingui

class ThrusterProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self):
        #nav.teleop.teleopMain()
        print("running teleopMain")
        teleopMain(self.input_queue, self.output_queue)
        # print("h")
        # pygame.init()
        # print("h")
        # pygame.joystick.init()
        # p = multiprocessing.Process(target = controller.controllerStart(), args = (self.input_queue, self.output_queue, self.fish_queue))
        # p.start()

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')

    thruster_in_queue = multiprocessing.Queue()
    thruster_out_queue = multiprocessing.Queue()

    # gui.queue(thruster_in_queue, thruster_out_queue)

    #
    thruster_proc = ThrusterProcess(thruster_in_queue, thruster_out_queue)
    thruster_proc.start()
    # thruster_proc.join()
    while True:
        gui.root.update()