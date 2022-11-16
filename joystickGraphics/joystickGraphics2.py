#from curses import window
import globvar
#
from tkinter import *
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2 

import executer

win = tk.Tk()
win.title('Joystick Graphics Test 0.1')
win.geometry('400x400')


c = Canvas(win,width=350, height=350)
c.pack()

ovalcenterx = 350/2
ovalcentery = 350/2

rad = 150

c.create_oval(ovalcenterx - rad, ovalcentery + rad, ovalcenterx + rad, ovalcentery - rad)

pointRad = 5

point = c.create_oval(ovalcenterx - pointRad, ovalcentery + pointRad, ovalcenterx + pointRad, ovalcentery - pointRad, fill="red", outline="red")

joyx = 0
joyy = 0 

currentx = ovalcenterx
currenty = ovalcentery

import multiprocessing

nav_in_queue = multiprocessing.Queue()
nav_out_queue = multiprocessing.Queue() 

def queuereciever():
    global joyx
    global joyy
    global nav_out_queue
    while not nav_out_queue.empty():
        joyx = nav_out_queue.get()[0]
        joyy = nav_out_queue.get()[1]
        print("reading from queue")

def updatePoint(): 
    global point 
    global currentx
    global currenty
    global joyx 
    global joyy
    queuereciever()
    # print("X:" + str(joyx))
    # print("Y:" + str(joyy))
    newx = rad*globvar.joyx + ovalcenterx
    newy = rad*globvar.joyy + ovalcentery
    c.move(point, newx - currentx, newy - currenty)
    currentx = newx
    currenty = newy
    c.after(20, updatePoint)

updatePoint()

#MULTIPROCESSING ---------------------------------

class JiaqiSucks(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue 
        self.output_queue = output_queue
    def run(self):
        print("running teleopMain")
        executer.run(self.input_queue, self.output_queue) 

class GUI():
    def __init__(self):
        self.nav_in_queue = multiprocessing.Queue()
        self.nav_out_queue = multiprocessing.Queue()
        global nav_in_queue
        nav_in_queue = self.nav_in_queue
        global nav_out_queue
        nav_out_queue = self.nav_out_queue

    def run(self):
        obj = JiaqiSucks(self.nav_in_queue, self.nav_out_queue)
        obj.start()
        win.mainloop()
        
if __name__ == "__main__":
    gui = GUI()
    gui.run()
    # multiprocessing.set_start_method('spawn')

    # obj = JiaqiSucks(self.nav_in_queue, self.nav_out_queue)
    # obj.start()
    # win.mainloop()
    

#win.mainloop()