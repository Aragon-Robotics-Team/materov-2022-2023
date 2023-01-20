import numpy as np 
import imutils
import cv2 
from colorpickerfunc import colorSelector

B = 0
G = 0
R = 0

def autodockinit(img_path):
    global B, G, R
    B,G,R = colorSelector(img_path)

# cv2.imshow("Image", image)
# cv2.waitKey()