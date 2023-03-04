import PID_Func
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


tick = 0 # represents each PID output (used for x-axis)
depth = 0.0
goal = 2.5
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

time_counter = 0
isTrue = False
isTrue2 = True
previous_depth = depth
max_overshoot = 0

pid_obj = PID_Func.PID()
pid_obj.tune_PID(500, 0, 0)

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
    global time_counter
    global isTrue
    global isTrue2
    global previous_depth
    global max_overshoot


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

    
    # calculate the ticks elasped for first overshoot
    if depth > goal:
        isTrue = True
    if depth > goal and isTrue and isTrue2:
        time_counter += 1
        if (depth > max_overshoot):
            max_overshoot = depth
    elif depth < goal and isTrue == True:
        isTrue2 = False
    
    print("Tick: " + str(tick) + " | Depth: " + str(depth))
    print("Ticks Elapsed: " + str(time_counter))
    print("Maximum overshoot: " + str(max_overshoot))
    print("PWM: " + str(PWM_Output[0]))
  

    if tick == 50:
        goal = float(input("Enter new goal: "))

    # P_x.append(tick)
    # P_y.append(p_depth)
    # I_x.append(tick)
    # I_y.append(i_depth)
    # D_x.append(tick)
    # D_y.append(d_depth)

    # if len(PID_x) > 50:
    #     PID_x.pop(0)
    #     PID_y.pop(0)
    #     goal_line_x.pop(0)
    #     goal_line_y.pop(0)

    previous_depth = depth
    
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









    





