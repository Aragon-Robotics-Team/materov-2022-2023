import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyautogui
from PIL import ImageTk, Image

import cv2 
import multiprocessing 

class GUIClass():
    def __init__(self):
        #BASIC SETUP 
        
        window = tk.Tk()
        window.geometry("2000x1000")

        screen = Canvas(window, height = 1000, width = 500, bg="#fff")
        screen.grid(row = 0, column = 0, sticky = 'n' )

        screen1 = Canvas(window, height = 1000, width = 900, bg="#fff")
        screen1.grid(row = 0, column = 1, sticky = 'e')


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
    