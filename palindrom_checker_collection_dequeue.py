"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
For example,
"A man, a plan, a canal: Panama" is a palindrome. "race a car" is not a palindrome.
"""

import collections

def checker(s):
    if len(s) == 0:
        return False
    elif len (s) == 1:
        return True    
    else:
        palindrom = True
        qu = collections.deque(s)
        print(qu)

        while len(qu) > 1:
            if qu.pop() != qu.popleft():
                palindrom = False

        return palindrom

# driver code
print(checker("raddar"))                