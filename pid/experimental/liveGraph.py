import time
import PID_Func
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


tick = 0 # represents each PID output (used for x-axis)
depth = 0.0
goal = 10.0
# p_depth = depth
# i_depth = depth
# d_depth = depth

PWM_Conversion = 0.001 # ex. 300 pwm = 0.3 meters traveled in a second

goal_line_x = [tick]
goal_line_y = [goal]
PID_x = [0.0]
PID_y = [depth]
# P_x = [0.0]
# P_y = [depth]
# I_x = [0.0]
# I_y = [depth]
# D_x = [0.0]
# D_y = [depth]

pid_obj = PID_Func.PID()
pid_obj.tune_PID(200, 0, 0)

def animate(i):
    # ok for some reason 
    # python is weird and doesnt 
    # recognize stuff as global 
    # variables so we need to explicitly 
    # say that
    global tick 
    global depth
    global p_depth
    global i_depth
    global d_depth
    global goal
    global PWM_Conversion
    global PID_x
    global PID_y
    global goal_line_x
    global goal_line_y
    global P_x
    global P_y 
    global I_x 
    global I_y
    global D_x
    global D_y


    tick += 1
    PWM_Output = pid_obj.calcPID(depth, goal)

    depth += (PWM_Conversion * PWM_Output[0]) #conversion is there to simulate the actual speed of the thrusters in water
    # p_depth += (PWM_Conversion * PWM_Output[1])
    # i_depth += (PWM_Conversion * PWM_Output[2])
    # d_depth += (PWM_Conversion * PWM_Output[3])

    PID_x.append(tick)
    PID_y.append(depth)
    goal_line_x.append(tick)
    goal_line_y.append(goal)
    # P_x.append(tick)
    # P_y.append(p_depth)
    # I_x.append(tick)
    # I_y.append(i_depth)
    # D_x.append(tick)
    # D_y.append(d_depth)
    

    plt.cla() #clear axes so lines don't change color
    plt.plot(goal_line_x, goal_line_y, label = "GOAL LINE")
    plt.plot(PID_x, PID_y, label = "PID")
    # plt.plot(P_x, P_y, label = "Porportional")
    # plt.plot(I_x, I_y, label = "Integral")
    # plt.plot(D_x, D_y, label = "Derivative")
    plt.legend() # line key

animation = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()









    





