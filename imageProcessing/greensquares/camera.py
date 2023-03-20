import cv2
import keyboard

result = True
videoCaptureObject = cv2.VideoCapture(0)

i = 0
while True:
	ret, frame = videoCaptureObject.read()
	cv2.imshow("Capturing Video", frame)
		# deletes every frame as the next one comes on, closes all windows when q is pressed
	if cv2.waitKey(1) == ord('q'):
		videoCaptureObject.release()   
		cv2.destroyAllWindows()
		break
		# when s is pressed
	else:
			result = False