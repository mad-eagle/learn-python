import time

gmtime = time.gmtime()
curr = time.time()
currTime = time.ctime(curr)

print("Current Time is : ",currTime)

print("Stopping execution for 1 sec")
time.sleep(1) # using sleep() to halt execution
print("finished execution for 1 sec , done")

localtime = time.localtime()
print(localtime)