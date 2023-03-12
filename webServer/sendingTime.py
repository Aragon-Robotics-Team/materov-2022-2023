import pygame
from serial import Serial
arduino = Serial('/dev/cu.usbmodem141201', 9600)

from datetime import datetime
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print("Current Time =", currentTime)

# while True:
#     # command = str(input("Time: "))
#     # arduino.write(command)
#     # time = str(arduino.readline())
#     # print(time)
#     arduino.write(currentTime.encode("ascii"))



# def serial_send_print(self):  # print to terminal / send regularly updated array to arduino

#         stringToSend = ','.join(str(x) for x in self.arduinoParams) + '.'
#         print('py: ' + stringToSend)  # print python
#         if self.serialOn:
#             self.arduino.write(stringToSend.encode("ascii"))  # send to arduino
#             start('arduino-wait')
#             # while self.serialRecieveOn and (self.arduino.in_waiting <= self.minBytes):  # wait for data
#             #     pass
#             sleep(self.loopSleep)
#             bytes = self.arduino.in_waiting
#             stringFromArd = self.arduino.readline().decode("ascii")  # read arduino data with timeout = 1

#             end('arduino-wait')

#             print('ard: ' + stringFromArd + ', ' + str(bytes))  # print arduino data


