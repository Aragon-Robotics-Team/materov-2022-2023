
# import required library
import webbrowser
from tkinter import *

#########################################

import tkinter as tk
from tkinter import ttk

#import glob 

import cv2 
import multiprocessing 

from PIL import Image, ImageTk 

cap = cv2.VideoCapture(0)

#SETUP ------------------------------------------------------------------------------------------------------
window = tk.Tk()
window.geometry("1300x1000")

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

vcol = 3
#VIDEO FEED ------------------------------------------------------------------------------------------------------

label = Label(window, height = 800, width = 1000) ##CHANGE SO THE FULL VIDEO IS SHOWN 

label.grid(row = 1, column = 0, rowspan = 40, columnspan = vcol, sticky = 'n')

def showFrames():
    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image = img)
    label.imgtk = imgtk
    label.configure(image=imgtk)
    # Repeat after an interval to capture continiously
    label.after(20, showFrames)

showFrames()

window.mainloop()

if __name__ == "__main__":
    window.mainloop()

    