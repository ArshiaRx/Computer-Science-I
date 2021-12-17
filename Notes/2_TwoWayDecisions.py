# =============================================================================
# =============================================================================
#2021/06/24 Thursday 2nd-class > TwoWayDecisions 
# =============================================================================
# =============================================================================
d = "hello"

def foo(a, b, c):
    print(f"a is {a}, b is {b}, c is {c}")
    
    return a * (b + c)

print("Hello there!", end = "$$$")
#In order to get lined space we write 
print("")
#If a function expect for example three parameter
#for ex (a, b, c), then expects three value below
#if write result1 = foo(2, 3) will give our error msg
result1 = foo(2, 3, 4)
result2 = foo(1, 2, 3)
result3 = foo(4, "hello", "world")

print(f"result1 is {result1}")
print(f"result2 is {result2}")
print(f"result3 is {result3}")

#output as such
# =============================================================================
#Hello there!$$$
#a is 2, b is 3, c is 4
#a is 1, b is 2, c is 3
#a is 4, b is hello, c is world
#result1 is 14
#result2 is 5
#result3 is helloworldhelloworldhelloworldhelloworld  
# =============================================================================
# =============================================================================
a = 42 

def foo(a, b, c):
    print(f"Inside foo, a is {a}.")
    return a * (b + c)

print(f"Before call, a is {a}.")
print(foo(1, 2, 3))
print(f"After call, a is {a}.")
print(foo(4, 5, 6))

x = int(input("Enter x: "))
print(foo(x, x, x))

#output as such
# =============================================================================
#Before call, a is 42.
#Inside foo, a is 1.
#then goes to return statmenet: a * (b+c) --> Result: 5
#After call, a is 42.
#nside foo, a is 4.
#then goes to return statmenet: a * (b+c) --> Result: 44
#Enter x: 2
#Inside foo, a is 2.
#then goes to return statmenet: a * (b+c) --> Result: 8
# =============================================================================
# =============================================================================
#Self_Study
# =============================================================================

x = 42
msg = "The value of name x is currently"  + str(x)
#Output when type msg: The value of x is currently 42

msg = f"The value of name x is currently {x}"
#Output when type msg: The value of name x is currently 42

msg2 = f"x squared equals {x**2}"
#output when type msg2: 1764

from fractions import Fraction
a = Fraction(1, 3)
type(a)
#output: fractions.Fraction

b = Fraction(1, 10)
#Output when in console write a + b
#Fraction(13, 30)

Fraction(1/3)
#Output in console: Fraction(6004799503160661, 18014398509481984)



