 #7 - Count dominators
# def count_dominators(items):
#     count = 0               #let count be zero
    
#     if(len(items) == 0):     #if the lenght of item is zero return 0
#         return 0
    
#     elif(len(items) == 1):   #else if the lenght of item is one return 1
#         return 1 
    
#     #literating over the element of list
#     else:   
#         for i in range(len(items)-1):   
#             #^ for every element in range of lenght item loop and subtract one
            
#             if(items[i] > max(items[i+1:len(items)])):
#               #^ if the item index is bigger than max item index from i to 
#               #lenght of item, do the increment below
                
#                 count += 1   #increment count
                
#         #incrementing count for last element
#         count += 1 
        
#         return count

#SUCCESSFUL (SLOWER RUN TIME)
# =============================================================================
def count_dominators(items):
    result = 0
    for x ,item in enumerate(items):
        dominate = True
        for num in items[x+1:]:
            if item <= num:
                dominate = False
                break
        if dominate:
            result += 1        
    return result

#SUCCESSFUL (Faster Run Time)
# =============================================================================
print(count_dominators([42, 7, 12, 9, 2, 5]))
print(count_dominators([]))
print(count_dominators([99]))
print(count_dominators([42, 42, 42, 42]))
print(count_dominators(range(10**7)))
print(count_dominators(range(10**7, 0, -1)))
