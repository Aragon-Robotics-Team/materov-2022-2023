import multiprocessing 
import imp

import Arduino_Mega.NavLoop_Mega

class NavProcess(multiprocessing.Process):
    def __init__(self, input_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
    def run(self): 
        Arduino_Mega.NavLoop_Mega.startNavClass(self.input_queue)
        return 

def startNavProcess(nav_in_queue):
    global p
    p = NavProcess(nav_in_queue)
    imp.reload(Arduino_Mega.NavLoop_Mega)
    p.start()

def terminateNavProcess():
    global p
    p.terminate()
    print("nav process ended")