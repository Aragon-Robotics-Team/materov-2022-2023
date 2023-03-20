from tkinter import *
from tkinter import ttk

import cv2

from PIL import Image, ImageTk 


from autodock1 import autodockinit
from autodock1 import autodocking
from autodock1 import autodockingloop

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

        #AUTO DOCKING

        self.AutoDockInitB = Button(self.root, text = "Initialize Auto Docking", command = lambda: autodockinit(self.snapshot()))
    
        self.AutoDockInitB.grid(row = 1, column = self.vcol + 1, sticky = 'n')

        self.AutoDockingB = Button(self.root, text = "Auto Docking Single Frame", command = lambda: autodocking("/Users/valeriefan/Desktop/videosnapshot.png"))

        self.AutoDockingB.grid(row = 2, column = self.vcol + 1, sticky = 'n')

        self.AutoDockingB = Button(self.root, text = "Auto Docking Live", command = lambda: autodockingloop(self.cap))

        self.AutoDockingB.grid(row = 3, column = self.vcol + 1, sticky = 'n')


    #VIDEO FEED
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

    def snapshot(self):
        cv2.imwrite("/Users/valeriefan/Desktop/MATE ROV 2023 /videosnapshot.png", self.cap.read()[1])
        return("/Users/valeriefan/Desktop/MATE ROV 2023 /videosnapshot.png") 
      
    def run(self):
        while True:
            self.root.update()

if __name__ == "__main__":
    gui = GUIClass()
    gui.showFrames()
    gui.run()
    