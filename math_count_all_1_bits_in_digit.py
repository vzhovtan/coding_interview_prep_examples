"""
Create a function to count all 1 bits in binary represenation of given decimal interger
"""

def count_bits(x):
    res = 0
    print(x)
    while x: 
        res += x&1 
        x >>= 1
    return res

# driver code
a = 15
print(count_bits(a))