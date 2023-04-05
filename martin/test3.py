# Import the required libraries
from tkinter import *
import tkinter as tk

# Create an instance of tkinter frame or window
window=tk.Tk()

# Set the size of the tkinter window
window.geometry("700x350")

# Create a canvas widget
canvas=Canvas(window, width=500, height=300)
canvas.pack()

# Add a line in canvas widget
canvas.create_line(100,200,200,35, fill="black", width=5)

window.mainloop()