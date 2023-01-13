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

currentx = ovalcenterx
currenty = ovalcentery

def updatePoint():
    global point 
    global currentx
    global currenty
    newx = rad*globvar.joyx + ovalcenterx
    newy = rad*globvar.joyy + ovalcentery
    c.move(point, newx - currentx, newy - currenty)
    currentx = newx
    currenty = newy
    c.after(20, updatePoint)

updatePoint()

import multiprocessing

class JiaqiSucks(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
    def run(self):
        print("running teleopMain")
        executer.run() 
        print("hi")
if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')


    obj = JiaqiSucks()
    obj.start()
    win.mainloop()
    

#win.mainloop()