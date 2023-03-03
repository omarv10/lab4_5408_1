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
    print(n,"is not a prime number")