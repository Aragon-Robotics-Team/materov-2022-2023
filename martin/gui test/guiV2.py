import tkinter as tk
from tkinter import ttk
from tkinter import *
import pyautogui
from PIL import ImageTk, Image

import cv2 
import multiprocessing 

window = tk.Tk()
window.geometry("2000x1000")

screen = Canvas(window, height = 1000, width = 500, bg="#fff")
screen.grid(row = 0, column = 0, sticky = 'n' )

screen1 = Canvas(window, height = 1000, width = 900, bg="#fff")
screen1.grid(row = 0, column = 1, sticky = 'e')
#

# Define a function to take the screenshot
def take_screenshot():
    x = 0
    y = 0
    # Take the screenshot in the given corrds
    im1 = pyautogui.screenshot(region=(x, y, 2000, 1000)) #make it your screensize

    # Create a toplevel window
    top = Toplevel(screen)
    im1 = ImageTk.PhotoImage(im1)

    # Add the image in the label widget
    image1 = Label(top, image=im1)
    image1.image = im1
    image1.place(x=0, y=0)

Button(screen, text='Take ScreenShot', command=take_screenshot).place(x=175, y=0)

#
Button(screen, text='Button2', command=take_screenshot).place(x=195, y=50)
Button(screen, text='Button3', command=take_screenshot).place(x=195, y=100)
Button(screen, text='Button4', command=take_screenshot).place(x=195, y=150)
Button(screen, text='Button5', command=take_screenshot).place(x=195, y=200)
Button(screen, text='Button6', command=take_screenshot).place(x=195, y=250)
#

screen2 = Canvas(window, height = 1000, width = 500, bg="#fff")
screen2.grid(row = 0, column = 2, sticky = 'n' )

task1text = "TASK 1 - 100 points \n \nReplace a damaged section of an inter-array cable: \n \nVisual inspection - 5 points \n \nCut cable on both sides of damaged section - 10 points \n \nRemove damaged section by pulling the metal connectors off - 5 points \n \nInstall new cable section - 10 points \n \nSecure the new section with 2 (each) connectors by pushing it sideways - 10 points \n \nReplacing a damaged buoyancy module on an inter-array cable of a floating offshore wind turbine: \n \n Turn the clamp upright and remove from water - 10 points \n \nPut on new clamp facing down - 10 points \n \nMonitor the environment: \n \nDeploy the hydrophone in the box and wait 5 mins till recovery - 10 points \n \nPull pin and remove net from water - 15 points \n \nDrive the bot into the box - 5 or 15 points"

task2text = "e"

task3text = "ee"

task4text = "eee"

task5text = "eeee"

text = "test"


def task1():
    text = task1text
    user_name = Label(window,text = text).place(x = 900,y = 60)

def task2():
    text = task2text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

def task3():
    text = task3text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

def task4():
    text = task4text
    user_name = Label(screen2,text = text).place(x = 40,y = 60) 

######################################################

Bu = Button(screen2, text = "Task 1", command = task1).place(x= 75, y= 10)

Bu = Button(screen2, text = "Task 2", command = task2).place(x= 175,y= 10)

Bu = Button(screen2, text = "Task 3", command = task3).place(x= 275,y= 10)

Bu = Button(screen2, text = "Task 4", command = task4).place(x= 375,y= 10)

# pack the text-Aera in the window

#EMERGENCY HALT ------------------------------------------------------------------------------------------------------------

def enableBot():
    global autoArray
    autoArray[1] = 0
    output_queue.put(autoArray)
    print ("BOT ENABLED")

startBot = Button(screen1, text = "Enable Bot", command = enableBot, width = 40, height = 2, fg = 'red', bg = 'gray').place(x=475,y=865)

def disableBot():
    global autoArray
    autoArray[1] = 1
    output_queue.put(autoArray)
    print("BOT DISABLED")

stopBot = Button(screen1, text = "Disable Bot (Emergency Halt)", command = disableBot, width = 40, height = 2, fg = 'red', bg = "gray").place(x=25,y=865)

# # # # # # # # # # # # # # # # # 

#VIDEO FEED ------------------------------------------------------------------------------------------------------

videolabel = Label(screen1, height = 800, width = 1000) ##CHANGE SO THE FULL VIDEO IS SHOWN 
videolabel.grid(row = 0, column = 0, sticky = 'n')

cap = cv2.VideoCapture(0)

def showFrames():
        cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
        #error is fine 
        img = Image.fromarray(cv2image)
        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image = img)
        #error is fine
        videolabel.imgtk = imgtk
        videolabel.configure(image=imgtk)
        # Repeat after an interval to capture continiously
        videolabel.after(20, showFrames)


showFrames()

window.mainloop()

if __name__ == "__main__":
    window.mainloop()

#USB INPUT ------------------------------------------------------------------------------------------------------
usb = tk.Label(screen1, text="USB Input:").place(x=725,y=5)

import os

os.system("color")

Usb = os.popen("wmic logicaldisk where drivetype=2 get description ,deviceid ,volumename").read()
print(Usb)

def check(DeviceID):
    if Usb.find(str(DeviceID)) != -2: #MAKE SURE TO PUT IN URS OTHERWISE NO WORK
        print("\033[1;32mUsb is plugged")
        yes = tk.Label(screen1, text="Connected",fg="green").place(x=810,y=5)
        input("")

    else:
        print("\033[0;31mUsb is not plugged")
        no = tk.Label(screen1, text="Disconnected",fg="red").place(x=810,y=5)
        input("")

i = "1"
while i < "2":
    check(1)
    #check(-"DEVICE ID HERE"-)

if __name__ == "__main__":
    print("hi yay stfu")
    #window.mainloop()