import cv2
import time
import keyboard
import tkinter as tk

#Press the button to start the program
#Press s to take as many photos as you want

def takePhotos():
    videoCaptureObject = cv2.VideoCapture(0)

    i = 0
    while True:
        ret, frame = videoCaptureObject.read()
        cv2.imshow("Capturing Video", frame)
            # deletes every frame as the next one comes on, closes all windows when q i`s pressed
        if cv2.waitKey(1) == ord('q'):
            videoCaptureObject.release()
            cv2.destroyAllWindows()
            break
                # when s is pressed
        if cv2.waitKey(1) == ord('s'):
            # and the index is less than txhe length of the snapshot list
            # take as snapshot, save it, show it
            #/Users/valeriefan/Desktop/materovip/{i}.png  
            cv2.imwrite(f"/Users/valeriefan/Desktop/materovip/{i}.png", frame)
            cv2.imshow(f"/Users/valeriefan/Desktop/materovip/{i}.png", frame)
            
            # cv2.imwrite(f"C://Users//alexa//Desktop//potos//picture//{i}.png", frame)
            # cv2.imshow(f"C://Users//alexa//Desktop//potos//picture//{i}.png", frame)
            cv2.waitKey(0)
            i += 1
        else:
            result = False
    

    

root = tk.Tk()
run = tk.Button(text="Start Photo Taking", command=takePhotos).pack()

root.mainloop()