#4 - Only odd digits
def only_odd_digits(n):
    
    digits = [int(x) for x in str(n)] 
    #^digits are sets of number (x) in a string (n)
    for num in digits:
    #^for each num in digit
        if num % 2 == 0:
            #^if the remainder of num is even then return false
            return False
        #else if its odd return True
    return True

#SUCCESSFUL
# ============================================================

print(only_odd_digits(8))
print(only_odd_digits(1357975313579))
print(only_odd_digits(42))
print(only_odd_digits(71358))
print(only_odd_digits(0))

#expected:
    #False
    #True
    #False
    #False
    #False