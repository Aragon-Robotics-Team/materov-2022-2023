# Note: code will probably will be in arduino (pseudocode for now)

time_elapsed = 1 # not an exact ratio to the real world (sorta made up)

# PID multiplier values
proportional_gain = 1
integral_gain = 1
derivative_gain = 1

# important data
goal_value = 0 # arbitirary 
sensor_value = 0 # get this data from sensor
actuator_value = 0 # (Thrusters) get this data from arduino 
error_value = 0


# PID STUFF
proportion = 0
integral = 0
derivative = 0

while True:
    # ideology: gets current point, waits a bit, 
    # stores the current point as last point, 
    # and then calculates derivative based on that 
    # (depth difference/time elapsed)
    last_point = [sensor_value, time_elapsed]
    time_elapsed += 1
    current_point = [sensor_value, time_elapsed] # gets the newest value 
    derivative = (current_point[0] - last_point[0])/()



# output = proportion + integral + derivative