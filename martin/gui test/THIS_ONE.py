from tkinter import *
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
import cv2 
import multiprocessing 

from PIL import Image, ImageTk 

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.title('Megalodon ROV GUI 0.1.0')
window.geometry(f'{screen_width}x{screen_height}')

print(screen_width)
print(screen_height)

greeting = tk.Label(text="Megalodon ROV GUI 0.1.0").place(x=5,y=5)

def web():
    webbrowser.open("http://www.aragonrobotics.org/")

website = tk.Button(text="More info!",width=10,height=1,fg="black", command=web).place(x=150, y=3)

screen = Canvas(window, height = screen_height, width = 0.25*screen_width, bg="#fff")
screen.grid(row = 0, column = 0, sticky = 'n' )

button1 = tk.Button(text="GUI",width=50,height=2,fg="black", command=web).place(x=0.1*screen_width, y=0.1*screen_height)
button2 = tk.Button(text="GUI",width=10,height=1,fg="black", command=web).place(x=0, y=0)

#
Button(screen, text='Button2', command=web).place(x=195, y=50)
Button(screen, text='Button3', command=web).place(x=195, y=100)
Button(screen, text='Button4', command=web).place(x=195, y=150)
Button(screen, text='Button5', command=web).place(x=195, y=200)
Button(screen, text='Button6', command=web).place(x=195, y=250)
#

#EMERGENCY HALT ------------------------------------------------------------------------------------------------------------

def enableBot():
    global autoArray
    autoArray[1] = 0
    output_queue.put(autoArray)
    print ("BOT ENABLED")

def disableBot():
    global autoArray
    autoArray[1] = 1
    output_queue.put(autoArray)
    print("BOT DISABLED")

startBot = Button( text = "Enable Bot", command = enableBot, width = 50, height = 2, fg = 'green', bg = 'gray').place(x=0.1*screen_width, y=0.1*screen_height)

stopBot = Button( text = "Disable Bot (Emergency Halt)", command = disableBot, width = 50, height = 2, fg = 'red', bg = "gray").place(x=.75*screen_width,y = .25*screen_height)

# # # # # # # # # # # # # # # # # 

cap = cv2.VideoCapture(0)

#SETUP ------------------------------------------------------------------------------------------------------

style =  ttk.Style()

style.theme_create( "button-center", parent="alt", settings={"TButton": {"configure": {"anchor": "center"}}} )

style.configure('TButton', font = ('Helvetica', 13), width = 25)

vcol = 3
#VIDEO FEED ------------------------------------------------------------------------------------------------------
e = int(screen_width*0.5)

label = Label(window, height = 500, width = e) ##CHANGE SO THE FULL VIDEO IS SHOWN 

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

##

if __name__ == "__main__":
    window.mainloop()