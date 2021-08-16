"""
Create a function to add 2 binary numbers given as stings
"""

from itertools import zip_longest

def add(a, b):
    def gen_add():
        c = 0
        for i, j in zip_longest(reversed(a), reversed(b), fillvalue='0'):
            n = (ord(i) - ord('0')) + (ord(j) - ord('0')) + c
            yield chr(ord('0') + n % 2)
            c = n // 2
        if c:
            yield chr(ord('0') + c)
    
    return ''.join(reversed(list(gen_add())))

# driver code
print(add('101101', '111101'))