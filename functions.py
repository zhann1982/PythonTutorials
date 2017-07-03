#  N! = 1*2*3*4*...*(N-2)*(N-1)*N

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
 
       #  print(factorial(4))  -> 24

#-----------------------------------------------------------------#

#  Check if N is divisible by M,
#  here N and M are natural numbers

def isDivisible(n,m):
    if (n/m)%1 == 0:
        return True
    else:
        return False

       #  print(isDivisible(9,3))  -> True

#-----------------------------------------------------------------#

#  Check if N is prime number

def isPrime(n):
    for i in range(n//2):
        if i+1==1:
            continue
        if (n/(i+1))%1 == 0:
            return False
    return True
    
       #  print(isPrime(21656616))
#----------------------------------------------------------------#

# Permutation of elements of array or string

def permut(array):
    if len(array) == 1:
        return [array]
    res = []
    for permutation in permut(array[1:]):
        for i in range(len(array)):
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    return res


       #  print(permut("abcd"))

#---------------------------------------------------------------#

# All combinations: M elements from LST

def comb(m, lst):
    if m == 0:
        return [[]]
    else:
        return [[x] + suffix for i, x in enumerate(lst)
                for suffix in comb(m - 1, lst[i + 1:])]

       #  print(comb(3, [1,2,3,4]))

#---------------------------------------------------------------#

# Get the result of Continued Fraction of next form:
#
#  1 / ( a0 + 1 / (a1 + 1 / (a2 + 1 / ....
#  
# Inpur is an array => [a0,a1,a2,a3,a4,...]

def continuedFraction(arr0):
    arr1 = arr0[1:]
    def recurr(arr):
        if len(arr)==1:
            return arr[0]
        return 1/(arr[0]+recurr(arr[1:]))
    return recurr(arr1) + arr0[0]

       #  print(recurr([1,1,1,1,1,1,1,1]))
    
#---------------------------------------------------------------#


            

