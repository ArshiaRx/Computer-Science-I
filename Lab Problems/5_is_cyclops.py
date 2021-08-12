#5 - Cyclops numbers
def is_cyclops(n):
    #A nonnegative integer is said to be a cyclops number
    #If it consist of an odd number of digits then,
    #middle digit should be zero
    if n < 0:            #No negative number
        return False
    
    #Calculate the lenght of string (n)
    digits_len = len(str(n))
    
    #If the number of digits were even return False
    if digits_len % 2 == 0:
        return False
    
    #if the number be 0 is True
    if digits_len == 1 and n == 0:
        return True
    
    x = 0   #declaring a variable and intializing it with 0 
    
    #calculate the middle index of digits
    mid = int(digits_len/2)
    
    flag = 0  #flag will reset the variable to zero
    
    #while the number is bigger than 0 do the following:
    while n > 0:
        #if n is 0 and it is not the middle is not 0, return false
        if n % 10 == 0 and x != mid:
            return False
        
        #if n is 0 and it is middle digit then set flag to 1
        elif n % 10 == 0 and x == mid:
            flag = 1
        
        #chop off the last digit of number
        n = n // 10
        x += 1      #increment k by 1 after every iteration
        
    #if flag is 1 then return True, else is false
    if flag == 1:
        return True
    else:
        return False

#SUCCESSFUL   
# ============================================================    
print(is_cyclops(0))
print(is_cyclops(101))
print(is_cyclops(98053))
print(is_cyclops(777888999))
print(is_cyclops(1056))
print(is_cyclops(675409820))    
    
#expected:
    #True
    #True
    #True
    #False
    #False
    #False