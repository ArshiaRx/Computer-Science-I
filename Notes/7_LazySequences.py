# =============================================================================
# =============================================================================
# 2021/07/15 Thursday 7th-class > LazySequences
# =============================================================================
# =============================================================================
from sys import getsizeof

N = 1000
eager = [x for x in range(N) if "3" not in str(x*x)]
#produce all at the same time
lazy = (x for x in range(N) if "3" not in str(x*x))
#produce one at the time
print(len(eager))            #674
print(len(lazy))             #'generator' has no lenght
print(getsizeof(eager))      #5488
print(getsizeof(lazy))       #112


print(eager[42])
eager[42] = 'hello world'
print(eager[42])              #47

#udnerscore is a variable we dont care about
print([next(lazy) for _ in range(30)]) 
print("here")
print([next(lazy) for _ in range(30)])
#^keep winding


def fibonacci(a=1, b=1):
    yield a
    yield b
    curr, prev = a + b, b   #current and previous value
    while True:
        yield curr
        curr, prev = curr +  prev, curr
 

def pyramid_series():
    v = 1
    while True:
        for _ in range(v):
            yield v
        v += 1
        
from itertools import islice
from generators import fibonacci
a = fibonacci(42, 99)     #starts from 42 and 99
list(islice(a, 30))       #a variable and print up to 30 index

a = fibonacci()
b = fibonacci()
list(islice(a, 10))       #[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


from generators import collatz
list(islice(collatz(42), 20))       #[42, 21, 64, 32, 16, 8, 4, 2, 1]
#^start from 42 and subtract 



def scale_random(seed, scale, skip):
    #The seed value determines the futue random sequences
#    rng = Random.random(seed)
    curr, count, orig = 1, 0, scale
    while True:
#        curr += rng.randint(1, scale)
        yield curr
        count += 1
        if count == skip:
            scale = scale * orig 
            count = 0
            
from generators import scale_random
list(islice(scale_random(12345, 10, 5), 20))
#output as such
# =============================================================================
#[8,
 #9,
 #14,
 #20,
 #24,
 #59,
 #132,
 #188,
 #209,
 #257,
 #385,
 #1281,
 #1725,
 #1993,
 #2569,
 #5426,
 #14490,
 #17551,
 #23366,
 #24862]
# =============================================================================

def primes():
    _primes = [2, 3, 5, 7, 11]
    # Handy syntatic sugar fi ryield inside for-loop
    yield from _primes
    curr = 13
    while True:
        for divisor in _primes:
            if curr % divisor == 0:
                break
            if divisor * divisor > curr:
                _primes.append(curr)
                yield curr
                break
        curr += 2
        
        
def theons_ladder(n = 2, a =1 , b =1):
    while True:
        yield(a, b)
        #original Theon's ladder was just n = 2 
        a, b = a + n * b, a + b 
        
list(islice(theons_ladder(), 10))

#output as such
# ============================================================================
#[(1, 1),
#(3, 2),
#(7, 5),
#(17, 12),
#(41, 29),
#(99, 70),
#(239, 169),
#(577, 408),
#(1393, 985),
#(3363, 2378)]
# ============================================================================
#Let throguh every k:th element and discard the rest.
def every_kth(seq, k: int):
    count = k
    for x in seq:
        count -= 1
        if count == 0:
            yield x
            count = k

#Duplicate each element k times.

def stutter(seq, k):
    for x in seq:
        for _ in range(k):
            yield x
            
a = [1,2, 3]
b = [4, 5, 6, 7, 8]
list(zip(a, b))             #[(1, 4), (2, 5), (3, 6)]
list(zip.longest(a, b))     #[(1, 4), (2, 5), (3, 6), (None, 7), (None, 8)]

