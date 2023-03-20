# returns the current time but can't use this since the float isn't allowed to recieve data like this
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# figure out how to send time from arduino to python through bluetooth to webserver 
# 1. figure out how to record time: have a preset time --> use millis to add execution time to preset time + account for any delays through testing 
# 2. figure out how to get current time from computer and add it to time tracker 
# 3. send time to python through serial (also figure out bluetooth comm)
# 4. send python to web server 