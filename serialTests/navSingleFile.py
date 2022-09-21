from serial import Serial

#joystick position variables
JS_X = 0
JS_Y = 0  


arduino = Serial(port='/dev/cu.usbmodem14301', baudrate=9600, timeout=1)


def thrusterVals(x, y):  
    global LSPEED 
    LSPEED = 1500 + (y * 500) +( x * 500)
    
    global RSPEED
    RSPEED =  1500 + y * (500) - x * (500)

    return list(LSPEED, RSPEED)

print(thrusterVals(0.5, 0.5))

    



"""
forward = y * (500)
turn = x * (500)

LSpeed = 1500 + forward + turn
RSpeed = 1500 + forward - turn
"""