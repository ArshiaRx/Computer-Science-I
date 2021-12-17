# =============================================================================
# =============================================================================
# 2021/07/01 Thursday 4th-class > SequenceIteration
# =============================================================================
# =============================================================================

def demonstrate_for(seq):
    print(f"Processing {seq}:")
    for e in seq:
        print(f"Element {e} processed")
    print("Done Processing.")   #OR print(f"Done Processing.")
    #since does not return any value
    
demonstrate_for("Hello")
demonstrate_for([42, "wolrd", 123.456])
demonstrate_for(range(10))

#output as such
# =============================================================================
#Processing Hello:
#Element H processed
#Element e processed
#Element l processed
#Element l processed
#Element o processed
#Done Processing.
#Processing [42, 'wolrd', 123.456]:
#Element 42 processed
#Element wolrd processed
#Element 123.456 processed
#Done Processing.
#Processing range(0, 10):
#Element 0 processed
#Element 1 processed
#Element 2 processed
#Element 3 processed
#Element 4 processed
#Element 5 processed
#Element 6 processed
#Element 7 processed
#Element 8 processed
#Element 9 processed
#Done Processing.
# =============================================================================
# =============================================================================
def demonstrate_for(seq):
    print(f"Processing {seq}:")
    for (i, e) in enumerate(seq):     #where i is the [index] and e is element
        print(f"Element {e} in position {i} processed")
    print("Done Processing.")     #OR  print(f"Done Processing.")
    #enumerate()  --> counts the index(position)
    
demonstrate_for("Hello")
demonstrate_for([42, "world", 1233.456])
demonstrate_for(range(10))

demonstrate_for("")
demonstrate_for([])
demonstrate_for(range(0))

#output as such
# =============================================================================
#Processing Hello:
#Element H in position 0 processed
#Element e in position 1 processed
#Element l in position 2 processed
#Element l in position 3 processed
#Element o in position 4 processed
#Done Processing.
#Processing [42, 'world', 1233.456]:
#Element 42 in position 0 processed
#Element world in position 1 processed
#Element 1233.456 in position 2 processed
#Done Processing.
#Processing range(0, 10):
#Element 0 in position 0 processed
#Element 1 in position 1 processed
#Element 2 in position 2 processed
#Element 3 in position 3 processed
#Element 4 in position 4 processed
#Element 5 in position 5 processed
#Element 6 in position 6 processed
#Element 7 in position 7 processed
#Element 8 in position 8 processed
#Element 9 in position 9 processed
#Done Processing.

#Processing :
#Done Processing.
#Processing []:
#Done Processing.
#Processing range(0, 0):
#Done Processing.
# =============================================================================
# =============================================================================
from itertools import accumulate

#import radius 

def factorial(n):
    """Return the factorial of a positive integer.
    n -- The postive whose factorial is computed. """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

factorial(3)  #output will be 6
#This means 1*2*3 = 6
factorial(0)  #output will be 1
#whatever number we input in n, for that many times the result will keep multiply

# =============================================================================
# =============================================================================
def maximum(seq):
    """Return the largest element in sequence."""
    if seq == []:
        raise ValueError("Empty list has no maximum")
    first = True 
    for x in seq:
        if first or x > king:
            king = x
            first = False
    return king

print(maximum([5, 2, 8, 1, 0, 9, 6]))  #9   (the biggest value is 9)
print(max([5, 2, 8, 1, 0, 9, 6]))      #9
print(maximum([]))                     #ValueError: Empty list has no maximum

# =============================================================================
# =============================================================================
def accum(seq):
    result = []
    total = 0
    for x in seq:
        total += x
        result.append(total)
    return result

print(accum([1, 2, 3, 4, 5]))     
print(list(accumulate([1, 2, 3, 4, 5]))) 

#output as such     
# =============================================================================
#Computation:
#0 + 1 = 1
#1 + 2 = 3
#3 + 3 = 6
#6 + 4 = 10
#10 + 5 = 15

#[1, 3, 6, 10, 15]
# =============================================================================
# =============================================================================
def select_upsteps(seq):
    prev = None  #None means no value
    result = []
    for x in seq:
        if prev is None or x > prev:
 #if there is no previous value or x is bigger than prev value do the following
            result.append(x)
        prev = x
    return result

print(select_upsteps([4, 8, 3, 7, 9, 1, 2, 5, 6]))

#output as such
# =============================================================================
#Computation:
#  None < 4          None < 4
#     4 < 8             3 < 8
#     3 < 8             7 < 9
#     3 < 7             1 < 2
#     7 < 9             5 < 6
#     1 < 9
#     1 < 2
#     2 < 5
#     5 < 6
#       
#[4, 8, 7, 9, 2, 5, 6]
# =============================================================================
# =============================================================================
def leading_digit_list(n):
    prod = 1                         #the currecnt factorial
    digits = [0] * 10                #creat a list full of zeros
    for i in range(1, n + 1):
        lead = int(str(prod)[0])     #Extract the highest order digit
        digits[lead] += 1
        prod = prod * i              #Next Factorial, from the current one
    return digits

print(leading_digit_list(2))

#https://en.wikipedia.org/wiki/Benford%27s_law

#output as such
# =============================================================================
#Computation:
#Example --> Input 2
#   digit = [0] * 10  --> [10] --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   range(1, n + 1)   --> range(1, 3) --> 1, 2
# 
#[0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# =============================================================================
from math import log
def output_leading_digits(n):
    digits = leading_digit_list(n)
    benford = [100 * (log(d+1, 10) - log(d, 10)) for d in range(1, 11)]
    print("\nDigit Observed Benford")
    for i in range(1, 10):
        pct =100 * digits[i] / n
        print(f"{1:5d}{pct:9.2f}{benford [i-1]:9.2f}")
    print("")

print(output_leading_digits(2))   #//Need to input define the above function

#ouptut as such
# =============================================================================
#Digit Observed Benford
#    1   100.00    30.10
#    1     0.00    17.61
#    1     0.00    12.49
#    1     0.00     9.69
#    1     0.00     7.92
#    1     0.00     6.69
#    1     0.00     5.80
#    1     0.00     5.12
#    1     0.00     4.58
#
#None      
# =============================================================================
# =============================================================================
names1 = {'Larry', 'Johnny', 'Billy', 'Mary', 'Larry'}   
names2 = {'Max', 'Lena', 'Larry', 'Billy', 'Tina'} 

print('Tony' in names1)           #False
print('Mary' in names1)           #True
print('Jonney' not in names1)    #False

print("First time through this set:")
for x in names2:
    print(f"{x} is in the second set.")
    
print("Second time through the same set:")
for x in names2:
    print(f"{x} is in the second set.")

#output as such
# =============================================================================
#Computation:                                     #Since its a list
#   First time through this set                   #They will not print in order
#   Billy is in the second set.
#   Lena is in the second set.
#   Tina is in the second set.
#   Max is in the second set.
#   Larry is in the second set.

#   Second time through the same set:
#   Billy is in the second set.
#   Lena is in the second set.
#   Tina is in the second set.
#   Max is in the second set.
#   Larry is in the second set.
# =============================================================================
# =============================================================================
names1 = {'Larry', 'Johnny', 'Billy', 'Mary', 'Larry'}   
names2 = {'Max', 'Lena', 'Larry', 'Billy', 'Tina'}
#^These are sets:
    #Sets: Un-ordered collection, which will only represent once if there is 
    #multiple of same item.

union = names1.union(names2) 
difference = names1.difference(names2)         #Difference from 1st to 2nd list
intersection = names1.intesrsection(names2)    #Same item in two list

print(F"Union of names is {union}.")
print(f"Their difference is {difference}.")
print(f"Their intersection is {intersection}.")

#ouput as such
# =============================================================================
#Computation:
#Union of names is {'Lena', 'Tina', 'Max', 'Mary', 'Johnny', 'Billy', 'Larry'}.
#Their difference is {'Mary', 'Johnny'}.
#Their intersection is {'Billy', 'Larry'}.
# =============================================================================
# =============================================================================
#Dictionary Object:
scores = {'Mary': 14, 'Tony': 8, 'Billy': 20, 'Lena': 3}
#Since the same notation of rucly braces is used for both sets and dictionaries,
#I wonder which one {} is?   (It's a dictionary)

print("The type of {} " f"is {type({})}.")   #The type of {} is <class 'dict'>.

print(scores['Mary'])                        #14
scores['Lena'] = scores['Lena'] + 5          #Lena scores 5 more point 3 + 5
print(scores['Lena'])                        #8
scores['Anne'] = 12                          #Addes Anne in the dictionary
del scores['Tony']                           #Removes Tony from dictionary
#scores                      #{'Mary': 14, 'Billy': 20, 'Lena': 8, 'Anne': 12}



# =============================================================================
#WORD_COUNT.py
# Regular expressions are a powerful way to perform some computations
# on strings that otherwise would be quite difficult.

import re

# To get rid of single quotes in text, we replace contractions with
# full words. This way, any single quotes that remain are actual quotes.

replacements = (
      ("doesn't", "does not"),
      ("don't", "do not"),
      ("you're", "you are"),
      ("i'm", "i am"),
      ("we're", "we are"),
      ("they're", "they are"),
      ("won't", "will not"),
      ("can't", "can not"),
      ("shan't", "shall not"),
      ("shouldn't", "should not"),
      ("mustn't", "must not")
    )

# Precompile a regex machine to recognize word separators. For
# simplicity, we accept any non-letter to be a word separator.

word_separators = re.compile("[^a-z]+")

# The dictionary of words that we shall build up as we see them.

words = {}

with open('warandpeace.txt', encoding="utf-8") as wap:
    for line in wap:
        if len(line) < 2:  # skip empty lines
            continue
        # Lowercase the line and remove the trailing linebreak character.
        line = line.lower()
        if line[-1] == '\n':
            line = line[:-1]
        # Remove the contractions (see above).
        for (orig, repl) in replacements:
            line = line.replace(orig, repl)
        # Remove whatever other contractions might remain.
        # Raw strings are handy for regexes.
        line = re.sub(r"'s\b", "", line)
        line = re.sub(r"'ll\b", " will", line)
        # Process the individual words in the line.
        for word in word_separators.split(line):
            if len(word) > 0:
                words[word] = words.get(word, 0) + 1

print("Here are some individual word counts.")
for w in ('prince', 'russia', 'you', 'supercalifragilisticexpialidocious'):
    print(f"The word {w!r} occurs {words.get(w, 0)} times.")

# Turn a dictionary into a list of its items as (value, key) tuples.
# Dictionary method items() produces sequence of (key, value) pairs,
# but swapping these is trivial with a list comprehension.
words_list_f = [(c, w) for (w, c) in words.items()]
# Sorting the list of pairs of the form (count, word). Python tuple
# comparison happens lexicographically, so the primary sorting criteria
# is the count. Words of equal frequency then get sorted according to
# their dictionary order.
words_list_f = sorted(words_list_f, reverse=True)
# Extract the sorted words into a separate list, dropping the counts.
words_list = [w for (c, w) in words_list_f]

print("\nThe 300 most frequent words in War and Peace are:")
print(", ".join(words_list[:300]))

once = list(reversed([w for w in words_list if words[w] == 1]))
print(f"\n{len(once)} words occur exactly once in War and Peace:")
print(", ".join(once))

#output as such
# =============================================================================
#Here are some individual word counts.
#The word 'prince' occurs 1928 times.
#The word 'russia' occurs 173 times.
#The word 'you' occurs 3801 times.
#The word 'supercalifragilisticexpialidocious' occurs 0 times.

#The 300 most frequent words in War and Peace are:
#the, and, to, of, a, he, in, that, his, was, with, not, it, had, her, him, at,
#i, but, as, on, you, for, she, is, said, all, from, be, were, by, what, they,
# who, one, this, which, have, pierre, prince, so, an, will, up, do, there, them,
# or, when, did, been, their, no, are, would, now, only, if, me, out, my, natasha,
# man, andrew, could, we, more, himself, about, how, into, then, time, princess,
# face, french, went, some, know, after, old, before, eyes, your, very, men, rostov,
# room, thought, go, like, well, see, count, moscow, began, again, has, down, come,
# came, still, mary, asked, without, army, same, can, those, am, looked, say,
# nicholas, first, felt, emperor, where, our, another, life, away, left, something,
# over, two, such, these, seemed, napoleon, other, head, just, its, day, yes, people,
# little, long, why, hand, should, than, whole, kutuzov, back, even, general, own,
# here, heard, good, having, way, because, countess, must, look, nothing, any,
# always, saw, being, made, though, russian, love, right, sonya, young, officer,
# father, suddenly, denisov, round, off, moment, voice, us, everything, smile,
# looking, knew, told, never, whom, let, while, took, house, words, much, too,
# turned, dear, through, quite, tell, chapter, under, think, once, get, battle,
# soldiers, take, evidently, understand, yet, last, sat, every, door, dolokhov,
# herself, already, most, feeling, going, oh, might, god, behind, place, stood,
# gave, horse, done, others, replied, expression, side, commander, war, position,
# wife, order, boris, anna, toward, anything, seen, new, may, give, three, make,
# son, put, petya, also, great, front, enemy, ran, chief, troops, hands, both,
# shall, talk, soon, want, mother, horses, petersburg, called, shouted, does,
# vasili, taken, alone, between, word, whether, saying, part, many, things,
# officers, thing, letter, everyone, regiment, mind, along, night, table, sent,
# during, t, rode, against, anatole, sitting, found, entered, question, moved,
# morning, evening

#5847 words occur exactly once in War and Peace:
#aah, ab, abacus, abandons, abasement, abbreviations, abc, abdicate, abductors,
# abhorrence, abnormal, abnormally, abodes, abolishing, abolition, abominably,
# abounding, aboveboard, abramovna, absentees, absolved, absorb, abstemious,
# abstention, abstiens, absurdly, abundantly, academy, accelerate, accents,
# accentuated, acceptance, access, accidently, acclaimed, accommodate,
# accommodated, accomplishing, accomplishments, accorded, accoucheur, accouterments,
# accrue, accumulated, accusers, accusing and etc ...
