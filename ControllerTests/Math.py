def PWM(joyVal): #converting a double to a PWM value
    Limit = 400 #with 400 the max is 1900 and the min is 1100 PWM
    joyVal = joyVal * 400
    return joyVal

def amalgamateString(Lx, Ly, Rx, A, B): #add in claw buttons and Sensitive Mode
    #Lx-Double/float, Ly-Double/float, Rx-Double/float, A-Boolean, B-Boolean, "Sensitive Mode" - Boolean
    v1= v2= fr= fl= br= bl = 1500

    HastaMañana = "" #constructed string to be sent to the arduino

    if(Lx>0):
        fr += PWM(Lx)
        br += PWM(Lx)
        #fr and br activate
    elif(Lx<0):
        fl += PWM(Lx)
        bl += PWM(Lx)
        #fl and bl activate

    if(Ly>0):
        br += PWM(Ly)
        bl += PWM(Ly)
        #br and bl enable
    elif(Ly<0):
        fr += PWM(Ly)
        fl += PWM(Ly)
        #fr and fl enable

    turnPWM = Rx50 #the fifty scales it down, bc we don't need 4 thrusters at 1900 pwm just to turn
    fl -= turnPWM
    bl += turnPWM
    br -= turnPWM
    fr += turnPWM


    Vstrength = 200 #deviation from 1500 for vertical thrusters from one button click
    if(A): #if A is pressed
        v1 += Vstrength
        v2 += Vstrength
        #v1 and v2 go up
    if(B): #if B is pressed
        v1 -= Vstrength
        v2 -= Vstrength
        #v1 and v2 go down

    list = [v1, v2, fr, fl, br, bl]
    for i in range(len(list)): #constructing HastaMañana
        list[i] = round(list[i])
        HastaMañana+= str(list[i])+","
    #return list #return an array of thruster values rather than a string
    return HastaMañana

print(amalgamateString(0.5, 0.5, 0, True, False))
