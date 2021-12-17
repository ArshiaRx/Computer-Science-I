# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 19:56:13 2021

@author: Arshia.Rahim
"""

my_list = [x for x in range(1, 10)]

def process_list(my_list):
    for i in range(len(my_list)):
        my_list = my_list[i] * 3
    return my_list

process_list(my_list)
#my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#len(my_list) --> 9
#my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]

def last(s):
    count, last = 0 , s[-2:]
    for i in range(len(s) - 1):
        if s[i:i+2] == last:
            count += 1
        return count