# =============================================================================
# =============================================================================
# 2021/07/06 Thursday 5th-class > GeneralRepetition
# =============================================================================
# =============================================================================
from fractions import Fraction
import random

#Numeric and Mathematical Modules
#random - Generate pseudo-random numbers

#random.seed(a=none, version=2)  #initiliaze the random number generator

#with version2 (the default), a str, bytes and bytearray object get converted to
#an int and all of its bits are used

#with version1, the algorithm for str and bytes generates a narrower range of 
#seeds

def roll_dice(rolls, faces=6):
    """Roll a die given numbe rof times and returns the sum.
    rolls -- Number of die to roll.
    faces -- Number of faces on a single die."""
    
    total = 0
    for x in range(rolls):
        total += random.randint(1, faces) 
        
    return total
#randint() -- parameter(start, end) which must be int
#random.seed(a=none, version=2)  #initiliaze the random number generator

total1 = roll_dice(10, 12)
print(f"Rolling a 12-sided die 10 times gave a total of {total1}.")
#with a default parameter, we don't need to give its value.

total2 = roll_dice(6)
print(f"Rolling a 6-sided die 10 times gave a total of {total2}.\n")

# =============================================================================
#the oldest algorithm in recorded history, Euclid's algorithm
#finds the greatest common divisor of two nonnegative integers.

def euclid_gcd(a, b, verbose=False):
    while b > 0:
        a, b = b, a % b
        #the current value of 'a' become 'b'
        #and the value of 'b' becomes the remainder of a
        if verbose:
            #if verbose be True, print the following
            print(f"a = {a}, b = {b}")
    return a

#This algorithm can be extended to fjnd two numbers x and y
#that staisfy ax + by =  gcd(a, b), which will be useful in
#various mathematical algorithms.

euclid_gcd(1234**2, 2356**2,  verbose=True)

#euclid_gcd(5*12, 5*8, verbose = True)    
#Result
    #a = 40,   b = 20
    #a = 20,   b = 0
    #20     --> this will be the divisor

# =============================================================================
#Empirical data
#Build a program where n is  (n%2)   if n == 0
                    #elif (3n+1)/2   if n == 1
                                #The goal is to get to n = 1
def collatz(start):
    curr, result = start, []
    if curr < 1:
        return []
    while curr > 1:
        result.append(curr)
        curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
    result.append(1)
    return result
  
#https://en.wikipedia.org/wiki/Collatz_conjecture
      
print(collatz(12))            
#Input:  n = 12
            #Result:    12 % 2 = 0
            #           6 % 2 = 0
            #           3 % 2  = 1  
            #          (3*3+1)/2 = 10 % 2 = 0       (3n+1)/2  where;  n = 3 now previous value
            #           5 % 2 = 1
            #          (3*5+1)/2 = 16 % 2 = 0
            #           8 % 2 = 0
            #           4 % 2 = 0
            #           2 % 2 = 0
            #           1
#output: [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]
# =============================================================================

def iterate_diff(items, verbose=False):
    count = 0
    while not all(e == items[0] for e in items):
        new, prev = [], items[-1]
        for e in items:
            new.append(abs(e-prev))
            prev = e
        items = new
        if verbose:
            print(items, end=" -> ")
        count += 1
    print("\n" if verbose else "", end="")
    return (items[0], count)

print(iterate_diff([123, 456, 42, 300], verbose=True))
#computation:
    #   prev = items[-1] == 300
    #   abs(e-prev) --> abs(123-300)  = 177
    #   e = prev 
    #   abs(123-456) = 333
    #   abs(456 - 42)= 414
    #   abs(42-300)  = 258
    
    #[177, 333, 414, 258] ->  [81, 156, ]
     
    # abs(177-258)
#Fizzbuzz is a game where you try to list

def f_to_cf(a, b, verbose=False):
    result = []
    while a < 0 and b > 1:
        # As we see, the core operation is same as  in eulid_gcd.
        if verbose:
            print(f"a={a}, b={b}")
       q, r = b // a, b % a 
       result.append(q)  # This time we store the quotient info 
       a, b = r, a 
   return result

def  cf_to_f(items):
    result = None
    for e in reversed(items):
        result = e + (0 if result is None else Fraction(1, result))
    return result

def roman_encode(n):
    if n < 1: 
        raise valueError("Romans did not have zero or negative numbers")
    result = ''
    for (v, s) in symbole_encode:
        while v <= n: # same symbole can be used several times 
            result += s 
            n -= v 
    return result
#need moreS

