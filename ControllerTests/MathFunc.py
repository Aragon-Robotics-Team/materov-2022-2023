

def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1 = v2 = fr = fl = br = bl = 1500
    sendStr = "" #constructed string to be sent to the arduino

    # deadband 0.1 deviation
    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0
    
    # Front, Left, Back, Right Calculations (cap is 200)
    capMovement = 200
    br += PWM(Ly) * (capMovement/400)
    bl += PWM(Ly) * (capMovement/400)
    fr += PWM(Ly) * (capMovement/400)
    fl += PWM(Ly) * (capMovement/400)

    br += PWM(Lx)  * (capMovement/400)
    bl += -PWM(Lx) * (capMovement/400)
    fr += -PWM(Lx) * (capMovement/400)
    fl += PWM(Lx)  * (capMovement/400)

    #Pivoting CALCULATIONS (cap is 100)
    capPivot = 100
    br += -PWM(Rx) * (capPivot/400)
    bl += PWM(Rx)  * (capPivot/400)
    fr += -PWM(Rx) * (capPivot/400)
    fl += PWM(Rx)  * (capPivot/400)


    Vstrength = 200 #vertical thruster code chunks
    if(A): #if A is pressed
        v1 += Vstrength
        v2 += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength
        v2 -= Vstrength
        #v1 and v2 go down

    
    sendStr  = str(br) + "," + str(bl) + "," + str(fr) + "," + str(fl) + "," + str(v1) + "," + str(v2) + ","
    return sendStr

# calc = makeString(1, 1, 1, 0, 0)
# print(calc)

    






 