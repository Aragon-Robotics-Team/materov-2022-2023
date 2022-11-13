

def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal*Limit
    return joyVal

def makeString(Lx, Ly, Rx, A, B):
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1= v2= fr= fl= br= bl = 1500
    sendStr = "" #constructed string to be sent to the arduino

    if(Lx < 0.1 and Lx > -0.1):
        Lx = 0
    if(Ly < 0.1 and Ly > -0.1):
        Ly = 0
    

    turn = PWM(Rx/6)
    br += round(PWM((Lx+Ly)/4) - turn)
    fl -= round(PWM((Lx+Ly)/4) - turn)
    bl += round(PWM((Ly-Lx)/4) - turn)
    fr -= round(PWM((Lx-Ly)/4) - turn)
    

    Vstrength = 200 #vertical thruster code chunks
    if(A): #if A is pressed
        v1 += Vstrength
        v2 += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength
        v2 -= Vstrength
        #v1 and v2 go down

    
    
    sendStr  = str(br)+","+str(fl)+","+str(bl)+","+str(fr)+","+str(v1)+","+str(v2)+","
    return sendStr




    






 