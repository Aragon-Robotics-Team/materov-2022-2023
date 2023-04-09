def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B, percent_horiz, percent_vert):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1 = v2 = fr = fl = br = bl = 1500
    sendStr = "" #constructed string to be sent to the arduino
    capMovement = 400 * (percent_horiz/100)
    capPivot = 400 * (percent_horiz/100)
    Vstrength = 400 * (percent_vert/100)

    Ly = Ly * (-1)  
    Lx = Lx * (1)
    Rx = Rx * (-1)
    
    # only works for crabbing and back/forth
    if abs(Lx) > 0 and abs(Ly) > 0.2:
        Lx = 0
        Ly = 0
    elif abs(Lx) < 0.2 and abs(Ly) > 0:
        Lx = 0
        Lx = 0


    #LINEAR MODE
    # Front and Back Calculations
    br += PWM(Ly) * (capMovement/400) 
    bl += PWM(Ly) * (capMovement/400)
    #fr += PWM(Ly) * (capMovement/400)

    

    #Crabbing Calculations
    br += PWM(Lx)  * (capMovement/400)
    #bl += -PWM(Lx) * (capMovement/400)
    fr += -PWM(Lx) * (capMovement/400)

    

    #Pivoting CALCULATIONS 
    #br += PWM(Rx) * (capPivot/400)
    bl += -PWM(Rx)  * (capPivot/400)
    fr += PWM(Rx) * (capPivot/400)

        
        
        

    #up-down movement
    if(A): #if A is pressed
        v1 += Vstrength
        v2 += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength
        v2 -= Vstrength
        #v1 and v2 go down


    #capping the pwm values at 1900/1100, also rounding them to the whole number
    pwmArray = [fr, fl, br, bl, v1, v2]
    for index in range(len(pwmArray)):
        # round to whole number
        pwmArray[index] = round(pwmArray[index])

        pwmArray[index] = max(1100, pwmArray[index])
        pwmArray[index] = min(1900, pwmArray[index])

    #pwmArray[4] = pwmArray[4] 
    # sends the PWM values in the order:
    # fr, fl, br, bl, v1, v2
    sendStr  = (str(pwmArray[0]) + "-" + 
                str(pwmArray[1]) + "=" + 
                str(pwmArray[2]) + "+" + 
                str(pwmArray[3]) + "*" + 
                str(pwmArray[4]) + "," + 
                str(pwmArray[5]) + ".")


    return sendStr
