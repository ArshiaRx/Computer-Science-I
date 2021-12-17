# =============================================================================
# =============================================================================
# 2021/06/29 Tuesday 3rd-class > SequenceTypesListStringTuples
# =============================================================================
# =============================================================================

def near_ten(num):
    last  = num % 10
    return last


#List Example's
a = "Hello, world!"
len(a)       #13
a[7]         #'w'
a[12]        #'!'
a[:3]        #'Hel'
a[0:3]       #'Hel'
a[6:]        #' world!'
a[6:len(a)]  #' world!'
a[4:8]       #'o, w'
a[-1]        #'!'
a[0]         #'H'
a[-3:]       #'ld!'
#if we say a[20] it will error, but if we say:
a[4:20]      #'o, world!'               it will take whatever is possible
a[-20:20]    #'Hello, world!'
a[3:7]       #'lo, '
#IMPORTANT
a[7:3:-1]    #'w ,o'            starts from 7 goes up 3, but reversed (right to left) see -1
a[::-1]      #'!dlrow ,olleH'   everything from beginning to end but reversed (right to left)


b = range (5)
b[3]    #3
b[0]    #0

b = range(10**100)
b[42]   #42
b[99]   #99
b[12**34]  #4922235242952026704037113243122008064

r1 = range(10)
list (r1)      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r2 = range(5, 10)
list(r2)       #[5. 6, 7, 8, 9] 


r3 = range(0, 100, 5)  #from 0 to 100, with 5 steps in between
list(r3)       #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

str(r3)        #range(0, 100, 5)
str(list(r3))  #'[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]'
list(r3)       #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

str(42)        #'42'

s = "Hello\tworld"          #\t means tab
print(s)    #Hello    world

s = "Hello\nworld"          #\n means new line
print(s)    #Hello
            #world
            
s = "Hello\aworld"          #\a has no effect
print(s)    #Helloworld

s = "\uabcd"
print(s)   #'ꯍ' --> \uxxxx something encoded (Doesnt show the next 4 character)

s = '\\'
print(s)    #Double \\ will return single \
    
from fractions import Fraction
bob = [42, "hello", 123.456, type(Fraction), type, [17, 42, 99]]
len(bob)    #6
bob[:3]     #[42, 'Hello', 123.456]
bob[-3:]    #[abc.ABCMeta, type, [17, 42, 99]]

#bob = [42, "hello", 123.456, abc.ABCMeta, type, [17, 42, 99]]
bob[3] = 'yeah!'
bob               #[42, 'hello', 123.456, 'yeah!', type, [17, 42, 99]]    
bob.append(777)   #[42, 'hello', 123.456, 'yeah!', type, [17, 42, 99], 777] 
len(bob)    #7
   

longo = list(range(10**6))
#len(longo)   --> 1000000
longo[999999]    # 999999

str.capaitalize()   #return the first character capital and rest lowercase
str.upper()         #return all character uppercase
str.lower()         #return all character lowercase

a = "hello, wolrd!"
a.capitalize()      #'Hello, world!'
a.upper()           #'HELLO, WORLD!'

a = "HELLO, WOLRD!"
a.lower()           #'hello, world!'

str.count()         #count the number of thing
str.find()          #find the first left position of the thing

a.count('o')        #2   where indicated there are 2 'o's in str(a)
a.find('o')         #4   where indicates the first 'o' from left is position 4

#IMPORTANT
a.find('xyz')       #-1    return -1 because the it does not exist

#inside_out
a[a.find('o')]      #a[4] --> 'o'
a[a.find('xyz')]    #a[-1] --> '!'  does not exist therefore -1 and position -1 is '!'

#checks if the first variable 'o' is in the position given
a = "hello, world!"       #1st 'o' is in position 4, 2nd 'o' 4 is in position 8
a.find('o', 4)      #4
a.find('o', 5)      #8

#'in' operator
'o' in a            #True    checks if there is any 'o' in a 
'Hello' in bob      #True
'hello' in bob      #False


str.split()
a.split(' ')        #['hello, ', 'world!']

"Hello world, how are you there?".split()
#['Hello', 'world', 'how', 'are', 'you', 'there?']

"Hello world, how are you there?".split('a')
#['Hello world, how ', 're you there?']


"".join(str(42), str(99), str(77))    #'429977'
"$$$".join(str(42), str(99), str(77))   #'42$$$99$$$77'
", ".join(str(42), str(99), str(77))    #'42, 99, 77'

#x in s   #True if an item of s is equal to x, else False
#x not in s #False if an item of s is equal to x, else True
#s[i]     #a number is position of i
#s[i:j]   #slice of s from i to j
#s[j:j:k] #slice of s from i to j with step k
len(s)  #length of the str
min(s)  #smallest item of the str
max(s)  #largest item of the str
s.count(x) #total number of x in s 

[42, 17, 99][2]    #99

bob = [42, 'hello', 123.456, 'yeah!', type, [17, 42, 99]]
bob.append(777)       #[42, 'hello', 123.456, 'yeah!', type, [17, 42, 99], 777]
bob.pop()             #777
#bob = [42, 'hello', 123.456, 'yeah!', type, [17, 42, 99]]
bob.pop()             #[17, 42, 99]
#bob = [42, 'hello', 123.456, 'yeah!', type]
bob.pop(2)            #123.456
#bob =  [42, 'hello', 'yeah!', type]


joe = [42, 99, 17, -6, 0, 35]
list(sorted(joe))     #[-6, 0, 17, 35, 42, 99]
joe                   #[42, 99, 17, -6, 0, 35]
joe.sort()
joe                   #[-6, 0, 17, 35, 42, 99]
sorted(joe)           #[-6, 0, 17, 35, 42, 99]


list(reversed(joe))   #[99, 42, 35, 17, 0, -6]

joe = [17, 42, 99]
moe = [joe, joe, joe, joe]
moe                   #[[17, 42, 99], [17, 42, 99], [17, 42, 99], [17, 42, 99]]
joe[0] = -5
joe                   #[-5, 42, 99]
moe                   #[[-5, 42, 99], [-5, 42, 99], [-5, 42, 99], [-5, 42, 99]]
moe = [joe[:], joe[:], joe[:], joe[:]]
                      #[[-5, 42, 99], [-5, 42, 99], [-5, 42, 99], [-5, 42, 99]]
bob = joe[:]
bob                   #[-5, 42, 99]
bob[2] = 'hello'
bob                   #[-5, 42, 'hello']
joe                   #[-5, 42, 99]
moe = joe
moe, joe, bob         #[[-5, 42, 99], [-5, 42, 99], [-5, 42, 'hello']]


id(s)  #mean identify the address of memory
id(moe)   #4866396096
id(joe)   #4866396096
id(bob)   #4866498944

moe is joe  #True
moe is bob  #False

range(10)   #range(0, 10)
#list(_)     #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   list of all previous list

#cube example
[e*e*e for e in range(10)]       #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

#This will with replace the character with the next character in alphabet
#For example: "Hello wolrd!"
[chr(ord(c) + 1) for c in "Hello World!"]   #ord--> unicode number
#Result:
                #['I', 'f', 'm', 'm', 'p', '!', 'X', 'p', 's', 'm', 'e', '"']
#"".join(_)     #Under secore will scan for the most recent one
#Result:
                #'Ifmmp!Xpsme"'


#if we want to do inverse, oppsosite
[chr(ord(c) - 1) for c in "Hello World!"]
#Result:
               #['G', 'd', 'k', 'k', 'n', '\x1f', 'V', 'n', 'k', 'q', 'c', ' ']
#OR we can say:
"".join([chr(ord(c) - 1) for c in "Hello World!"])
#Result:
               #'Gdkkn\x1fVnkqc '    --> No space in between
#print(_)
#Result:
               #Gdkkn\x1fVnkqc
               
#EXAMPLE PROBLEM
d = 123**456
#len(str(_))                                      #953
[c for c in "Hello"]                              #['H', 'e', 'l', 'l', 'o']
len([c for c in str(d) if int(c) % 2 == 0])       #493
len([c for c in str(d) if int(c) % 2 == 1])       #460
#This means there are 493 numbers that are even
##This means there are 460 numbers that are odd
#which 493 + 460 = 953

a.islower()   #Asks if its lower


a = "Hello, world!"                      #'Hello, world!'   
[c for c in a if c.islower()]    #['e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
#^asks if there is lowercase in 'a' variable.
#doesn't have to be c, it can be anything.
#For example:
    #[xyz for xyz in 'variable for us is 'a'' if xyz.islower()]
"".join([c for c in a if c.islower()])   #'elloworld'

#To Print more copy of the result
"".join([c for c in a if c.islower()])           #'elloworld'
"".join([f"{c}{c}" for c in a if c.islower()])   #'eelllloowwoorrlldd'
"".join([c*3 for c in a if c.islower()])         #'eeellllllooowwwooorrrlllddd'


{2, 3, 4} == [1, 2, 3]     #False    
#^Tuple with list can not compared, They are not the same type(object)
#(1, 2, 3) is (1, 2, 3)    #True
[1, 2, 3] == [1, 2] + [3]  #True 
[1, 2, 3] is [1, 2] + [3]  #False

len([n for n in range(1, 1000001) if str(n) == str(n)[::-1]])   #1998
#reversed lenght
len([n for n in range(1, 10000001) if '33' in str(n)])          #45739
#^ there are 45739 numbers that contain '33'


