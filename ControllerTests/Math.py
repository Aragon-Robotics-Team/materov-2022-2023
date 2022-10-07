def PWM(joyVal): # converting a double to a PWM value
    limit = 400 # with 400 the max is 1900 and the min is 1100 PWM
    joyVal = (joyVal * limit)
    return joyVal

def ConvertString(LX, LY, RX, A, B): # add in claw buttons and Sensitive Mode
    #LX-Double/float, LY-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    
    v1 = v2 = fr = fl = br = bl = 1500
    string_values = ""

    if (LX > 0):
        fr += PWM(LX)
        br += PWM(LX)
        #fr and br activate
    elif (LX < 0):
        fl += PWM(LX)
        bl += PWM(LX)
        #fl and bl activate
    if (LY > 0):
        br += PWM(LY)
        bl += PWM(LY)
        #br and bl enable
    elif (LY < 0):
        fr += PWM(LY)
        fl += PWM(LY)
        #fr and fl enable


    if(RX>0):

        pass
    elif(RX<0):

        pass
    

    if RX > 0:
        maxRight = max(fl, br)
        spaceRight = 1900 - maxRight
        fl -= RX*spaceRight
        br -= RX*spaceRight

    elif RX < 0:
        maxLeft = max(fr, bl)
        spaceLeft = 1900 - maxLeft
        fr += RX*spaceLeft
        bl += RX*spaceLeft


        
    vertical_strength = 200 #deviation from 1500 for vertical thrusters from one button click
    if (A): #if A is pressed
        v1 += vertical_strength
        v2 += vertical_strength
        #v1 and v2 go up

    if (B): #if B is pressed
        v1 -= vertical_strength
        v2 -= vertical_strength
        #v1 and v2 go down

    array_values = [fr, fl, br, bl, v1, v2]
    print(array_values)

    for value in array_values: 
        value = max(1100, value)
        value = min(1900, value)
        string_values += str(value) + ", "

    #return array_values #return an array of thruster values rather than a string
    return string_values
    
"""
if (RX): # right controller joystick formula
        cap = 50
        modifier = 400/cap
        br -= PWM(RX)/modifier
        fr += PWM(RX)/modifier
        fl -= PWM(RX)/modifier
        bl += PWM(RX)/modifier
"""  

print(ConvertString(1, 0, 1, False, False))