#13 - Boustrophedon
def create_zigzag(rows, cols, start=1):
    result = []     #result is a list
    for i in range(rows):    #for every element in range of rows create a list
        new_lis = []            #creating a temperary list name new_lis
        
        for j in range(cols):    #for every element in range of cols in new_lis
            new_lis.append(start)        #start the count and add to 'start'
            start += 1
            
        if i % 2 == 1:              #if the the element of i is odd
            new_lis.reverse()          #reverse the temp list 'new_lis' element
        result.append(new_lis)              #include it in result and return it
    return result

#SUCCESSFUL
# ============================================================================= 
print(create_zigzag(3, 5))
print(create_zigzag(10, 1))
print(create_zigzag(4, 2))