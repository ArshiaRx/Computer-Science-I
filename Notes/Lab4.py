# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:07:13 2021

@author: Arshia.Rahim
"""

def squares_intersect(s1, s2):
    (x1, y1, r1) = s1
    (x2, y2, r2) = s2
    disjoint = (x1 + r1 < x2 or x2 + r2 < x1 or y1 + r1 < y2 or y2 + r2 < y1)
    return not disjoint

def turkey_ninthers(items):
    while len(items) > 1:
        items = [sorted(items[i:i+3])[1] for i in range(0, len(items), 3)]
    return items[0]


_vowels = 'aeioAEIOU'
def reverse_vowels(text):
    vowels, result = [c for c in text if c in _vowels], ""
    for c in text:
        if c in _vowels:
            ch = vowels.pop()
            ch = ch.upper() if c.isupper() else ch.lower()
            result += ch
        else:
            result += c
    return result