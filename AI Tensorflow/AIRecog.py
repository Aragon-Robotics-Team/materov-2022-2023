import cv2
import tensorflow as tf 
#import imageai.Detection
from imageai.Detection import ObjectDetection
import os

#executionPath = "C:/Users/alexa/Desktop/MATEcode"
#executionPath = os.getcwd()

executionPath = os.path.dirname(os.path.abspath(__file__))

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(executionPath, './saved_model.h5'))
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image = os.path.join(executionPath, "fish.png"), output_image_path=os.path.join(executionPath, "fishnew.jpg"))
for eachObject in detections:
    print(eachObject["name"], ":", eachObject["percentage_probability"])