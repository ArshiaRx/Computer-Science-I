#Introduction to strings
#character:  h  e  l  l  o
#index    :  0  1  2  3  4
#reverse  :  0 -4 -3 -2 -1
# [start:stop:step]

mystring = "Hello World"         #'Hello World'
mystring[0]                      #'H'

mystring = "abcdefghijk"         #'abcdefghijk
mystring[3:6]                    #'def'
mystring[1:3]                    #'bc'
mystring[::2]                    #'acegik'
mystring[2:7:2]                  #'ceg'
mystring[::-1]                   #'kjihgfedcba'

#String Properties and Methods
#Immutability: can not be changed
#string are not mutable! (meaning you can't use indexing to change
#inividual elements of a string)

name = "Sam"
name[0] = 'p'  #initializing the first index to be 'p' will error
last_letters = name[1:]             #'am'
'p' + last_letters                  #'pam'

x = 'Hello World'
x + " It is beautiful outside!"  #'Hello World it is beautiful outside'
x = x + " It is beautiful outside"
# x = Hello World " it is beautiful outside

letter = 'z'
letter * 10        #'zzzzzzzzzz'
2 + 3              # 5
'2' + '3'          #'23'

x = 'Hello World'
x.upper()            #'HELLO WORLD'
#^ make sure have paranthesis
x.lower()            #'hello world'
x.split()            #['Hello', 'World']

x = 'Hi this is a string'
x.split('i')            #['H', ' th', 's ', 's a str', 'ng']
#^split out the 'i' from the string