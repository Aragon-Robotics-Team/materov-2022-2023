from serial import Serial

def main():
    arduino = Serial(port='/dev/cu.usbmodem143101', baudrate=115200, timeout=1)
    num = input("enter a number: ")
    arduino.write(num)
    while (arduino.in_waiting == 0):
        pass
    recieved = arduino.readline().decode("ascii")  # read arduino data with timeout = 1
    print(recieved)


if __name__ == '__main__':
    main()
