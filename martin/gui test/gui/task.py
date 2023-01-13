import tkinter as tk
from tkinter import ttk
from tkinter import *

window = tk.Tk()
window.geometry("1300x1000")

taskcanvas = Canvas(window, height = 600, width = 300, bg="#fff")
taskcanvas.grid(row = 0, column = 2, sticky = 'e')

task1text = "TASK 1 - 100 points \n \nReplace a damaged section of an inter-array cable: \n \nVisual inspection - 5 points \n \nCut cable on both sides of damaged section - 10 points \n \nRemove damaged section by pulling the metal connectors off - 5 points \n \nInstall new cable section - 10 points \n \nSecure the new section with 2 (each) connectors by pushing it sideways - 10 points \n \nReplacing a damaged buoyancy module on an inter-array cable of a floating offshore wind turbine: \n \n Turn the clamp upright and remove from water - 10 points \n \nPut on new clamp facing down - 10 points \n \nMonitor the environment: \n \nDeploy the hydrophone in the box and wait 5 mins till recovery - 10 points \n \nPull pin and remove net from water - 15 points \n \nDrive the bot into the box - 5 or 15 points"

task2text = "e"

task3text = "ee"

task4text = "eee"

task5text = "eeee"

text = "test"


def task1():
    text = task1text
    user_name = Label(window,text = text).place(x = 40,y = 60)

def task2():
    text = task2text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

def task3():
    text = task3text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

def task4():
    text = task4text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

def task5():
    text = task5text
    user_name = Label(window,text = text).place(x = 40,y = 60) 

######################################################

Bu = Button(taskcanvas, text = "Task 1", command = task1).place(x= 30, y= 10)

Bu = Button(taskcanvas, text = "Task 2", command = task2).place(x= 95,y= 10)

Bu = Button(taskcanvas, text = "Task 3", command = task3).place(x= 165,y= 10)

Bu = Button(taskcanvas, text = "Task 4", command = task4).place(x= 230,y= 10)

# pack the text-Aera in the window
window.mainloop()
