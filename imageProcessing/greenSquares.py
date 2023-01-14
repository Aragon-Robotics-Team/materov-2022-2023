import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import time
import keyboard

snapshots = ["C:/Users/alexa/Desktop/square0.png", "C:/Users/alexa/Desktop/square1.png"]

videoCaptureObject = cv2.VideoCapture(1)
result = True
i = 0
while result:
    ret, frame = videoCaptureObject.read()
    cv2.imshow("Capturing Video", frame)
    # deletes every frame as the next one comes on, closes all windows when q is pressed
    if cv2.waitKey(1) == ord('q'):
        videoCaptureObject.release()
        cv2.destroyAllWindows()
    # when s is pressed
    if keyboard.is_pressed('s'):
        # and the index is less than the length of the snapshot list
        if i < 2:
            # take as snapshot, save it, show it
            cv2.imwrite(snapshots[i], frame)
            cv2.imshow(snapshots[i], frame)
            time.sleep(1)
            i += 1
        else:
            result = False

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

squareOne = cv2.imread(snapshots[0])
# squareOne = cv2.imread("C:/Users/alexa/Desktop/green1.png")
hsv_squareOne = cv2.cvtColor(squareOne, cv2.COLOR_RGB2HSV)

# lowerb = (2, 0, 0)
# upperb = (179, 255, 255)

lowerb = (0,0,0)
upperb = (179, 255, 190)

mask = cv2.inRange(hsv_squareOne, lowerb, upperb)
result = cv2.bitwise_and(squareOne, squareOne, mask=mask)

totalSquares = 64

# plt.subplot(1,2,1)
# plt.imshow(mask, cmap="gray")
# plt.subplot(1,2,2)
# plt.imshow(result)
# plt.show()

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

count = 0
      
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(mask, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(imageFrame, "Green", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
        count += 1


cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
cv2.waitKey(0)


squareTwo = cv2.imread(snapshots[1])
# squareTwo = cv2.imread("C:/Users/alexa/Desktop/square2.png")
hsv_squareTwo = cv2.cvtColor(squareTwo, cv2.COLOR_RGB2HSV)

mask = cv2.inRange(hsv_squareTwo, lowerb, upperb)
result = cv2.bitwise_and(squareTwo, squareTwo, mask=mask)

contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

countAfter = 0
      
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(mask, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(imageFrame, "Green", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
        countAfter += 1

whiteAfter = totalSquares - countAfter
whiteCount = totalSquares - count

whiteDiff = whiteAfter - whiteCount
greenDiff = countAfter - count

if whiteDiff > greenDiff:
    print("The seagrass decreased by " + str(whiteDiff) + " white squares.")
elif greenDiff > whiteDiff:
    print("The anchor tear recovered by " + str(greenDiff) + " green squares.")
elif greenDiff == whiteDiff: 
    print("No change.")
# pixel_colors = squareOne.reshape((np.shape(squareOne)[0]*np.shape(squareOne)[1], 3))
# norm = colors.Normalize(vmin=-1.,vmax=1.)
# norm.autoscale(pixel_colors)
# pixel_colors = norm(pixel_colors).tolist()


# h, s, v = cv2.split(hsv_squareOne)
# fig = plt.figure()
# axis = fig.add_subplot(1, 1, 1, projection = "3d")

# axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors = pixel_colors, marker=".")
# axis.set_xlabel("Hue")
# axis.set_ylabel("Saturation")
# axis.set_zlabel("Value")

# plt.show()