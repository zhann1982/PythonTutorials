# N! = 1*2*3*4*...*(N-2)*(N-1)*N

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
 
       # print(factorial(4))  -> 24

#--------------------------------------------#

# Check if N is divisible by M,
# here N and M are natural numbers

def isDivisible(n,m):
    if (n/m)%1 == 0:
        return True
    else:
        return False

       #print(isDivisible(9,3))  -> True

#--------------------------------------------#

# Check if N is prime number

def isPrime(n):
    for i in range(n//2):
        if i+1==1:
            continue
        if (n/(i+1))%1 == 0:
            return False
    return True
    
    #print(isPrime((2**565) + 1))  ->  False

#---------------------------------------------#

def checkOverflow(n,func):
    for i in range((2**n)+1):
        try:
            func(i)
        except OverflowError:
            return "Overflow at " + str(i)
    return "No overflow"

print(checkOverflow(600, isPrime))

