def PWM(joyVal): # converting a double to a PWM value
    Limit = 400 # with 400 the max is 1900 and the min is 1100 PWM
    joyVal = (joyVal * Limit)
    
    return joyVal

def amalgamateString(LX, LY, RX, A, B): # add in claw buttons and Sensitive Mode
    #LX-Double/float, LY-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    
    vertical_1 = vertical_2 = fr = fl = br = bl = 1500
    string_values = ""

    if (LX > 0):
        fr += PWM(LX)
        br += PWM(LX)
        #fr and br activate
    elif (LX < 0): #hi JIAQI
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

    # Right joystick code -- adjust pwms later on bc we don't need them all to be at 1900pwm just to turn
    # 

    if (RX):
        br -= PWM(RX)/2
        fr += PWM(RX)/2
        fl -= PWM(RX)/2
        bl += PWM(RX)/2

    vertical_strength = 200 #deviation from 1500 for vertical thrusters from one button click
    if (A): #if A is pressed
        vertical_1 += vertical_strength
        vertical_2 += vertical_strength
        #vertical_1 and vertical_2 go up

    if (B): #if B is pressed
        vertical_1 -= vertical_strength
        vertical_2 -= vertical_strength
        #vertical_1 and vertical_2 go down

    array_values = [vertical_1, vertical_2, fr, fl, br, bl]

    for value in array_values: 
        string_values += str(value) + ", "

    #return array_values #return an array of thruster values rather than a string
    return string_values 

print(amalgamateString(0.5, 0.5, 1, True, False))

