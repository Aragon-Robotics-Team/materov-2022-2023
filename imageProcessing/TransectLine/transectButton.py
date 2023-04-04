import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import time
import keyboard
import tkinter as tk
import tkinter as tk

from colorMaskTransect2 import findAngle
from colorMaskTransect2 import straightLFPWMOutput
from colorMaskTransect2 import colorSelector

def startTransect():
    videoCaptureObject = cv2.VideoCapture(0)
    ret,frame = videoCaptureObject.read()
    B,G,R = colorSelector(frame)
    result = True
    while result:
        ret,frame = videoCaptureObject.read()
        # cv2.imshow("Capturing Video",frame)
        findAngle(frame, B, G, R)
        cv2.imshow("linesDetected", image)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            videoCaptureObject.release()
            result = False
            cv2.destroyAllWindows()

root = tk.Tk()
run = tk.Button(text = "Transect Line", command = startTransect).pack()

root.mainloop()