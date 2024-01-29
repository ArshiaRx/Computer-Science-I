#Submitted by 2021-08-09 --> CCPS109
# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":
#1 - Ryerson Letter Grade
def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

#SUCCESSFUL
# =============================================================================
#2 - Ascending list
def is_ascending(items):
    
    for i in range(1, len(items)):
        #for every element in items ranging 1 to len(items):
        if items[i-1] >= items[i]:
            #if the last index number is equal or bigger than current index
            return False     #return False
       
    return True      #if the whole thing run as stated return True

# SUCCESSFUL
# =============================================================================
# #3 - Riffle
def riffle(items, out=True):
    
    result = []   #result is a list
    
    if items == []:     #if items is a list return as a list
        return []
    
    #half of total lenght of items
    half = len(items) // 2
    

    if out == True:
        #if out is true
        first_half = items[:half]     #first half is anyhing until half lenght
        second_half = items[half:]  #second half is anything from half lenght to end
        
    elif out != True:       #else OR elif out != True OR out == False:
        first_half = items[half:]     #first half is anything after half lenght to end
        second_half = items[:half]   #second half is anything until half lenght
    
#^generally speaking first and second half will be opposite depends on out result 
        
    for i in range(half):
    #append first and second half on the range of the index of half to the result
        result.append(first_half[i])
        result.append(second_half[i])
        
    return result
    #return the resultant list

#SUCCESSFUL
# =============================================================================
#4 - Only odd digits
def only_odd_digits(n):
    
    digits = [int(x) for x in str(n)] 
    #^digits are sets of number or integer (x) in a string (n)
    
    for num in digits:
    #^for each num (element) in digit
        if num % 2 == 0:
            #^if the remainder of num is even then return false
            return False
        
    return True   #if all element is odd return True

#SUCCESSFUL
# =============================================================================
#5 - Cyclops numbers
def is_cyclops(n):
    #A nonnegative integer is said to be a cyclops number
    #If it consist of an odd number of digits then,
    #middle digit should be zero
    
    flag = 0  #flag will reset the variable to zero
    x = 0   #declaring a variable and intializing it with 0
    
    if n < 0:            #No negative number
        return False
    
    #Calculate the lenght of string (n)
    digits_len = len(str(n))
    
    #If the lenght of digits were even return False
    if digits_len % 2 == 0:
        return False
    
    #calculate the middle index of digits
    mid = int(digits_len/2)
    
    #if the number be 0 return true
    if digits_len == 1 and n == 0:
        return True
    

    
    #while the number is bigger than 0 do the following:
    while n > 0:
        #if n is even and middle number is not 0, return false
        if n % 10 == 0 and x != mid:
            return False
        
        #else if n is even and the middle digit is 0, reset it by flag to 1
        
        elif n % 10 == 0 and x == mid:
            flag = 1
        
        #chop off the last digit of number
        n //= 10     #n = n // 10
        x += 1       #x = x + 1   increment x by 1 after every iteration
        
    #if flag is 1 return True, else return false
    if flag == 1:
        return True
    else:
        return False

# SUCCESSFUL   
# =============================================================================    
# 6 - Domino cycle
def domino_cycle(tiles):
    
    lenght = len(tiles)    #lenght of tiles
     
    if(len(tiles) == 0):     #if there is nothing in tiles return True
        return True  
    
    #else if the first tuples
    #The first index represents which tuple () and then the second index 
    #represents which element in that tuple
    elif(tiles[0][0] == tiles[lenght-1][1]):
        #if first element of tiles which is a tuples and first element of tuples
        #is equal to the last element of tiles, 2nd index do the following:
        
        for i in range(lenght-1):    #itertating over the tuples of list
            
            #check if the 2nd index of tuples are not equal and are in cycle
            if tiles[i][1] != tiles[i + 1][0]:
                return False             #return false if they are not in cycle
        else:
            #else return True if all element are in cycle
            return True
    else:
        #return false if last and first are not adjacent
        return False
    
# SUCCESSFUL
# =============================================================================
#BY_PROF - Count Dominator

# def count_dominators(items):
#     if len(items) == 0:
#         return 0
#     dominators, big = 0, None
#     for e in reversed(items):
#         if big is None or e > big:
#             dominators += 1
#             big = e 
#     return dominators

#SUCCESSFUL
# =============================================================================
# 7 - Count Dominator
def count_dominators(items):
    
    length = len(items)    #find the length of items
    start = 1
    
    if (length == 0):    #if there is nothigng in the items return zero
        return 0
    
    last_element = items[-1]         #last_element is the last index in items
    
    #for every element in items in reverse do the following:
    for e in reversed (items):
        
        if last_element < e:      #if the last_element is less than element
            start = start + 1        #increment the start by adding 1
            last_element = e      #now let the element be the last element 
            
    return start     #rreturn start as the output

# SUCCESSFUL
# =============================================================================
# 8 - Extract increasing integers from digit string
def extract_increasing(digits):
    
    result = []     #RESULT is a list
    
    #initially current = 0 and previous = -1
    current, previous = 0, -1
   
    #Loop through each element in range of lenght of digits string
    for i in range(len(digits)):
        
        #defined d to convert string in result list to inreger
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

# SUCCESSFUL
# =============================================================================
# 9 - Taxi Zum Zum
def taxi_zum_zum(moves):
       
    #define a coordinate where shows one step from the origin,
    #let first element be defined as x and second be y, we set it in list
    #because the position might be change through out the program
    
        xy_coordinate = [[0, 1], [1, 0], [0, -1] ,[-1, 0]]
        #^  xy_coordinate = [[x, y]]
        
        x, y, current_origin = 0, 0, 0
        
        for i in moves:
                if i =='R':    #if i is 'R' for right
                        current_origin = (current_origin + 1) % 4
                        
                elif i =='L':    #if i is 'L' for left
                        current_origin = (current_origin - 1) % 4
                        
                else:      #else choose the element from defiend xy_coordinate
                            #with the current_origin value nd add them to x & y
                        x = x + xy_coordinate[current_origin][0]
                        y = y + xy_coordinate[current_origin][1]

#if none 'R' and 'L' add xy_coordinate position with origin to x and y
        return (x,y)      #lastly, return x and y value
    
    
# #SUCCESSFUL 
# =============================================================================    
#10 - Giving back change
def give_change(amount, coins):
    change = []      #give the change as a list
    i = 0     
    while amount > 0:    #while the amount is higher than zero do the following
        if amount >= coins[i]:   #loop through every coins index if is equal or
                                        #less then the amount
                                        
            #subtract amount from that coin in that specific index                           
            amount -= coins[i]      #amount = amount - coins[i]
            change.append( coins[i] )   #append add the coin index, to change
                                        #if its equal or less than amount
        else:
            i += 1        # i = i + 1
          #if the coins is higher than amount value skip to next coin
    return change   #return change as  result

#SUCCESSFUL
# =============================================================================
#11 - Rooks on a rampage
def safe_squares_rooks(n, rooks):
#    initializing two sets containing values from 0 to n
#    representing the initial safe rows and cols

    safe_columns = set(y for y in range(0, n))
    safe_rows = set(x for x in range(0, n))
    
    for x, y in rooks:    #loop for every x & y value os each tuple in rooks
        safe_columns.discard(y)
        #^ remove y in safe_column if there is any
        safe_rows.discard(x)
        #^ remove x in safe_rows if there is any
        
        if len(safe_rows) == 0 or len(safe_columns) == 0:
        #if safe_rows or coloumns has no lenght return zero
            return 0   
        
    total_len = len(safe_columns) * len(safe_rows)
    #^multiply the rows and columns to see length total
    
    return total_len   #return total lenght

#SUCCESSFUL
# =============================================================================
#12 - Try a spatula
def pancake_scramble(text):
    
    #loop through every element from 2 to the range of (lenght of text+1)
    #note: len(text)+1   --> +1 inicates that the last element be also included
    for i in range(2, len(text)+1):
        
        text = text[:i][::-1] + text[i:]
        #^text = from beginning to i reversed + from i to the end
    return text

#SUCCESSFUL
# =============================================================================
#13 - Boustrophedon
def create_zigzag(rows, cols, start=1):
    result = []     #result is a list
    for i in range(rows):    #for every element in range of rows create a list
        new_lis = []            #creating a temperary list name new_lis
        
        for j in range(cols):    #for every element in range of cols in new_lis
            new_lis.append(start)        #start the new list with start which is
            start += 1       #equal to one, and for every element in range
                                        #increment by one
            
        if i % 2 == 1:              #if the the element of i is odd
            new_lis.reverse()          #reverse the temp list 'new_lis' element
        result.append(new_lis)              #include it in result and return it
    return result

#SUCCESSFUL
# ===========================================================================       
#BY_PROF - Intersecting, intersecting

# def squares_intersect(s1, s2):
#     (x1, y1, d1) = s1
#     (x2, y2, d2) = s2
#     disjoint = x1 + d1 < x2 or x2 + d2 < x1 or y1 + d1 < y2 or y2 + d2 < y1
#     return not disjoint

#SUCESSFUL
# ===========================================================================
#14 - Intersecting, intersecting
def squares_intersect(s1,s2):
    #Defining square1: (x1, y1) and (x2, y2)
    # s1 = (x1, y1, x2, y2)
    square1_x1, square1_y1 = s1[0], s1[1]
    
    square1_x2 = square1_x1 + s1[2]   
    square1_y2 = square1_y1 + s1[2]   
    
    #finding square2: (x1, y1), (x2, y2)
    # s2 = (x1, y1, x2, y2)
    square2_x1, square2_y1 = s2[0], s2[1]
    
    square2_x2 = square2_x1 + s2[2]
    square2_y2 = square2_y1 + s2[2]
    
    #check if square start before the origin (Horizontal)
    if (square1_x2 < square2_x1) or (square2_x2 < square1_x1):
        return False   #Do not intersect
    
    #if (sq1_x2 < sq2_x1)  or (sq2_x2 < sq1_x1)
        #return False
        
    #check if any square start before the y-coordinate origin.
    if (square1_y2 < square2_y1) or (square2_y2 < square1_y1):
        return False  #Doesn't intersect
    
    #if (sq1_y2 < sq2_y1) or (sq2_y2 < sq1_y1):
        #return False
    
    return True   #Intersect

#SUCESSFUL
# =============================================================================  
#BY_PROF - Do you reach many, do you reach one?

# def knight_jump(knight, start, end):
#     knight = list(knight)       
#     knight.sort()
#     array = []
#     for i in range(len(start)):
#         array.append(abs(start[i]-end[i]))
#     array.sort()
#    if array == knight:
#        return True
#    else:
#        return False
    
#SUCCESSFUL
# =============================================================================
#15 - Sevens rule, zeros drool
def seven_zero(n):
    current, answer = 1, 0
    seven, zero = str(7), str(0)
    while True:
        if n % 2 == 0 or n % 5 == 0:
            #if n is divisable by 2 & 5, give remainder of 0, let x = 1
            x = 1
            while x <= current:     
                #while x <= 1 do the following
                value = int(x * seven + (current-x) * zero)
                        #value = ((1 * '7') + ((1-1) * '0'))
                if value % n == 0:
                #if value divisable by n is zero let answer = value
                    answer = value
                    break           #then break it
                x += 1      #x = x + 1      #do the loop while x <= curr
        else:
            #else value is only (curr * '7')
            value = int(current * seven)
            answer = value if value % n == 0 else 0
            #^set answer = value if value % n == 0
        current += 1    # current = current + 1
        #^increment current value by 1
        if answer > 0:
    #if answer is bigger than 0 return answer and break it
            return answer
            break
        
#SUCCESSFUL
# ===========================================================================
#16 - Fulcrum
def can_balance(items):
    negative = -1
    for num in range(len(items)):       #for every element in range(len(items)):
        L_torque, R_torque = 0, 0            #let left & right torque be zero
        
        for num1 in range(0, num):        
            L_torque = L_torque + items[num1] * (num - num1)  
            #for every element from in range of 0 to num:
        #left torque += items at that index * (difference of num-num1 element)
        
        for num2 in range(num + 1, len(items)):        #(same structure) 
            R_torque = R_torque + items[num2] * (num2 - num)
#for every element in range (2nd element of num up to the length of items):
            
        if(R_torque == L_torque):       #if the right torque and left are equal
            return num                    #return num
    
    return negative   #if all condition met return minus

#SUCCESSFUL
# =============================================================================
#17 - All your fractions are belong to base
def group_and_skip(n, out, ins):
    result = []        #result is a list
    while n != 0:         #while n is not zero do the follwoing:
        result.append(n % out)    
        n //= out  #n = n // out
        n *= ins     # n = n * ins

#simple computation:
#n, out, ins = 81, 5, 3
#n % out = 1    -->  append to result = [1]
#n // out = 16 
#n * ins = 48
#n % out --> 48 % 5 = 3 --> append to result = [1, 3 and etc ..]      
    return result
    
#SUCCESSFUL
# ============================================================================
#18 - Recaman's sequence
def recaman(n):
#     #recaman func takes a number n as an argument and return
#     #a list of first n terms in recaman series
    
      recaman_serie = []    #recaman serie is a list
      start = 1
#     #^lets consider the first n term to be 1
    
      recaman_serie.append(start)
#     #^ add the n term to the list recaman_serie
    
      for i in range(2, n+1):
#         #^loop the elements starting from 2nd index to nth index
#         #but excluding n+1
        
          if(start-i > 0 and (start-i) not in recaman_serie):
#            # check if previous term is = 0 and is not in the serie 
              curr_term = start - i
#             #then let current term be (start - index of element)
          else:
#             #^ if the condition does not meet let the curr be 
#             #equal to pstart + index of element
              curr_term = start + i
        
          recaman_serie.append(curr_term)
          #^ now add the current term to the recaman list after
          #looping through each element
        
          start = curr_term    #let the current term be the new start
      
    
      return recaman_serie     #return the list of recaman series
  
#SUCESSFUL
# =============================================================================
#19 - count the balls off the brass monkey
def pyramid_blocks(n, m, h):
    result = 0
    for i in range(h):     #loop through tht range(h):
        #add the sum after each loop
        result += (n * m)    #result = result + (n * m)
        #every time looping add 1 to n and m
        n += 1        #n = n + 1
        m += 1        #m = m + 1
    return result

#SUCCESSFUL
# =============================================================================
#20 - count growlers
def count_growlers(animals): 
    
    store = 0   #store the growling count
    
    #for every element check the value if exist and do the following:
    for i, value in enumerate(animals):          
        temp = 0    #temperary variable set to zero
        
        #if value is cat or dog we have to check left of the list
        if(value == 'cat' or value == 'dog'):
            
            for k in range(i):   
            #for every element 'k' of range(i) check if left side of i    
                #is a dog or god then add 1 to temp
                if(animals[(i - k) - 1] == 'dog' or animals[(i - k) - 1] == 'god'):
                    temp += 1      #temp = temp + 1
                    
                #if it is otherwise decrement
                else:
                    temp -= 1     #temp = temp - 1
                    
        #else if value is tac or god we do the following for loop:
            #will check to the right of it
        elif(value == 'tac' or value == 'god'):
            
             
            for k in range(len(animals) - i-1):
            #for every element 'k' of range(lenght(animals-last position)):
                #if the right side of animals is equal to dog or god increment
                if(animals[(i + k) + 1] == 'dog' or animals[(i + k) + 1] == 'god'):
                    temp += 1     #temp = temp + 1
                
                else:
                    temp -= 1     #temp = temp - 1

        if(temp > 0):    #if the temp is greater, do the following:

            i += 1       #increment the i count
            
            store += 1   #increment to store the growling count
   
    return store    #return store (the growling count)

#SUCCESSFUL
# =============================================================================
#BY_PROF - bulgarian solitaire 

# def bulgarian_solitaire(piles, k):
#     goal, count = list(range(1, k+1)), 0
#     while True:
#         if len(piles) == k and sorted(piles) == goal:
#             return count
#         count += 1
#         piles = [p -1 for p in piles if p > 1] + [len(piles)]

#SUCCESSFUL
# =============================================================================
#BY_PROF
# def tukeys_ninthers(items):
#     while len(items) > 1:
#         items = [sorted(items[i:i+3])[1] for i in range(0, len(items), 3)]
#     return items[0]

#SUCCESSFUL
# =============================================================================   
#21 - Crack the crag (poker game)
def crag_score(dice):
    count = [0] * 6    #list to store count --> count = [0, 0, 0, 0, 0, 0]
    result = [0] * 6    #list to store sum of same digits
    total_sum = 0        #total sum
    max_score = 0    #stores max crag score and return the highest score
  
    for i in range(3):   #loop through the range of 3
    #update the count       
        count[dice[i] - 1] += 1          #count[dice[i]-1] =  count[dice[i]-1] + 1
        result[dice[i] - 1] += dice[i]     #result[dice[i]-1] = result[dice[i]-1] + dice[i]
        total_sum += dice[i]                   #sum = sum + dice[i]
  
#crag cases - [1,6,6] [3,5,5] [5,4,4]
    if (count[0] == 1 and count[5] == 2) or (count[2] == 1 and count[4] == 2) or (count[4] == 1 and count[3] == 2):
        max_score = 50
    
#sum is 13
    elif total_sum == 13:
        max_score = 26
  
#check if the cards are three-of-a-kind
    elif count[0] == 3 or count[1] == 3 or count[2] == 3 or count[3] == 3 or count[4] == 3 or count[5] == 3:
        max_score = 25
  
#check if the cards arelow straight   
    elif count[0] == 1 and count[1] == 1 and count[2] == 1:
        max_score = 20
  
#check if the cards are high straight
    elif count[3] == 1 and count[4] == 1 and count[5] == 1:
        max_score = 20
  
#check if the cards are odd straight
    elif count[0] == 1 and count[2] == 1 and count[4] == 1:
        max_score = 20
  
#check if the cards are evenly straight
    elif count[1] == 1 and count[3] == 1 and count[5] == 1:
        max_score = 20
  
#if none of those cases do the the remaining cases by setting else statement
#find max out of ones, twos, threes, fours, fives and sixes
    else:
        for i in range(6):
            #loop through every element in range(6)
            #if result at every element is higher let the max_score be equal to it
            if max_score < result[i]:
                max_score = result[i]
  
    return max_score
# return the max_score as the result

#SUCCESSFUL
# =============================================================================
#22 - Sum of two square
def sum_of_two_squares(n):
    root = int(n**0.5)   #square root = radical(x^2 + y^2)
    
    #for every element in range (root, tuple(0, -1)):
    for i in range(root, 0, -1):
        # sq_i = int(i**2)
        
        diff = n - (i*i)   #define a variable to give the difference
        
        #define a variable where return the root of diffrent in integer
        diff_int = int(diff**0.5)  
        
        #if the root of diff to power of 2 is equal to diff and root of diff is
        #greater than zero, then return the element, the root of the difference
        
        if diff_int ** 2 == diff and diff_int > 0:
            return i, diff_int
        
#SUCCESSFUL
# =============================================================================
#23 - Carry on Pythonista
def count_carries(a, b):
    #x finds the minimum value whether is a or b
    #y finds the maximum value in (a, b)
    x, y = min(a, b), max(a, b)
    count, carry  = 0, 0
    while x != 0 or carry != 0:  #while x or carry not zero do the following:
       
        
        last_x = x % 10          #take the x remainder
        last_y = y % 10          #take the y remainder
        total = last_x + last_y + carry   #total is sum of all the reminder + carry 
        
        if total > 9:   #if total is greater than 9, increment 1 to count
            count += 1               
            carry = total // 10    #and let carry be the divison of total by 10
        else:           #else carry stays the same 
            carry = 0
            
        #lastly let x and y be divisable by 10
        x, y = x // 10, y // 10
        
    return count

#SUCCESSFUL
# =============================================================================
#BY_PROF - Expand positive integer intervals

# def expand_intervals(intervals):
#     if intervals == '':
#         return  []
#     result = []
#     for item in intervals.aplit(","):
#         dash = item.find("-")
#         if dash > 0:
#             start, end = item[:dash], item[dash+1:]
#         else:
#             start = end = item
#         result.extend(range(int(start), int(end)+1)
#     return result

#SUCCESSFUL
# =============================================================================
#24 - Expand positive integer intervals
def expand_intervals(intervals):
     
    result = []   #result is a list
    if not intervals:        #if there is no intervals return the result
        return result
    
    #define a variable string, where split every intevrals by comma
    string = intervals.split(',')

#for every element inthe string do the following:
    for element in string:
        #define a varibale Range, where split every element by a dash
        Range = element.split('-')
        #i is i integer of range wich is the first index of the Range
        i = int(Range[0])

        if len(Range) == 1:   #if the lenght of Range is 1, add the integer i to result
            result.append(i)
        else:       #

            while i <= int(Range[1]):  #while value of index 0 is less than 2nd index
                result.append(i)   #append the value to result and increment i by 1
                i += 1      # i = i + 1

    return result  #return the result as an ouput

#SUCCESSFUL
# ===========================================================================
#25 - Collapse positive integer intervals
def collapse_intervals(items):
    result, index = '', 0        #result = empty string,   index = 0
    
    
    while index < len(items):    #while len(items) is larger than index = 0 
        initial = index          #set initial = index
        
        result += str(items[initial])   
        # result = ' ' + str(items[index number]) 
        #the result will be displayed as an string
        
        #while 1 is added to initial and still lower than length of items and
        #items value at a index +1 is equal to the  next index value
        #do the follwoing:
        while initial + 1 < len(items) and items[initial] + 1 == items[initial + 1]:
            
            initial += 1   #increment 1 to the initial 
            
            #if initial and index are not qual
        if initial != index:
            index = initial + 1   #let index be equal to initial value + 1
            
            #let result be a empty string + dash + string of items for each index
            result += '-' + str(items[initial])    
            #result = result + '-' + str(items[initial])
        else:
            index += 1  #increment 1 to index
            #index = index + 1
            
        if index != len(items):   #if index is not qual to the length of items
            #do the following:
            result += ','   #result = result + ','
            
            
    return result    #lastly return result, where its a string numbers

#SUCCESSFUL
# =============================================================================
#By_PROF - What do you hear, what do you say?
#from itertools import chain
#def count_and_say(digits):
#    result, prev, count = '', None, 0
        #Chain two sequences into one sequence in a lazy fashion
        #to save time and space needed by digits + ['$']
#    for d in chain(digits, ['$']):
#            if d == prev:
#                count += 1
#            else:
#                if prev != None:
#                    result += str(count)
#                    result += prev
#                prev = d
#                count= 1
#    return result

#SUCCESSFUL
# =============================================================================
#26 - What do you hear, what do you say?
def count_and_say(digits):
    
    #define a list to hold and count the digit, also present the previous digit as string
    digit_holder, count_digit, prev = [], [], ''    #list to hold letters
    i = -1
    
    #if there is no digit return a empty string
    if len(digits) == 0:
        return " "

    #iterarte over the digits
    for element in digits:
        #if element is equal to previous digit, increment the value of count by 1
        if element == prev:       
            count_digit[i] += 1    #count_digit[i] = count_digit[i] + 1

        else:            
            digit_holder.append(element)    #add digit to the digit holder list
            i += 1                   #increment i count by 1 --> i = i + 1
            count_digit.append(1)    #then add 1 to the digit count list
            prev = element         #let previus digit be the current element

    result = ""    #let result be a string
    i = 0   #reset i to be zero
    
    #generate the string based on the both the list
    for element in digit_holder:
        #let result be the sum of string count digit of each index + element + prev result
        result += str(count_digit[i]) + element  # result = result + str(count_digit[i]) + element
        i += 1    #i = i + 1,  increment i by 1 
        
    return result  #return result as a string

#SUCCESSFUL
# =============================================================================
#27 - Reversing the deserver
def reverse_reversed(items):
    # isinstance = check if the first parameter is the type of the second parameter
    if (isinstance(items, list)):
        #^if items is a type of list do the following:
    
        result = []    #result is a list
        for element in items:     #for every element in items do the loop:
            #run the program for every element then append it into result list
            result.append(reverse_reversed(element))  
        result.reverse()    #reverse everything in result list
        return result       #return the result now
    else:              
        return items    #if items not a list return items 

#SUCCESSFUL
# =============================================================================
#28 - That's enough of you!
def remove_after_kth(items, k=1):
    
    
    finalized_items = []      #define a variable to be returned as a list
    same_items = list(set(items))        #list the same values of items
    
    #multiply the length of same items to get the list lenght
    number_of_items = [0]*len(same_items)     
    
    for i in range(len(items)):
        #for every element in range of length of items do the following:
            #define a variable to add the items element in the same list items
        index = same_items.index((items[i]))
        
        #increment number of items each time new index adds up
        #number_of_items[index] += 1
        number_of_items[index] = number_of_items[index] + 1
        
        if number_of_items[index] <= k:  
            #if number of items at each index is less than k fo the following:
                #add the items element to the finalized items list
            finalized_items = finalized_items + [items[i]]
            
    return finalized_items  #return the list

#SUCCESSFUL
# =============================================================================
#29 - That's enough for you!
def first_preceded_by_smaller(items, k=1):
    #iterate through the range of length of items:
    for i in range(len(items)):
        j, count = 0, 0   #define twok variable and set them to zero
        while j < i:     #while j is less than i do the following:
            
            if items[j] < items[i]:   #if items[j] element less than items[i] elemnt:
                count += 1    #increment 1 to the count, i = i + 1
                #then increment 1 to j count
            j += 1   #j = j + 1
        if count >= k:      #if count is equal or greater than k 
            return items[i]    #return items at each items element[i]

#SUCCESSFUL
# =============================================================================
#30 - Crab bucket list
def eliminate_neighbours(items):
    count = 0
    len_items = len(items)    #define the lenght of items
    
    if len_items == 1:    #if the length of items is equal to 1 retrun 1
        return 1

    #for every element in range(1, to len_items and including the last element)
    #do the following:
    for i in range(1, len_items + 1):
        #if there is any element in items increment 1 to the counter
        if i in items: 
            count += 1   #count = count + 1
            #if items has only one element remove it and exit the loop
            if len(items)==1:
                items.pop(0)
                break
            #find the element of i in items and locate it in index1
            index1 = items.index(i)
            
            index2 = index1 - 1   #subtract 1 from the index1 and set that to index2
            
            #if index 2 is less than zero OR index1+1 is less than length of items
            #and items[2nd index] is greater than items[index2] do the following:
            if index2 < 0 or ((index1 + 1) < len(items) and items[index1 + 1] > items[index2]):
                index2 = index1 + 1   #index2 is index1 + 1
            
            value = items[index2]   #let value be the items at the index2
            
            if index1 > index2:   #if index1 is greater than index2
                index1 = index2       #let indexs1 become equal to index2
                
            #Call pop items twice at same index, so the elements at index1 and index2 will be
            #removed (after first pop, index2 becomes new index1, so we should remove element at
            #index1 again to remove both values)
            items.pop(index1), items.pop(index1)
            
            #if the vale is equal to lenght of items break the loop
            if value == len_items:
                break

    return count   #return the count times

#SUCCESSFUL
# =============================================================================
#31 - Bishops on a binge
def safe_squares_bishops(n, bishops):
    cell = 0     #define a variable and set to zero
    for row in range(n):          #for every element row in range of n
        for coloumn in range(n):     #for every element coloumn in range of n
            safe = True         #if the safe is true do the for loop
            for position in bishops:     #for every element position in bishops,
            #do the following:
                if abs(row - position[0]) == abs(coloumn - position[1]):
                    safe = False
                #if the absolute of row subtract by the first element of position 
                #is equal to the absolute of coloumn subtracter by second element of position
                #change safe to be equal to False
                
                    break   #lastly end the loop by breaking it
                    
            if safe:       #if safe is true, increment cell by 1
                cell += 1
                
    return cell    #return cell as the result

#SUCCESSFUL
# =============================================================================
#32 - Everybody come do the Scrooge Shuffle
def spread_the_coins(coins,left,right):
    
    start, i = 0, 0                 #define two variable and set them two zero

    while i <(len(coins)):   
      #while i is less than the ocins length do the following:   
        
        
        #define a variable that goes throguht every elements of coin and
        #divide it by the sum of left and right
        x = coins[i] // (left + right)        
        
#if x is greater than zero, Remove extra coin from unstable piles  
        if x > 0:                
            #coins[i] = coins[i] - x * (lef + right)
            coins[i] -= x* (left + right)  
            
#if i element is not equal to the last coins element spread coing to right (if exist)
            if i != (len(coins) - 1):
                
                #coins[i + 1] = coins[i + 1] + x * right
                coins[i + 1] += x * right   
                
#if i element is equal to the last element of coins append right spread to coins
            elif i == (len(coins) - 1):    
                coins.append(x * right)     
                
#if i is not equal to zero, spread to left (if exist) and then decrement from i element            
            if i != 0:
                
                #coins[i -1] = coins[i -1] + x * left
                coins[i - 1] += x * left    
                i -= 1
                continue                    #continue from left spread
                
#if i is equal to zero, decrement from start     
            else:
                start -= 1
#insert = insert the 2nd parameter, to the first parameter which is a index psotion
                coins.insert(0, x * left)   
                continue                    #continue from left spread
        i += 1       #i = i + 1, while all condition are met incremeent i by 1
                       
    return(start, coins)   #return starts and coins

#SUCESSFULL
# =============================================================================
#33 - Calkin-Wilf sequence
from fractions import Fraction  #importing a mathematic fraction by python
def calkin_wilf(n):

    result = []       #result is a list
    frac = Fraction(1,1)    #defined a variable which a fraction of (1,1)
    result.append(frac)   #append it into the result list

  
    while n > 0:     #while n is greater than zero do the following:
        
        remove = result.pop(0)      #remove the first index of result
        frac = remove    #let the frac remove the first index of result
  
        numerator = remove.numerator      #remove the numenator which is 1st position in (x, y)
        denominator = remove.denominator  #remove rhe denominator which is 2nd position in (x, y)

        #the definition of fraction 1 and 2
        frac1 = Fraction(numerator, (numerator + denominator))
        frac2 = Fraction((numerator + denominator), denominator)
        
        
        #add the fraction1 & 2 to the result and start decrementing from n
        result.append(frac1)   
        result.append(frac2)
        n -= 1     #decrement from n , n = n - 1
    
    return frac   #return the fraction as the result

#SUCCESSFUL
# =========================================================================== 
#34 - Three Summer Go
def three_summers(items, goal):
    #define a variable that starts from negative
    count = -1
    
    
    #while count is less than the last element of the items, increment 1 to count
    while count < len(items)-1:
        count = count + 1
        i = count + 1               #create a new variable that takes over count
        last_element = len(items)-1   #last_item is the last element in items
        
        #while i is less than the last element, do the following:
        while i < last_element:
            
            #total is the addtion of items at index count + i + last_element
            total = items[count] + items[i] + items[last_element]
            
            #if the total is equal to goal return True
            if total == goal:
                return True
            #else if goal greater, increament i by 1
            elif total < goal:
                i = i + 1      # i += 1
            #else if total greater, decrement the last element by 1
            elif total > goal:
                last_element = last_element - 1    #last_element -= 1
                
      #when all condition are met, return False           
    return False

#SUCCESSFUL 
# =============================================================================
#35 - ztalloc ecneuqes
def ztalloc(shape):
    prev_value = 1  #previous value starts from 1
  
    #for every element i in range (last element) of lenght(shape) check in reverse
    for i in range(len(shape)-1,-1,-1):        #until the first element 
        
        if(shape[i] == 'd'):  #if any element of shape is equal to string d
            prev_value = prev_value * 2      #multiply previous value by 2, --> prev *= 2
            
        else:  #if none element shape is equal to string d, decrement the previous
            prev_value = prev_value - 1      #prev -= 1
            
            if (prev_value % 3) != 0:   #if previous value is divisable by 3
                return None         #and the remainder is not 0, return none
            
            else:     #else do the following expression
                
                prev_value /= 3  #previous = previous / 3   
                
                if((prev_value % 2 == 0)):     #if previous is even return None 
                    return None
    #when all condition are met, return previous value as an integer
    return int(prev_value)

#SUCCESSFUL
# =============================================================================
#36 - Count divisibles in range
def count_divisibles_in_range(start, end, n):
    
    #define a new variable where it subtracts start by n and find the difference
    #of the subtraction and the remainder of the n
    new = ((start - n) - (start % n))
    
    #define a new variable where subtracts (end by new) and do the divison of 
    #the remainder of the two by n, subtracted by 1
    diff = (((end - new) // n) - 1)
    
    #return the diff + if condition where it return 1 if start divided by n 
    #gives a remainder of 0 else returns zero
    
    return diff + (1 if start % n == 0 else 0)

#SUCCESSFUL
# =============================================================================
#37 - Bridge Hand Shape
def bridge_hand_shape(hand):
    #define a list, where the size of if it is 4
    result = [0] * 4       #reuslt = [0, 0, 0, 0]
    
    #for every element in hand, check the following:
    for i in hand:
        if i[1] == 'spades':
            result[0] += 1       #result[0] = reuslt[0] + 1
        #if 2nd element in hand is 'spades', increment by 1 to the result at 1st index
        
        elif i[1] == 'hearts':
            result[1] += 1       #result[1] = result[1] + 1
        #else if 2nd element in hand is 'hearts', increment by 1 to the result at 2nd index
        
        elif i[1] == 'diamonds':
            result[2] += 1       #result[2] = result[2] + 1
        #else if 2nd element in hand is 'diamonds', increment by 1 to the result at 3rd index
        
        #else: keep iterating to the 4th index of result by 1
        else:
            result[3] += 1       #result[3] = result[3] + 1
            
    return result

#SUCCESSFUL
# =============================================================================
#38 - Milton Work Point Count
def milton_work_point_count(hand, trump = 'notrump'):
    #define a variable point and set it to zero
    points_value = 0
    
    # create a dictionary to store number of card of each suit 
    suits = {'spades': 0,'hearts': 0,'diamonds': 0,'clubs': 0}

    #iterate over every card in hand and check for the conditions:
    for card in hand:
        
        #card is a tuple, where it has the following:
        value, suit = card
        
        #extract the card values & suits
        #add to points for value ace, king, queen, jack
        
        #if value is equal to 'jack' increment 1 to points_value
        if value == 'jack':
            points_value += 1   #points_value = points_value + 1
        
        #if value is equal to 'queen' increment 2 to points_value
        elif value == 'queen':
            points_value += 2   #points_value = points_value + 2
            
        #if value is equal to 'king' increment 3 to points_value    
        elif value == 'king':
            points_value += 3   #points_value = points_value + 3
            
        #if value is equal to 'ace' increment 4 to points_value
        elif value == 'ace':
            points_value += 4   #points_value = points_value + 4


        #after every element has been check increment 1 to the suits dict at that index
        suits[suit] += 1      #suits[suit] = suits[suit] + 1

    #if the values in dictionary is in a way ['king', 'king', 'king', 'ace']
    #decrement 1 from points_value
    if sorted(suits.values()) == [3, 3, 3, 4]:
        points_value -= 1        #points_value = points_value - 1
        return points_value

    #iterate over suits dict to add more points
    for suit, card_num in suits.items():
        
        #if there are 7 or more cards add 3 points (increment 3 points)
        if card_num >= 7:   
            points_value += 3    #points_value = points_value + 3
        
        #if there are 6 cards add 2 points (increment 2 points)
        elif card_num == 6:
            points_value += 2    #points_value = point_value + 2
            
        #if there are 5 cards, add 1 point (increment 1 point)
        elif card_num == 5:     
            points_value += 1    #poitns_value = points_value + 1

        #add points for trump
        #if trump is not equal to the str 'notrump' and suit is not equal to trump
        #do the following:
        if trump != 'notrump' and suit != trump:
            #if there is no card, add 5 to the points value (increment 5)
            if card_num == 0:
                points_value += 5     #points_value = points_value + 5
                
            #else if there is 1 card, add 3 to the points value (increment 3)
            elif card_num == 1:
                points_value += 3     #points_value = point_value + 3

    return points_value   #when all condition are met return points_value

#SUCCESSFUL
# =============================================================================
#39 - sort list by element frequency
def frequency_sort(items):
    result = []   #result should be a list
    sorted_list = sorted(items)     #sort the items
    count = 0       #define a count variable
    dic_count = {}       #defined a dictionary
     
    #while the lenght of sorted items is greater than count do the following:
    while count < len(sorted_list):
        
        #define a variable which is a sorted list of items with size of count
        element = sorted_list[count]   
        counter = 1                #define a variable counter, starts from 1           
        
        #check if length of sorted list is greater then count + 1 and
        #next index of sorted list has same size as element, while condition met
        #do the following:
        while(count + 1 < len(sorted_list) and sorted_list[count + 1] == element):
            #increment 1 to counter and count
            counter = counter + 1    #counter += 1
            count += 1   #count = count + 1
            
        #while length of sort lists is greater increment 1 to count 
        count += 1      #count = count + 1
        
        dic_count[element] = counter    #let the dictionary have same size of element
    
    #for every element in sorted value of dictionary while it is reversed,
    #do the following:
    for curr_val in sorted(dic_count.values(), reverse = True):

        #read every element key in dictionary in ascending order:
        for curr_key in sorted(dic_count.keys()):
            
#if the dictionary count with that index is equal to the element run throguht a loop
            if(dic_count[curr_key] == curr_val):
             
                #for every element in range(current_value), append the current key
                for i in range(curr_val):          
                    result.append(curr_key)   #to the reult, let the dictionary
                dic_count[curr_key] = 0        #with that index be equal to zero
                break  #exit the loop

    return result     #return the resultant

#SUCCESSFUL
# =============================================================================
#40 - Followed by its square
def square_follows(it):
    result = []          #result should be a list
    prev_values = set()    #previous num are a set
    
    #for every element in it, take the square root of it
    for digits in it:
        sq_root = digits**0.5   #square root of digits
        
        if sq_root in prev_values:
            result.append(int(sq_root))  #square root are integer, append it in result
        prev_values.add(digits)      #add digits to the previous values
        
    return result    #return result which is a list

#SUCCESSFUL
# =============================================================================
#41 - Longest arithmetic progression
def arithmetic_progression(items):
    #create a variable define the length of items
    length = len(items)
  
    if length == 1:             #if the length of items is 1
        return (items[0], 0, 1)   #return tuples, where the first index of items are (0, 1)
  
    if  length == 2:     #if the length of items is 2
    #return tuples, where the values are diffence of 2nd and 1st items and 2
        return (items[0], items[1] - items[0] ,2)   #(items[1] - items[0], 2)
  
    #create a table list for every element in x from 0 to the range(length)
    #for every y element in range(length)
    n_n__table = [[0 for x in range(length)] for y in range(length)] 
  
    #for every element in range of last element of length, do the following:
    for i in range(length-1):
        
        #let the every element of n_n__table[i] & last element be equal to 2
        n_n__table[i][length - 1] = 2 
  
    #iterate through every element from 2nd last element to very first element,
    #in reversed steps of 1
    for j in range(length - 2, 0, -1): 
        
        i = j - 1   #let i be the subtraction of j - 1 
        k = j + 1   #let k be the addition of j + 1
        
        #while i is equal or greater than zero and k is equal or less than 
        #last element of lenght, do the following:   
        while(i >= 0 and k <= length - 1):
            
            #if the addition of items[i] and items[k] is less than the 
            #multiplication of items[j] times 2, increment k by 1
            if ((items[i] + items[k]) < (2 * items[j])):
                k += 1     #k = k + 1
                
            #else if is greater, do the following:    
            elif ((items[i] + items[k]) > (2 * items[j])):
                
                #let the created table with index i and j
                n_n__table[i][j] = 2 
                i -= 1   #i = i - 1    #be equal to 2, and then decrement by 1
                
            else:
                    
                #update the n_n__table[i][j]
                n_n__table[i][j] = n_n__table[j][k] + 1
                
                i = i - 1    #decrement i by 1 --> i -= 1
                k = k + 1    #increment k by 1 --> k += 1
                
        #while i is equal oe greater than zero, do the following:
        while (i >= 0):
            n_n__table[i][j] = 2   #let the table at that element be equal to 2
            i -= 1     #i = i - 1     #decrement by 1
            
            loop, max_i, max_j = 0, 0, 0
            
    #for every element in range(lenght), loop through every element of j in range(length)
    for i in range(length):
        for j in range(length):
            #if the n_n__table[i][j] is greater than loop value, do the following:
            if n_n__table[i][j] > loop:
                
                #let the loop be n_n__table at[i][j] index
                loop = n_n__table[i][j]
                
                #lastly set the i and j to a new variable max 
                max_i = i     
                max_j = j
                
                #difference of items in the indexs
                diff_max = items[max_j] - items[max_i] 
  
    #return, items at [max_i] index, different of items at different index,
    #and the loop value
    return (items[max_i], diff_max, loop)

#SUCCESSFUL
# =============================================================================
#42 - Duplicate digit bonus
def duplicate_digit_bonus(n):
    #defined two variable, bonus starts at zero, count start counting at one
    bonus, count = 0, 1    
     
    #string is a string of n
    string = str(n)
   
    result = string[0]     #result is the first element of num which is a string
    
    #for every elemnt in range(1, length of num), do the following:
    for e in range(1,len(string)):
        #for the first element of num, increment 1 to the count
        if result == string[e]:
            count = count + 1    #count += 1
            
            #if the (element + 1) is equal to the length of num do the following:
            if (e + 1) == len(string):
                
                #bonus = bonus + 2 * (10**(count - 2))
                bonus += 2 * (10**(count - 2))
        else:
            #else not, if count is equal or greater than 2, do the following:
            if count >= 2:
                bonus = bonus + 10**(count - 2)
            count = 1   #reset count to be 1
        result = string[e]     #change the result to the num element
        
        #return the bonus value
    return bonus

#SUCCESSFUL
# =============================================================================
#43 - Whenever they zig, you gotta zag
def is_zigzag(n):
    result = []     #result should be a list
    zig = list(str(n))   #zig is a list of string n
    count = 0    #define a variable and set to zero
    
    #if the length of zigis equal or less than 2, return True
    if (len(zig) <= 2):    
        return True
    
    #for every element in range of length of zig, let string become integers
    for i in range(len(zig)):
        zig[i] = int(zig[i])   
        
    #for every element in range 1 up to the last element of length zig, do following:
    for i in range(1, len(zig)):
        #define a variable to subtract current element of zig with last element
        diff = zig[i] - zig[i-1]
        result.append(diff)         #append the difference to result
        
    
    #for every element in range zero up to the last element of length of result,
    #including last element do the following:
    for i in range(0, len(result) - 1):
        
        #if result(element) is greater than zero and next element less than zero
        #Or if viceversa, increment 1 to the count
        if ((result[i] > 0 and result[i + 1] < 0) or (result[i] < 0 and result[i + 1] > 0)):
            count += 1    #count = count + 1
        else:          #if otherwise, break the loop
            break
      
    #if count is equal to the last element of result, return True   
    if (count == len(result) - 1):
        return True
    
    return False   #if all condition are met return False

#SUCCESSFUL
# =============================================================================
#44 - Brussel's choice
def brussels_choice_step(n, mink, maxk):
    #define a variable which is a list
    result = [] 
    string = str(n)
    length = len(string)
    
    
    #for every element in range of (minks, maxk + 1):
    for i in range(mink, maxk + 1):
        #for every element in range (0 to the length of string n), do the following:
        for j in range(0, length):
            #if the element sum of element i and j is greater than length
            if (j + i) > length:
                break         #break the loop
            
            #define a variable where it return string as integer from j
            #element to the end of (j+i) element
            value = int(string[j:(j+i)])
            
            #define a temperary variable where is equal to 
            #string(n) anything up to j + result of mulitplication of value in string
            #plus anything from (i+j) element to the end
            temp = string[:j] + str(value * 2) + string[(i+j):]
            
            #append it as integer into the results list
            result.append(int(temp))
            
            #if value is even, do the following:
            if value % 2 == 0:
                #create a temprary varible which is equal to 
                #string(n) anything up to j, + string of result of value divisable by 2
                #plus string(n) from (i+j)to the end
                temp = string[:j] + str(value // 2) + string[(i+j):]
                
                #append the result in temp as a integer in results list
                result.append(int(temp))
    result.sort()  #sort the value integers in result
    
    #return the results list
    return result

#SUCCESSFUL
# =============================================================================
#45 - Reverse ascending sublists 
def reverse_ascending_sublists(items):
    #define a variable and set it to zero
    current = 0
    
    #enumerate = tuples (count, value)
    #for every item in items do the following while num is counting:
    for num, item in enumerate(items):
        
        if ((num + 1) >= len(items)) or (item >= items[num + 1]):
            #if (num + 1) is equal or greater than length of items OR
            #if items next index is equal or less than item value
            #do the following:
            
            items[current:num + 1] = items[current:num + 1][::-1]
            #let items value be equal to the reversed of it, means
#from start of current up to last element of num including it, but in reversed by -1
            
            current = num + 1   #let current value be updated by num value + 1

    return items  #return items

#SUCCESSFUL
# =============================================================================
#BY_PROF - Nearest Smaller Element

# def nearest_smaller(items):
#     n, res = len(items), []
#     for i, e in enumerate(items):
#         j = 1
#         while j < n:
#             left = items[i - j] if i >= j else e
#             right = items[i + j] if i + j < n else e
#             if left < e or right < e:
#                 res.append(left if left < right else right)
#                 break
#             j += 1
#         else:
#             res.append(e)
#     return res

#SUCCESSFUL
# =============================================================================
#BY_PROF - Sum of distinct cubes
#Create a function, and call it in the main function

# def sdc_rec(n, k):
#     if n == 0:
#         return []
#     if n < 0 or k < 1:
#         return None
#     i = k
#     while i**3 > n:
#         i -= 1
#     while i >= 0:
#         ans = sdc_rec(n - i**3, i - 1)
#         if ans is not None:
#             return [i] + ans
#         i -= 1
#     return None

# def sum_of_distinct_cubes(n):
#     k = 1
#     while k**3 < n:
#         k += 1
#     return sdc_rec(n, k)

#SUCCESSFUL
# =============================================================================
#BY_PROF - Manhattan skyline

#def manhattan_skyline(towers):
    #collect events into a list 0 means enter, 1 means exit.
#    sweep = [(s, 0, i, h) for (i, (s, e, h)) in enumerate(towers)]
#    sweep +=[(e, 1, i, h) for (i, (s, e, h)) in enumerate(towers)]
#    sweep.sort()    #sort the evens in ascending x-order.
#    total_area = 0  #count of total area.
#    prev_x = 0      #x-coordinate of the previous event.
#    active = set()  #The set of active buildings in the view.
#    tallest = 0     #The height of the currently tallest active building.
#    for(x, mode, i, h) in sweep:
        #add the area from the previous step.
#        total_area += (x - prev_x) * tallest
        #update the content of the active set depending on mode.
#        if mode == 0:  #Building i enters the active view.
#            active.add((i, h))
#            tallest = max(tallest, h)   #may need to update tallest.
#        else:     #Building i exits the active view.
#            active.remove((i, h))
#            if h == tallest:     #Tallest may now need to be updated.
#                if len(active) > 0:
#                    tallest = max(hh for (i, hh) in active)
#                else:
#                    tallest = 0
#        prev_x = x
#    return total_area

#SUCCESSFUL
# =============================================================================
#45 SUCCESSFUL PROJECT BY ME
