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

c= Canvas(self,width=350, height=300)
c.pack()

c.create_oval(60,60,300,300)
joycirclecenterx = (60+300)/2
joycirclecentery = (300 + 60)/2


#f= Canvas(self,width=9, height=9)
#f.pack()

oval = c.create_oval(10,10,5,5, fill="red", outline="red").place(x=joycirclecenterx,y=joycirclecentery)


#*draw position circle* 

def joy1graphic(): 

    
    #*change position to x + (circlesize)(globvar.joyx1), y + (circlesize)(globvar.joyy1)
    joy1graphic.after(20, showFrames)

self.mainloop()