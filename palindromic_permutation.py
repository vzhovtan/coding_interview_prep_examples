"""
Create a function to checkif the given string can be permutated to form a palindrom
"""

import collections

def can_form_palindrome(s) : 
    # A string can be permuted to form a palindrone if and only if the number # of chars whose frequencies is odd is at most 1. 
    return sum (v % 2 for v in collections.Counter(s).values()) <= 1

# driver code
string = "edified"
print (can_form_palindrome(string))

