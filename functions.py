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
#  a0 + 1 / (a1 + 1 / (a2 + 1 / ....
#  
# Input is an array => [a0,a1,a2,a3,a4,...]

def continuedFraction(arr0):
    if len(arr)==1:
        return arr[0]
    return arr[0] + 1/continuedFraction2(arr[1:])

       #  print(recurr([3,7,15,1,292,1,1,1,2,1,3,1]))   ->  3.1415926535898153 = PI
    
#--------------------------------------------------------------------------------------#

# Get the result of General Continued Fraction of next form:
#
#  a0 + b0/( a1 + b1/( a2 + b2 / (... 
#
# Inputs are two arrays:  [a0,a1,a2,...] , [b0,b1,b2,...]

def generalCF(a,b):
    if (len(a)!=len(b)):
        if (len(a)<len(b)):
            b = b[:len(a)]
        else:
            a = a[:len(b)]
    if len(a)==1:
        return a[0]
    else:
        return a[0] + b[0]/generalCF(a[1:],b[1:])
    
      #   print(generalCF([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
      #   outputs  tanh(1)^(-1)
#---------------------------------------------------------------------------------------#

# interesting example of recursive function that returns multidimensional array

def recX(n):
    if n<=1:
        return 1
    x = [recX(n-1), 1]
    return x

      #   print(recX(5))    ->  [[[[1, 1], 1], 1], 1]
