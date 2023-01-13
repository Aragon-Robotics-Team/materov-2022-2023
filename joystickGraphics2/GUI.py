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

import multiprocessing

nav_in_queue = multiprocessing.Queue()
nav_out_queue = multiprocessing.Queue() 


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
    def __init__(self, nav_in_queue, nav_out_queue):
        self.nav_in_queue = nav_in_queue
        self.nav_out_queue = nav_out_queue
        # global nav_in_queue
        # nav_in_queue = self.nav_in_queue
        # global nav_out_queue
        # nav_out_queue = self.nav_out_queue

        #Basic Setup  ----------------------- 

        self.win = tk.Tk()
        self.win.title('Joystick Graphics Test 0.1')
        self.win.geometry('400x400')

        #Joystick Canvas Setup ------------

        self.c = Canvas(self.win,width=350, height=350)
        self.c.pack()

        self.ovalcenterx = 350/2
        self.ovalcentery = 350/2

        self.rad = 150

        self.c.create_oval(self.ovalcenterx - self.rad, self.ovalcentery + self.rad, self.ovalcenterx + self.rad, self.ovalcentery - self.rad)

        self.pointRad = 5

        self.point = self.c.create_oval(self.ovalcenterx - self.pointRad, self.ovalcentery + self.pointRad, self.ovalcenterx + self.pointRad, self.ovalcentery - self.pointRad, fill="red", outline="red")

        self.joyx = 0
        self.joyy = 0 

        self.currentx = self.ovalcenterx
        self.currenty = self.ovalcentery

        #Start Joystick Loop ------------
        self.updatePoint() 

    def queuereciever(self):
        while not self.nav_out_queue.empty():
            self.joyx = self.nav_out_queue.get()[0]
            self.joyy = self.nav_out_queue.get()[1]
            # print("reading from queue")

    def updatePoint(self): 
        # global point 
        # global currentx
        # global currenty
        # global joyx 
        # global joyy
        # global rad
        # global ovalcenterx
        # global ovalcentery
        self.queuereciever()
        print(self.joyx)
        print(self.joyy)
        # print("X:" + str(joyx))
        # print("Y:" + str(joyy))
        newx = self.rad*self.joyx + self.ovalcenterx
        newy = self.rad*self.joyy + self.ovalcentery
        self.c.move(self.point, newx - self.currentx, newy - self.currenty)
        self.currentx = newx
        self.currenty = newy
        self.c.after(5, self.updatePoint)

    def run(self):
        obj = JiaqiSucks(self.nav_in_queue, self.nav_out_queue)
        obj.start()
        self.win.mainloop()
    
        
if __name__ == "__main__":

    nav_in_queue = multiprocessing.Queue()
    nav_out_queue = multiprocessing.Queue()
    gui = GUI(nav_in_queue, nav_out_queue)
    gui.run()