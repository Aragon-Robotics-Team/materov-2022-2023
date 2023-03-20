import cv2
import numpy as np
import argparse
import math

def findAngle(videoImg): 
    global image
    image = videoImg

    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50]) #doesnt produce best mask
    upper_red = np.array([10,255,255]) #doesnt produce best mask
    mask = cv2.inRange(gray_hsv, lower_red, upper_red)
    maskedImage = cv2.bitwise_and(image, image, mask=mask)
    #cv2.imshow("mask", mask)
    cv2.imshow("result", maskedImage)
    #cv2.waitKey()
    edges = cv2.Canny(maskedImage, 75, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength = 100, maxLineGap = 20)
    #lines are somewhat unreliable because the mask is spotty --> either can make range larger and hope that
    #we won't have an issue underwater or stick with countours which may not work with pool tiles


    i = 0
    rightLinePresent = False

    if lines is not None:
        for line in lines:
            if i == 0:
                leftx1, lefty1, leftx2, lefty2 = line[0]
            else:
                rightx1, righty1, rightx2, righty2 = line[0]
                if abs(rightx1 - leftx1) > 90:
                    rightLinePresent = True
                    if (rightx1 - leftx1) < 0: 
                        rightx1 = leftx1
                        rightx2 = leftx2
                        righty1 = lefty1
                        righty2 = lefty2
                        leftx1, lefty1, leftx2, lefty2 = line[0]
                    if lefty1 > lefty2:
                        leftEndX = leftx1
                        leftStartX = leftx2
                    else:
                        leftEndX = leftx2
                        leftStartX = leftx1
                break
            i += 1

        if rightLinePresent:
            cv2.line(image, (leftx1, lefty1), (leftx2, lefty2), (0, 255, 255), 10)
            cv2.line(image, (rightx1, righty1), (rightx2, righty2), (255, 255, 255), 10)
            StraightLFPWMOutput(leftEndX, leftStartX, lefty1, lefty2, videoImg)

def StraightLFPWMOutput(x1, x2, y1, y2, videoImg):
    yComponent = abs(y1-y2) 
    xComponent = x1-x2
    if x1-x2 > 0:
        angleToAdjust = -1*(math.acos(yComponent/(math.sqrt(xComponent**2 + yComponent**2))))*180/math.pi
    else:
        angleToAdjust = (math.acos(yComponent/(math.sqrt(xComponent**2 + yComponent**2))))*180/math.pi
    print(angleToAdjust)
    #NAV CODE TO ADJUST ANGLE
    lineMidpoint = (int)((x1+x2)/2)
    imageMidpoint = (int)(videoImg.shape[1])
    #if lineMidpoint > imageMidpoint:
        #NAV CODE TO MOVE LEFT/RIGHT


videoCaptureObject = cv2.VideoCapture(0)
result = True
while result:
    ret,frame = videoCaptureObject.read()
    # cv2.imshow("Capturing Video",frame)
    findAngle(frame)
    cv2.imshow("linesDetected", image)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        videoCaptureObject.release()
        result = False
        cv2.destroyAllWindows()