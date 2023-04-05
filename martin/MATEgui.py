import tkinter as tk
from tkinter import ttk
from tkinter import *
#import pyautogui
from PIL import ImageTk, Image

import cv2 
import multiprocessing 

window = tk.Tk()
window.geometry("1400x700")

screen = Canvas(window, height = 1000, width = 500, bg="#fff")
screen.grid(row = 0, column = 0, sticky = 'n' )

screen1 = Canvas(window, height = 1000, width = 900, bg="#fff")
screen1.grid(row = 0, column = 1, sticky = 'e')

Button(screen, text='Button', command="").place(x=195, y=250)

window.mainloop()