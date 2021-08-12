#10 - Giving back change
def give_change(amount, coins):
    change = []      #give the change as a list
    i = 0;     
    while amount > 0:
        if amount >= coins[i]:
            amount = amount - coins[i]
            #append add the values to the change
            change.append( coins[i] )  
        else:
            i += 1
    return change

#SUCCESSFUL
# ============================================================
print(give_change(64, [50, 25, 10, 5, 1]))
print(give_change(123, [100, 25, 10, 5, 1]))
print(give_change(100, [42, 17, 11, 6, 1]))