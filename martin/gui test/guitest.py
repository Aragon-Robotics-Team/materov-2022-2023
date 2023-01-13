from tkinter import *
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2 
import multiprocessing 

from PIL import Image, ImageTk 


window = tk.Tk()
window.title('Megalodon ROV GUI 0.1.0')
window.geometry('1800x900')

greeting = tk.Label(text="Megalodon ROV GUI 0.1.0").place(x=5,y=5)

def web():
    webbrowser.open("http://www.aragonrobotics.org/")

website = tk.Button(text="More info!",width=10,height=1,fg="black", command=web).place(x=150, y=3)

#EMERGENCY HALT ------------------------------------------------------------------------------------------------------------

def enableBot():
    global autoArray
    autoArray[1] = 0
    output_queue.put(autoArray)
    print ("BOT ENABLED")

startBot = Button( text = "Enable Bot", command = enableBot, width = 50, height = 2, fg = 'red', bg = 'gray').place(x=250,y=590)


def disableBot():
    global autoArray
    autoArray[1] = 1
    output_queue.put(autoArray)
    print("BOT DISABLED")

stopBot = Button( text = "Disable Bot (Emergency Halt)", command = disableBot, width = 50, height = 2, fg = 'red', bg = "gray").place(x=650,y=590)



# # # # # # # # # # # # # # # # # 

cap = cv2.VideoCapture(0)

#SETUP ------------------------------------------------------------------------------------------------------

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

vcol = 3
#VIDEO FEED ------------------------------------------------------------------------------------------------------

label = Label(window, height = 500, width = 1200) ##CHANGE SO THE FULL VIDEO IS SHOWN 

label.place(x=50,y=50)

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


#USB INPUT ------------------------------------------------------------------------------------------------------
usb = tk.Label(text="USB Input:").place(x=1138,y=5)

import os

os.system("color")

Usb = os.popen("wmic logicaldisk where drivetype=2 get description ,deviceid ,volumename").read()
print(Usb)

def check(DeviceID):
    if Usb.find(str(DeviceID)) != -1:
        print("\033[1;32mUsb is plugged")
        yes = tk.Label(text="Connected",fg="green").place(x=1195,y=5)
        input("")

    else:
        print("\033[0;31mUsb is not plugged")
        no = tk.Label(text="Disconnected",fg="red").place(x=1195,y=5)
        input("")

i = "1"
while i < "2":
    check(1)
    #check(-"DEVICE ID HERE"-)

if __name__ == "__main__":
    window.mainloop()