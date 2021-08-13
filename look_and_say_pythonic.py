"""
Having sequence like
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211
The first term is "1"
Second term is "11", generated by reading first term as "One 1" (There is one 1 in previous term)
Third term is "21", generated by reading second term as "Two 1"
Fourth term is "1211", generated by reading third term as "One 2 One 1" 
"""

import itertools
# itertools.groupby(iterable, key=None)
# Make an iterator that returns consecutive keys and groups from the iterable

def look_say_pythonic(n):
    s = "1"
    for _ in range(n-1):
        s = "".join(str(len(list(group))) + key for key, group in itertools.groupby(s))
        print(s)
    return s    

# driver code
print(look_say_pythonic(11))