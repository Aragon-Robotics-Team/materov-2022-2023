import time
import PID_Func
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


tick = 0 # represents each PID output (used for x-axis)
depth = 50.0
goal = 100.0
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
pid_obj.tune_PID(100, 2, 0)

def animate(i):
    # ok for some reason 
    # python is weird and doesnt 
    # recognize tick as a global 
    # variable so we need to explicity 
    # say that
    global tick 
    global depth
    global goal
    global PWM_Conversion
    global PID_x
    global PID_y
    global goal_line_x
    global goal_line_y

    tick += 1
    PWM_Output = pid_obj.calcPID(depth, goal)

    depth += (PWM_Conversion * PWM_Output[0])
    
    PID_x.append(tick)
    PID_y.append(depth)
    goal_line_x.append(tick)
    goal_line_y.append(goal)

    plt.cla() #clear axes so lines don't change color

    plt.plot(PID_x, PID_y, label = "PID")
    plt.plot(goal_line_x, goal_line_y, label = "GOAL LINE")

animation = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()









    





