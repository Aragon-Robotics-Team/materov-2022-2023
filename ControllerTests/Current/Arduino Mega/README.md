# Navigation Program 

Hello! As you may or may not know, this is the cove of the navigation system. This folder contains all the necessary files/code that are used to successfully run navigation.


## How To Use

The main program that runs is "NavLoop.py", which has all the functions and methods imported from other files such as MathFunc.py and Objects.py (which I shall describe in more detail later). As a precaution to save you and your fellow mates from hours of debugging, a **controller must be connected to the device** of your choice before running the file. Additionally, make sure you have the code inside "ArduinoCode.ino" uploaded to your arduino. That is, assuming you know how to work an arduino (I do hope so), but I will not partake in any presuming. Before you actually upload the arduino code, make sure that your device has a connection with the arduino itself (arduino app -> tools -> port). Take that number and replace the variable "serial_number" in "NavLoop.py" if necessary. Now, you can upload the arduino code and it should say "Done uploading" on the bottom above the terminal of the arduino app. Congrats! This will enable you to smoothly run NavLoop.py without any issues.  

TLDR; just follow the instructions below lmao
1. Ensure proper connection between Arduino Serial and Device.
2. Take port number and replace variable named "serial_number" in NavLoop.py if necessary.
3. Upload code in ArduinoCode.ino to Arduino.
4. Make sure Controller is connected to Device
5. Run NavLoop.py



# Sections Below Contain Detailed Info on Each File and It's Purposes

## MathFunc.py

Contains the mathematics for robot movement. It takes in the controller input and outputs a string containing all six thruster values based the two joysticks, 4 buttons and LB, RB.

## Objects.py

Class Structure for Main Program to display sliders (I gave up on explaining dis and section above)
