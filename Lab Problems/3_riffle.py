#3 - Riffle
def riffle(items, out=True):
    
    if items == []:
    #Return empty list if the original list is empty
        return []
    
    #Determine the helf of number of elements in the original list
    half = len(items) // 2
    
    #create an empty list
    result = []
   
    if out == True:
        #create two separate list which stores half of thd original list based on whether the value is True/False
        Half_list_1 = items[:half]
        Half_list_2 = items[half:]
        
    else:
        Half_list_1 = items[half:]
        Half_list_2 = items[:half]
        
    for i in range(half):
        #appending elements for both the list created in pervious step to the new empty list
        result.append(Half_list_1[i])
        result.append(Half_list_2[i])
        
    return result
    #return the resultant list

#SUCCESSFUL
# ============================================================
print(riffle([1, 2, 3, 4, 5, 6, 7, 8]))
print(riffle([1, 2, 3, 4, 5, 6, 7, 8], out=False))
print(riffle([]))
print(riffle(['bob', 'jack'], out=True))
print(riffle(['bob', 'jack'], out=False))
