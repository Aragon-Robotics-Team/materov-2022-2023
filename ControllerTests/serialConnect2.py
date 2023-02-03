import serial


arduino = serial.Serial('/dev/cu.usbmodem14201', 9600)
message = "hello,"
message.encode("ascii")

while True:
    arduino.write(message)
