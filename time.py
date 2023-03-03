# names: omar, elijah & jason 
#group 9
#cse 5408 Spring 2023 Lab 4
import time

def military_time(t):
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


time_rn = time.localtime()

print("military time is:", military_time(time_rn))
