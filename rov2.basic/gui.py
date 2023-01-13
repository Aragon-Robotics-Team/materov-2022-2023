from tkinter import *
from tkinter import ttk

import cv2 
import multiprocessing 

from PIL import Image, ImageTk 

# cap = cv2.VideoCapture(0)

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x1000")

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={
        "TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

vcol = 3

#START NAV PROCESS ------------------------------------------------------------------------------------------------------
# from subprocess import Popen


# def startNavProcess():
#     global nav 
#     nav = Popen(['python', '/Users/valeriefan/Desktop/Robotics/materov-2022-2023/rov2/exectest.py'])
#     print("asdf")
#    # exec(open('/Users/valeriefan/Desktop/Robotics/materov-2022-2023/rov2/exectest.py').read())

# B = Button(root, text ="Start Nav Process", command = startNavProcess)
# B.pack()

# def endNavProcess():
#     global nav 
#     nav.terminate()

# B = B = Button(root, text ="End Nav Process", command = startNavProcess)
# B.pack()


#START NAV PROCESS PT2 ---------------------------------------------------------------
# import subprocess 
# import os 
# import signal 
# import time 
# import queue
# import threading
# import time 

# def startNavProcess():
#     global nav 
#     nav = subprocess.Popen(['python', '/Users/valeriefan/Desktop/Robotics/materov-2022-2023/rov2/exectest.py'], stdin = subprocess.PIPE, stdout = subprocess.PIPE)

# B = Button(root, text ="Start Nav Process", command = startNavProcess)
# B.pack()

# def endNavProcess():
#     global nav 
#     nav.kill()
#     nav.communicate()

# B = Button(root, text = "End Nav Process", command = endNavProcess).pack()

#COMMUNICATING WITH SUBPROCESS ---------------------------------------------------------------

# import multiprocessing 
# import threading

# queue = multiprocessing.Queue() 
# x=0

# def sendToSubProcess():
#     global x 
#     queue.put("x")


# B = Button(root, text = "Send x++ to subprocess", command = sendToSubProcess).pack()

#START NAV PROCESS PT2 ---------------------------------------------------------------

import multiprocessing
import imp 
import exectest

from nav.teleop import teleopMain

class NavProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self): 
        teleopMain(self.input_queue, self.output_queue)
        # exectest.testMethod()

nav_in_queue = multiprocessing.Queue()
nav_out_queue = multiprocessing.Queue() 

def startNavProcess():
    global p
    p = NavProcess(nav_in_queue, nav_out_queue)
    imp.reload(exectest)
    p.start()

B = Button(root, text = "Start Nav Process", command = startNavProcess).pack()

def terminateNavProcess():
    global p
    p.terminate()

B = Button(root, text = "Terminate Nav Process", command = terminateNavProcess).pack()

#---------------------------------------------------------------

def startGUI():
    while True:
        root.update()

if __name__ == "__main__":
    root.mainloop()