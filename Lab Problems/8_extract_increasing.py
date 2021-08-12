#8 - Extract increasing integers from digit string
def extract_increasing(digits):
    
    result = []     #RESULT is an empty list
    
    #initially current = 0 and previous = -1
    current, previous = 0, -1
   
    #Loop through each index element in digits string
    for i in range(len(digits)):
        
        #defined d to convert string in result list to int 
        d = int(digits[i])
        
        #update current value while in the loop range
        current = (current * 10) + d     
        
        #check if it current has higher value than prev
        if current > previous:
            
            #add 'append' current to the result
            #will separate with a comma
            result.append(current)
            
            #current digit becomes the previous
            previous = current
            
            current = 0 
            #^reset current when previous take over
            
    return result   #return the result which is a list

#SUCCESSFUL
# ============================================================
print(extract_increasing('045349'))
print(extract_increasing('77777777777777777777777'))
print(extract_increasing('122333444455555666666'))
print(extract_increasing('1234567890987654321'))
print(extract_increasing('3141592653589793238462643383279502884'))
print(extract_increasing('2718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260'))
print(extract_increasing('12345978' * 100))



