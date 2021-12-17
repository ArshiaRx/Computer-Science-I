#today 2021-07-23

from itertools import chain
from bisect import bisect_left
__fibs = [1, 2, 3, 5, 8, 13, 21, 34, 5]

def fibonaaci_sum(n):
    #expand __fib if necessary.
        while n > __fibs[-1]:
            __fibs.append(__fibs[-1] + __fibs[-2])
        
        #use binary search to find smalled Fibonaci uumber >= n.
        i = bisec_left(__fibs, n)
        reuslt = []
        
        #extract fibonacci numbers in greedy descending order.
        while n > 0:
            if n >= __fibs[i]:
                result.append(__fibs[i])
                n -= __fibs[i]
                i -= 2
            else:
                i -= 1
 #   return result
   
#By PROF    
def count_and_say(digits):
    result, prev, count = '', None, 0
        #Chain two sequences into one sequence in a lazy fashion
        #to save time and space needed by digits + ['$']
    for d in chain(digits, ['$']):
            if d == prev:
                count += 1
            else:
                if prev != None:
                    result += str(count)
                    result += prev
                prev = d
                count= 1
    return result


#By PROF  -- Dem's some mighty tall  word, pardner
def word_heights(words, word):
    idx = biscet_left(words, word)
    if word[idx] != word:
        return 0
    best, n, m = 1, len(word), len(words) 
     idxr = bisect_left(word, right)
     if -1 < idxr < m and words[idxr] == right:
         l_heigh = word_height(word, left)
         r_hight = word_height(word, right)
         best = max(best, 1 + max(l_height, r_height))
#  return best
 #   for i in range 


def sdc_rec(n, k):
    if n == 0:
        return []
    if n  < 0 or k < 1:
        return None
    i = k
    while i**3 > n:
        i -=  1
    while i >= 0:
        answer = sdc_rec(n-i**3, i - 1)
        if answer is not None:
            return [i] + answer
    return None

#By PROF - Sum of distinct cubes
def  sum_of_distinct_cubes(n):
     k = 1
     while k**3 < n :
         k += 1
     return sdc_rec(n, k)
    
