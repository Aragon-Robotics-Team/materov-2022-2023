from serial import Serial

def main():
    arduino = Serial(port='/dev/cu.usbmodem14301', baudrate=9600, timeout=1)
    num = input("enter a number: ").encode("ascii")
    arduino.write(num)
    # data sent to arduino
    # waits for arduino to do something
    while (arduino.in_waiting == 0):
        pass

    recieved = arduino.readline().decode("ascii")  # read arduino data with timeout = 1
    print(recieved)


if __name__ == '__main__':
    main()
