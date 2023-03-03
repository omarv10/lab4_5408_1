def is_prime(number): 
    if (number == 1):
            return False
    for i in range(2, number):
        if (number%i) == 0:
            return False
    return True
    
n = int(input("Enter a number: "))

if(is_prime(n) == True):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")# names: omar, elijah & jason 
#group 9
#cse 5408 Spring 2023 Lab 4

def reversed_input(user_string):
    return user_string[::-1]

txt = input("Input a string: ")
print(reversed_input(txt))# names: omar, elijah & jason 
#group 9
#cse 5408 Spring 2023 Lab 4
import time

def military_time(t):
    current_time = time.strftime("%H:%M:%S", t)
    return current_time


time_rn = time.localtime()

print("military time is:", military_time(time_rn))
