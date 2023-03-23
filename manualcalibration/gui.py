#THERE SHOULD BE NO FUNCTIONS BESIDES THE INIT, RUN, AND MAIN FUNCTION IN THIS FOLDER
#there should only be imports and tk functions in this folder that call imported functions 

#---------------------------------------
#basic gui imports
from tkinter import *
from tkinter import ttk

#multiprocessing
import multiprocessing 
import navProcessStart

class GUIClass:
    def __init__(self):
        #basic setup 
        self.root = Tk()
        self.root.geometry("1300x1000")

        #styling
        self.style =  ttk.Style()
        self.style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )
        self.style.configure('TButton', font = ('Helvetica', 13), width = 25)
        self.vcol = 3 #number of columns that the video feed, or else the video is weirdly squished for some reason 
        self.vrow = 40 #number of rows that the video feed needs to span, same reasoning as above 

        #multiprocessing
        self.nav_in_queue = multiprocessing.Queue()

        StartNavB = Button(self.root, text = "Start Nav Process", command = lambda: navProcessStart.startNavProcess(self.nav_in_queue))
        StartNavB.pack()

        EndNavB = Button(self.root, text = "Terminate Nav Process", command = navProcessStart.terminateNavProcess)
        EndNavB.pack()

        #sliders
        self.br = DoubleVar(self.root, value = 5)
        self.bl = DoubleVar(self.root, value = 5)
        self.fr = DoubleVar(self.root, value = 5)
        self.fl = DoubleVar(self.root, value = 5)
        self.vr = DoubleVar(self.root, value = 5)
        self.vl = DoubleVar(self.root, value = 5)

        Label(self.root, text = "_________________________________").pack()
        Label(self.root, text = "Back Right").pack()
        BRight = Scale(self.root, variable = self.br, from_ = 0, to = 10, orient = HORIZONTAL)
        BRight.pack()
        Label(self.root, text = "_________________________________").pack()

        Label(self.root, text = "Back Left").pack()
        BLeft = Scale(self.root, variable = self.bl, from_ = 0, to = 10, orient = HORIZONTAL)
        BLeft.pack()
        Label(self.root, text = "_________________________________").pack()

        Label(self.root, text = "Front Right").pack()
        FRight = Scale(self.root, variable = self.fr, from_ = 0, to = 10, orient = HORIZONTAL)
        FRight.pack()
        Label(self.root, text = "_________________________________").pack()

        Label(self.root, text = "Front Left").pack()
        FLeft = Scale(self.root, variable = self.fl, from_ = 0, to = 10, orient = HORIZONTAL)
        FLeft.pack()
        Label(self.root, text = "_________________________________").pack()

        Label(self.root, text = "Vertical Right").pack()
        VRight = Scale(self.root, variable = self.vr, from_ = 0, to = 10, orient = HORIZONTAL)
        VRight.pack()
        Label(self.root, text = "_________________________________").pack()

        Label(self.root, text = "Vertical Left").pack()
        VLeft = Scale(self.root, variable = self.vl, from_ = 0, to = 10, orient = HORIZONTAL)
        VLeft.pack()
        Label(self.root, text = "_________________________________").pack()

        
        self.sendThroughQueue([0,0,0,0,0,0])
        #----------------

    def run(self):
        while True:
            self.root.update()

    def sendThroughQueue(self, old_coeffs):
        #send through queue
        self.coeffs = [self.br.get(), self.bl.get(), self.fr.get(), self.fl.get(), self.vr.get(), self.vl.get()]
        self.nav_in_queue.put(self.coeffs)

        #loop every 20 ms
        self.root.after(20, lambda: self.sendThroughQueue(self.coeffs))

    def GUIloop(self):
        while True: 
            self.root.update()
            # self.sendThroughQueue()
    

if __name__ == "__main__":
    gui = GUIClass()
    gui.GUIloop()