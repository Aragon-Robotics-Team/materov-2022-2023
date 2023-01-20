import cv2
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import time
import keyboard

snapshots = ["C:/Users/alexa/Desktop/square0.png", "C:/Users/alexa/Desktop/square1.png"]

def video():
	while True:
		videoCaptureObject = cv2.VideoCapture(0)
		i = 0
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

# lowerb = (2, 0, 0)
# upperb = (179, 255, 255)

def colorSelector(img_path):
	color_selected = np.zeros((150,150,3), np.uint8)

	global Bnum
	global Gnum
	global Rnum 

	#Mouse Callback function
	def show_color(event,x,y,flags,param): 
		global Bnum
		global Gnum
		global Rnum 

		Bnum = 0
		Gnum = 0
		Rnum = 0

		B=img[y,x][0]
		G=img[y,x][1]
		R=img[y,x][2]

		if event == cv2.EVENT_LBUTTONDOWN:
			color_selected [:] = (B,G,R)
			Bnum = B
			Gnum = G
			Rnum = R

		return

	#Show selected color when left mouse button pressed
	cv2.namedWindow('color_selected')
	cv2.resizeWindow("color_selected", 50,50);

	#image window for sample imageq
	cv2.namedWindow('image')

	#read sample image
	img=cv2.imread(img_path)

	#mouse call back function declaration
	cv2.setMouseCallback('image',show_color)
	while (1):
		cv2.imshow('image',img)
		cv2.imshow('color_selected', color_selected)
		if cv2.waitKey(1) == ord('q'):
			cv2.destroyAllWindows()
			break

	return (Bnum, Gnum, Rnum)


def mask(colorArray):

	h = colorArray[0]
	s = colorArray[1]
	v = colorArray[2]

	squareOne = cv2.imread(snapshots[0])
	hsv_squareOne = cv2.cvtColor(squareOne, cv2.COLOR_RGB2HSV)

	rgbVal = np.array(colorArray)
	rgbVal = cv2.cvtColor(rgbVal, cv2.COLOR_RGB2HSV)

	lowerb = (h - 10, s - 10, v - 10)
	upperb = (h + 10, s + 10, v + 10)

	lowerb = np.array(lowerb)
	upperb = np.array(upperb)

	mask = cv2.inRange(hsv_squareOne, lowerb, upperb)
	result = cv2.bitwise_and(squareOne, squareOne, mask=mask)

	return (lowerb, upperb, mask)




def findSquares(array):

	lowerb = array[0]
	upperb = array[1]
	mask = array[2]

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

	return (count, countAfter)

def calculator(array):

	count = array[0]
	countAfter = array[1]

	totalSquares = 64
	whiteAfter = totalSquares - countAfter
	whiteCount = totalSquares - count

	whiteDiff = whiteAfter - whiteCount
	greenDiff = countAfter - count

	if whiteDiff > greenDiff:
		return("The seagrass decreased by " + str(whiteDiff) + " white squares.")
	elif greenDiff > whiteDiff:
		return("The anchor tear recovered by " + str(greenDiff) + " green squares.")
	elif greenDiff == whiteDiff: 
		return("No change.")


#running stuff

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]

result = True
videoCaptureObject = cv2.VideoCapture(0)
while True:
	i = 0
	ret, frame = videoCaptureObject.read()
	cv2.imshow("Capturing Video", frame)
		# deletes every frame as the next one comes on, closes all windows when q is pressed
	if cv2.waitKey(1) == ord('q'):
		videoCaptureObject.release()
		cv2.destroyAllWindows()
		break
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

calculator(findSquares(mask(colorSelector("C:/Users/alexa/Desktop/square0.png"))))


