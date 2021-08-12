#14 - Intersecting, intersecting
def squares_intersect(s1,s2):
    #Defining square1: (x1, y1) and (x2, y2)
    square1_x1, square1_y1 = s1[0], s1[1]
    
    
    square1_x2 = square1_x1 + s1[2]
    square1_y2 = square1_y1 + s1[2]
    
    #finding square2: (x1, y1), (x2, y2)
    square2_x1, square2_y1 = s2[0], s2[1]
    
    square2_x2 = square2_x1 + s2[2]
    square2_y2 = square2_y1 + s2[2]
    
    #check if square start before the origin (Horizontal)
    if (square1_x2 < square2_x1) or (square2_x2 < square1_x1):
        return False   #Do not intersect

    #check if any square start before the y-coordinate origin.
    if (square1_y2 < square2_y1) or (square2_y2 < square1_y1):
        return False  #Doesn't intersect
    
    return True   #Intersect

#SUCESSFUL
# ============================================================================= 
print(squares_intersect((2, 2, 3), (5, 5, 2)))
print(squares_intersect((3, 6, 1), (8, 3, 5)))
print(squares_intersect((8, 3, 3), (9, 6, 8)))
print(squares_intersect((5, 4, 8), (3, 5, 5)))
print(squares_intersect((10, 6, 2), (3, 10, 7)))
print(squares_intersect((3000, 6000, 1000), (8000, 3000, 5000)))
print(squares_intersect((5*10**6, 4*10**6, 8*10**6), (3*10**6, 5*10**6, 5*10**6)))