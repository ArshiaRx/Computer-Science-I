#7/20
import functools
#import operator
#import itertools
#from fractions import Fraction

@functools.lru_cache()   #(maxsize=128, typed=False) or (user_function)
def factorial(n, verbose=False):
    if verbose:
        print(f"enter with n = {n}")
    if n < 2:
        result = 1                      # base case
    else:
        result = n * factorial(n - 1, verbose)   # linear recursive call
    if verbose:
        print(f"Returning {result} from {n}")
    return result

#factorial means:
    #5! 1*2*3*4*5 = 120
    #3! 1*2*3     = 6
print(factorial(10, verbose=True))
print(factorial(5, verbose=True))
# =============================================================================

def hanoi(src, tgt, n):
    if n < 1:
        return None
    mid = 6 - src - tgt
    hanoi(src, mid, n - 1)
    print(f"Move top disk from {src} and peg {tgt}.")
    hanoi(mid, tgt, n -1)
    
    #For computing high integer powers, binary power is more efficient
    #than repeated multiplication n - 1 times.
    
    def binary_power(a, n, verbose=False):
        if verbose:
            print(f"Entering binary_power({n}).")
            if n < 0:
                raise ValueError(f"Negative exponent {n} not allowed.")
            elif n == 0:
                result = 1
            elif n % 2 == 0:
                result = binary_power(a * a, n // 2, verbose)
            else:
                result = a * binary_power(a * a, (n - 1) // 2, verbose)
            if verbose:
                print(f"Exiting binary_power({n}) with {result}.")
            return result
