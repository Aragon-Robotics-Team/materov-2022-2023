def thruster_pwm(LX, LY, RX):
    br = bl = fr = fl = 1500
    LJ_cap = 200
    RJ_cap = 50
    br += (LX * LJ_cap) + (LY * LJ_cap) - (RX * RJ_cap)
    bl += -(LX * LJ_cap) + (LY * LJ_cap) + (RX * RJ_cap)
    fr += -(LX * LJ_cap) + (LY * LJ_cap) - (RX * RJ_cap)
    fl += (LX * LJ_cap) + (LY * LJ_cap) + (RX * RJ_cap)

    string = str(br) + ", " + str(bl) + ", " + str(fl) + ", " + str(fr) + ", "
    return string

print(thruster_pwm(0.5, 0.5, 0))

