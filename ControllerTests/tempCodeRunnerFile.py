import serial
import time

arduino = serial.Serial(port='/dev/cu.usbmodem14201', baudrate=9600, timeout=1)

time.sleep(1)

message = "Hello" + ","
message = message.encode("ascii")

arduino.write(message)

while (arduino.in_waiting == 0):
    pass

received = arduino.readline().decode("ascii")
print(received)