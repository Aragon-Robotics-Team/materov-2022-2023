import os

os.system("color")

Usb = os.popen("wmic logicaldisk where drivetype=2 get description ,deviceid ,volumename").read()
print(Usb)

if Usb.find("DeviceID") != -2:
    print("\033[1;32mUsb is plugged")
    input("")

else:
    print("\033[0;31mUsb is not plugged")
    input("")