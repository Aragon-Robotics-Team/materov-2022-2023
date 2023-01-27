#IMPORTS-----------------------

#Tkinter is the GUI library 
from tkinter import *
from tkinter import ttk

#cv2 is the img processing library
import cv2 
from PIL import Image, ImageTk 

#multiprocessing is used to simultaenously run the gui loop and nav loop 
#see: https://docs.google.com/document/d/1p1qO26FKTEcZP4UgPsS2ZpZkVdvwvDSy1yENwRNjM9Y/edit?usp=sharing 
import multiprocessing 
import imp 

#NAV---------------------------
import nav.playground 

#Organize imports by each feature, e.g.: 
#---------------------
#AUTODOCKING TASK:  
#from _____ import ______
#--------------------

class GUIClass():
    def __init__(self):
        #*in the init function:
            #set up the gui
            #initialize and format all the gui entities, e.g. buttons, labels, etc.
            #initialize any variable that needs to be accessed throughout the entire class, using self.var 

        #BASIC SETUP ----------
        self.root = Tk()
        self.root.geometry("1300x1000")

        self.style =  ttk.Style()

        self.style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )

        self.style.configure('TButton', font = ('Helvetica', 13), width = 25)

        self.vcol = 3 #number of columns that the video feed, or else the video is weirdly squished for some reason 
        self.vrow = 40 #number of rows that the video feed needs to span, same reasoning as above 

        #EXAMPLE: 
        #*INSERT FEATURE* ------
        #initialize button: ButtonName = Button(self.root, text = "Button Text", command = *insert function that this button triggers*)
        #format button: ButtonName.grid(row = x, column = self.vcol + 1, sticky = 'n')
            #self.vcol + 1 ensures that the buttons are one column to the right of the video feed, regardless of how many columns the videefeed takes

        #VIDEO FEED -------------
        self.cap = cv2.VideoCapture(0)

        self.videolabel = Label(self.root, height = 800, width = 1000) ##CHANGE SO THE FULL VIDEO IS SHOWN 

        self.videolabel.grid(row = 0, column = 0, rowspan = self.vrow, columnspan = self.vcol, sticky = 'n')

        #MULTIPROCESSING -------
        self.nav_in_queue = multiprocessing.Queue()
        self.nav_out_queue = multiprocessing.Queue() 
            #you can create as many queues as you want --- for example, if you wanted a separate pipeline for the between the gui and nav about the joystick axis data
            #to put something in the queue, use self.nav_in_queue.put(*insert data*) 

        StartNavB = Button(self.root, text = "Start Nav Process", command = self.startNavProcess)
        StartNavB.grid(row = 0, column = self.vcol + 1, sticky = 'n')

        EndNavB = Button(self.root, text = "Terminate Nav Process", command = self.terminateNavProcess)
        EndNavB.grid(row = 1, column = self.vcol + 1, sticky = 'n')

    #insert functions that the buttons trigger, if the functions are not imported from other files 
    #I would recommend writing the functions that the buttons trigger in separate files, and importing them, for organization purposes
    #e.g.: autodockinginit() from the autodocking file, that includes all the other functions related to autodocking 

    #VIDEO FEED -------------
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


    #MULTIPROCESSING ----------
    # see: https://docs.google.com/document/d/1p1qO26FKTEcZP4UgPsS2ZpZkVdvwvDSy1yENwRNjM9Y/edit?usp=sharing  
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

    #EXAMPLE QUEUE RECIEVER: 
    def QueueReceiver(self):
        global statuses
        if self.nav_in_queue.empty() == False:
            statuses = self.nav_in_queue.get()
            #print("recieved from queue")
        self.root.after(10, self.QueueReceiver)

    #-----------------------
    def updateGUI(self):
        self.root.update()

    #-----------------------
    #*insert more functions below* 

if __name__ == "__main__":
    gui = GUIClass()
    gui.showFrames()
    gui.updateGUI()
    
