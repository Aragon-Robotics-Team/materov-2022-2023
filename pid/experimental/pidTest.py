import time
import PID_Func
import numpy as np 
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

PWM_Conversion = 0.001 # ex. 300 pwm = 0.3 meters traveled in a second

tick = 0 # represents each PID output (used for x-axis)
pid_obj = PID_Func.PID()
pid_obj.tune_PID(1, 0.0001, 1)

depth = 50.0
goal = 100.0

PID_x = [0.0]
PID_y = [depth]
P_x = [0.0]
P_y = [depth]
I_x = [0.0]
I_y = [depth]
D_x = [0.0]
D_y = [depth]


while True:
    tick += 1
    PWM_Output = pid_obj.calcPID(depth, goal)

    depth += (PWM_Conversion * PWM_Output[0])
    
    PID_x.append(tick)
    PID_y.append(depth)

    if tick > 25000:
        break

print(PID_y)
plt.plot(PID_x, PID_y)
plt.show()