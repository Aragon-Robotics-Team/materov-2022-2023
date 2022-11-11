import globvar
#
from tkinter import *
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2 
#

self = tk.Tk()
self.title('Joystick Graphics Test 0.1')
self.geometry('400x400')

c= Canvas(self,width=350, height=350)
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

self.mainloop()