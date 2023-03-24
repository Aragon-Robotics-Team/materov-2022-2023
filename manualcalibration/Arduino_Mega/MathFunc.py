

def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B, mode, sensitive, coeffs):
    print(coeffs)
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1 = v2 = fr = fl = br = bl = 1500
    sendStr = "" #constructed string to be sent to the arduino
    capMovement = 400
    capPivot = 100
    Vstrength = 200 #vertical thruster code chunks
    expMulti = 1.2

    Ly = Ly * (-1)  
    Lx = Lx * (-1)  
    
    if sensitive == True:
        capMovement = capMovement/2
        capPivot = capPivot/2
        Vstrength = Vstrength/2
    
    #deadband 0.1 deviation
    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0


    #LINEAR MODE
    #if button is not pressed
    
    if (mode == False):

        # Front and Back Calculations (cap is 200)
        br += PWM(Ly) * (capMovement/400) * coeffs[0]/10 
        bl += PWM(Ly) * (capMovement/400) * coeffs[1]/10
        fr += PWM(Ly) * (capMovement/400) * coeffs[2]/10 
        fl += PWM(Ly) * (capMovement/400) * coeffs[3]/10
        

        #Crabbing Calculations (cap is 200)
        br += PWM(Lx)  * (capMovement/400) * coeffs[0]/10
        bl += -PWM(Lx) * (capMovement/400) * coeffs[1]/10
        fr += -PWM(Lx) * (capMovement/400) * coeffs[2]/10
        fl += PWM(Lx)  * (capMovement/400) * coeffs[3]/10
        

        #Pivoting CALCULATIONS (cap is 100)
        br += PWM(Rx) * (capPivot/400) * coeffs[0]/10
        bl += -PWM(Rx)  * (capPivot/400) * coeffs[1]/10
        fr += PWM(Rx) * (capPivot/400) * coeffs[2]/10
        fl += -PWM(Rx)  * (capPivot/400) * coeffs[3]/10
        

    #EXP MODE
    else:
        
        if Ly < 0:
            Ly = abs(Ly)
            br += (PWM(-(Ly**expMulti))) * (capMovement/400)
            bl += (PWM(-(Ly**expMulti))) * (capMovement/400)
            fr += (PWM(-(Ly**expMulti))) * (capMovement/400)
            fl += (PWM(-(Ly**expMulti))) * (capMovement/400)
        else:
            br += (PWM(Ly**expMulti)) * (capMovement/400)
            bl += (PWM(Ly**expMulti)) * (capMovement/400)
            fr += (PWM(Ly**expMulti)) * (capMovement/400)
            fl += (PWM(Ly**expMulti)) * (capMovement/400)

        if Lx < 0:
            Lx = abs(Lx)
            br += (PWM(-(Lx**expMulti)))  * (capMovement/400)
            bl += -(PWM(-(Lx**expMulti))) * (capMovement/400)
            fr += -(PWM(-(Lx**expMulti))) * (capMovement/400)
            fl += (PWM(-(Lx**expMulti)))  * (capMovement/400)
        else:
            br += (PWM(Lx**expMulti))  * (capMovement/400)
            bl += -(PWM(Lx**expMulti)) * (capMovement/400)
            fr += -(PWM(Lx**expMulti)) * (capMovement/400)
            fl += (PWM(Lx**expMulti))  * (capMovement/400)
        

        if Rx < 0:
            Rx = abs(Rx)
            br += -(PWM(-(Rx**expMulti))) * (capPivot/400)
            bl += (PWM(-(Rx**expMulti)))  * (capPivot/400)
            fr += -(PWM(-(Rx**expMulti))) * (capPivot/400)
            fl += (PWM(-(Rx**expMulti)))  * (capPivot/400)
        else:
            br += -(PWM(Rx**expMulti)) * (capPivot/400)
            bl += (PWM(Rx**expMulti))  * (capPivot/400)
            fr += -(PWM(Rx**expMulti)) * (capPivot/400)
            fl += (PWM(Rx**expMulti))  * (capPivot/400)
        
        

    #up-down movement
    if(A): #if A is pressed
        v1 += Vstrength * coeffs[4]/10
        v2 += (Vstrength + 38) * coeffs[5]/10 
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength * coeffs[4]/10
        v2 -= (Vstrength + 38) * coeffs[5]/10
        #v1 and v2 go down

    # print(coeffs)

    #capping the pwm values at 1900/1100, also rounding them to the whole number
    pwmArray = [fr, fl, br, bl, v1, v2]
    for index in range(len(pwmArray)):
        # round to whole number
        pwmArray[index] = round(pwmArray[index])

        pwmArray[index] = max(1100, pwmArray[index])
        pwmArray[index] = min(1900, pwmArray[index])

    pwmArray[4] = pwmArray[4] 
    # sends the PWM values in the order:
    # fr, fl, br, bl, v1, v2
    sendStr  = (str(pwmArray[0]) + "-" + 
                str(pwmArray[1]) + "=" + 
                str(pwmArray[2]) + "+" + 
                str(pwmArray[3]) + "*" + 
                str(pwmArray[4]) + "," + 
                str(pwmArray[5]) + ".")


    return sendStr
