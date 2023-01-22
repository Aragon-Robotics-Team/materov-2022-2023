

def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B, mode):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1 = v2 = lf = lb = rf = rb = 1500
    sendStr = "" #constructed string to be sent to the arduino
    capMovement = 300
    capPivot = 100
    Vstrength = 200 #vertical thruster code chunks
    
    #deadband 0.1 deviation
    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0

    #LINEAR MODE
    if (mode > 0):

        v1 -= PWM(Rx) * (capMovement/100)
        v2 -= PWM(Rx) * (capMovement/100)

        # Front and Back Calculations (cap is 200)
        rb -= PWM(Ly) * (capMovement/400)
        lb -= PWM(Ly) * (capMovement/400)
        rf += PWM(Ly) * (capMovement/400)
        lf -= PWM(Ly) * (capMovement/400)

        
        #Crabbing Calculations (cap is 200)
        rb += PWM(Lx)  * (capMovement/400)
        lb += -PWM(Lx) * (capMovement/400)
        rf += -PWM(Lx) * (capMovement/400)
        lf += PWM(Lx)  * (capMovement/400)


        #Pivoting CALCULATIONS (cap is 100)
        rb += -PWM(Rx) * (capPivot/400)
        lb += PWM(Rx)  * (capPivot/400)
        rf += -PWM(Rx) * (capPivot/400)
        lf += PWM(Rx)  * (capPivot/400)

    #EXPONENTIAL MODE (ACCELERATION)
    else:

        #eq: cap*x^1.2
        exponent = 1.2
        # Front and Back Calculations (cap is 200)
        rb += (PWM(Ly)**exponent) * (capMovement/400)
        lb += (PWM(Ly)**exponent) * (capMovement/400)
        rf += (PWM(Ly)**exponent) * (capMovement/400)
        lf += (PWM(Ly)**exponent) * (capMovement/400)

        #Crabbing Calculations (cap is 200)
        rb += (PWM(Lx)**exponent)  * (capMovement/400)
        lb += -(PWM(Lx)**exponent) * (capMovement/400)
        rf += -(PWM(Lx)**exponent) * (capMovement/400)
        lf += (PWM(Lx)**exponent)  * (capMovement/400)


        #Pivoting CALCULATIONS (cap is 100)
        rb += -(PWM(Rx)**exponent) * (capPivot/400)
        lb += (PWM(Rx)**exponent)  * (capPivot/400)
        rf += -(PWM(Rx)**exponent) * (capPivot/400)
        lf += (PWM(Rx)**exponent)  * (capPivot/400)
        #if-else END

    # #up-down movement
    # if(A): #if A is pressed
    #     v1 += Vstrength
    #     v2 += Vstrength
    #     #v1 and v2 go up
    # if(B): #if B is pressed
    #     v1 -= Vstrength
    #     v2 -= Vstrength
    #     #v1 and v2 go down

    #capping the pwm values at 1900/1100, also rounding them to the whole number
    # pwmArray = [fr, fl, br, bl, v1, v2]
    pwmArray = [lf, lb, rf, rb, v1, v2]
    for index in range(len(pwmArray)):

        #round to whole number
        pwmArray[index] = round(pwmArray[index])
        
        #cap
        pwmArray[index] = max(1100, pwmArray[index])
        pwmArray[index] = min(1900, pwmArray[index])
    

    # sends the PWM values in the order:
    # fr, fl, br, bl, v1, v2
    sendStr  = str(pwmArray[0]) + "," + str(pwmArray[1]) + "," + str(pwmArray[2]) + "," + str(pwmArray[3]) + "," + str(pwmArray[4]) + "," + str(pwmArray[5]) + ","
    # sendStr  = str(1500) + "," + str(1500) + "," + str(1500) + "," + str(1500) + "," + str(pwmArray[0]) + "," + str(pwmArray[0]) + ","
    return sendStr

calc = makeString(0.5, 0.5, 0.5, 0, 0, 1)
print(calc)

    






 