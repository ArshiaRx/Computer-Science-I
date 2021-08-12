#6 - Domino cycle
def domino_cycle(tiles):
    
    lenght = len(tiles)    #lenght of tiles
     
    if(len(tiles) == 0):     #if there is nothing in tiles return True
        return True  
    
    #check if the last time and first type are adjacent
    elif(tiles[0][0] == tiles[lenght-1][1]):
        
        #itertating over the tuples of list
        for i in range(lenght-1):
            
            #checke if they are in cycle
            if tiles[i][1] != tiles[i+1][0]:
                return False             #return false if they are not in cycle
        else:
            #else return True if all element are in cycle
            return True
    else:
        #return false if last and first are not adjacent
        return False
    
#SUCCESSFUL
# =============================================================================

print(domino_cycle([(3, 5), (5, 2), (2, 3)]))
print(domino_cycle([(4, 4)]))
print(domino_cycle([]))
print(domino_cycle([(2, 6)]))
print(domino_cycle([(5, 2), (2, 3), (4, 5)]))
print(domino_cycle([(4, 3), (3, 1)]))
