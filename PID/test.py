import time

currentTime = time.time()
while True:
    time.sleep(5)
    break

print(time.time() - currentTime)


