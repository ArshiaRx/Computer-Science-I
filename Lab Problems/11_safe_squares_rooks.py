#11 - Rooks on a rampage
def safe_squares_rooks(n, rooks):
#    initializing two sets containing values from 0 to n-1
#    representing the initial safe rows and cols
    safe_columns = set(x for x in range(0, n))
    safe_rows = set(x for x in range(0, n))
    # looping through x, y values of each tuple in rooks
    for x, y in rooks:
        safe_columns.discard(x)
        #^ remove x is safe_column if there is any
        safe_rows.discard(y)
        #^ removing y from safe_rows if there is any
        
        if len(safe_rows) == 0 or len(safe_columns) == 0:
        #^if the lenght of rows or columns be none (zero),
            return 0   #return 0
        
    total_len = len(safe_columns) * len(safe_rows)
   
    return total_len

#SUCCESSFUL
# ==============================================================
print(safe_squares_rooks(10, []))
print(safe_squares_rooks(4, [(2, 3), (0, 1)]))
print(safe_squares_rooks(8, [(1, 1), (3, 5), (7, 0), (7, 6)]))
print(safe_squares_rooks(2, [(1, 1)]))
print(safe_squares_rooks(6, [(r, r) for r in range(6)]))
print(safe_squares_rooks(100, [(r, (r*(r-1)) % 100) for r in range(0, 100, 2)]))
print(safe_squares_rooks(10**6, [(r, r) for r in range(10**6)]))                               