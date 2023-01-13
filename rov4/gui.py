from tkinter import *
from tkinter import ttk

import cv2 
import multiprocessing 

from PIL import Image, ImageTk 

import imp 

import nav.playground 

class GUIClass():
    def __init__(self):
        #BASIC SETUP 
        
        self.root = Tk()
        self.root.geometry("1300x1000")

        self.style =  ttk.Style()

        self.style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )

        self.style.configure('TButton', font = ('Helvetica', 13), width = 25)

        self.vcol = 3 #number of columns that the video feed, or else the video is weirdly squished for some reason 
        self.vrow = 40 #number of rows that the video feed needs to span, same reasoning as above 

        #VIDEO FEED
        
        self.cap = cv2.VideoCapture(0)

        self.videolabel = Label(self.root, height = 800, width = 1000) ##CHANGE SO THE FULL VIDEO IS SHOWN 

        self.videolabel.grid(row = 0, column = 0, rowspan = self.vrow, columnspan = self.vcol, sticky = 'n')

        #MULTIPROCESSING
        self.nav_in_queue = multiprocessing.Queue()
        self.nav_out_queue = multiprocessing.Queue() 

        StartNavB = Button(self.root, text = "Start Nav Process", command = self.startNavProcess)
        StartNavB.grid(row = 0, column = self.vcol + 1, sticky = 'n')

        EndNavB = Button(self.root, text = "Terminate Nav Process", command = self.terminateNavProcess)
        EndNavB.grid(row = 1, column = self.vcol + 1, sticky = 'n')

    def showFrames(self):
        cv2image= cv2.cvtColor(self.cap.read()[1],cv2.COLOR_BGR2RGB)
        #error is fine 
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        #error is fine
        self.videolabel.imgtk = imgtk
        self.videolabel.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        self.videolabel.after(20, self.showFrames)

    class NavProcess(multiprocessing.Process):
        def __init__(self, input_queue, output_queue):
            multiprocessing.Process.__init__(self)
            self.input_queue = input_queue
            self.output_queue = output_queue
        def run(self): 
            # teleopStart(self.input_queue, self.output_queue)
            nav.playground.teleopStart()

    def startNavProcess(self):
        global p
        p = self.NavProcess(self.nav_in_queue, self.nav_out_queue)
        imp.reload(nav.playground)
        p.start()

    def terminateNavProcess(self):
        global p
        p.terminate()
        print("nav process ended")
        
    def run(self):
        while True:
            self.root.update()


if __name__ == "__main__":
    gui = GUIClass()
    gui.showFrames()
    gui.run()
    