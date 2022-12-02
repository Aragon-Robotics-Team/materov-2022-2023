from tkinter import *
from tkinter import ttk

import cv2 
import multiprocessing 

from PIL import Image, ImageTk 

#SETUP ------------------------------------------------------------------------------------------------------
root = Tk()
root.geometry("1300x1000")

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={
        "TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

vcol = 3 #number of columns that the video feed, or else the video is weirdly squished for some reason 
vrow = 40 #number of rows that the video feed needs to span, same reasoning as above 

#VIDEO FEED ------------------------------------------------------------------------------------------------------

cap = cv2.VideoCapture(0)

label = Label(root, height = 800, width = 1000) ##CHANGE SO THE FULL VIDEO IS SHOWN 

label.grid(row = 0, column = 0, rowspan = vrow, columnspan = vcol, sticky = 'n')

def showFrames():
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    #error is fine 
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    #error is fine
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, showFrames)

showFrames()

#START NAV PROCESS ---------------------------------------------------------------

import multiprocessing
import imp 


import nav.playground 

class NavProcess(multiprocessing.Process):
    def __init__(self, input_queue, output_queue):
        multiprocessing.Process.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
    def run(self): 
        # teleopStart(self.input_queue, self.output_queue)
        nav.playground.teleopStart()

nav_in_queue = multiprocessing.Queue()
nav_out_queue = multiprocessing.Queue() 

nav_in_queue = multiprocessing.Queue()
nav_out_queue = multiprocessing.Queue()

def startNavProcess():
    global p
    p = NavProcess(nav_in_queue, nav_out_queue)
    imp.reload(nav.playground)
    p.start()

B = Button(root, text = "Start Nav Process", command = startNavProcess)
B.grid(row = 0, column = vcol + 1, sticky = 'n')

def terminateNavProcess():
    global p
    p.terminate()

B = Button(root, text = "Terminate Nav Process", command = terminateNavProcess)
B.grid(row = 1, column = vcol + 1, sticky = 'n')

#---------------------------------------------------------------

def startGUI():
    while True:
        root.update()

if __name__ == "__main__":
    root.mainloop()