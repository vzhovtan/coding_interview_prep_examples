"""
Create a function to reverse digits of given integer.
Example 1:
Input: 123
Output: 321
"""
import math

def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result

def rev (x):
    negate = False
    if x < 0:
        x = -x
        negate = True
    
    res = 0
    while x != 0:
        res = res * 10 + x % 10
        print(res)
        x = math.floor(x/10)
    
    if negate:    
        res = -res
    return res

#driver code    
print(reverse(1044567890987654))
print (rev(1044567890987654))