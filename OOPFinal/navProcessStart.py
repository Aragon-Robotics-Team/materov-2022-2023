import multiprocessing 
import imp

from nav import executer

class NavProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self): 
        # teleopStart(self.input_queue, self.output_queue)
        #nav.playground.teleopStart()
        print("starting auto")
        executer.run(self.input_queue, self.output_queue)
        return 

def startNavProcess(nav_in_queue, nav_out_queue):
    global p
    p = NavProcess(nav_in_queue, nav_out_queue)
    imp.reload(executer)
    p.start()

def terminateNavProcess():
    global p
    p.terminate()
    print("nav process ended")