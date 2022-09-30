def convert(val): #converting joystick numbers(-1 to 1) to pwm values
    #default is 1500
    return 1500 + val*400

(0.5, 0.5)

def getXVals():
    pass


def mathify(LJ, RJ): #get all the stuffs together  #left and right joysticks
    Lx =  LJ.getXVals()  # left joystick x position
    Ly = LJ.getYVals() # left joystick y position
    Rx = RJ.getXvals() # right joystick x position
    LxPWM = convert(LJ.getXvals())  # mapped value (to be added as PMW)
    LyPWM = convert(LJ.getYVals())  # mapped value (to be added as PMW)
    RxPWM = convert(RJ.getXvals())  # mapped value (to be added as PMW)

    #Ry values not necessary

    deadband = 0.1

    fl, fr, bl, br = 0  #each thrusters speed(2d motion)

    if(abs(Lx)<deadband): # if its greater than deadband
        #go right, else go left (my fault jiaqi)
        fl, bl += LxPWM
        #add onto the left thrusters
        pass
    if(Lx<0):
        fr, br += LxPWM
        #add onto the right thrusters
        pass
    if (Ly>0): #go forward, else go backwards
        br, bl += LyPWM
        #add onto the back thrusters
        pass
    if(Ly<0):
        fr, fl += LyPWM
        #add onto the front thrusters
        pass
    StringToSend  = str(fr)+str(fl)+str(br)+str(bl) 
    return StringToSend





