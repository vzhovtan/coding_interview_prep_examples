"""
Given an integer, create a function to determine if it is a power of three.
Tips: The maximum power of 3 value that integer can hold is 1162261467 ( 3^19 ) in 32-bits integer
"""

def isPowerOfThree(n):
    while n  > 3:
        n = n / 3
    return n == 1 or n == 3

def check(n):
    if n != 0:
        return 1162261467 % n == 0
    else:
        return False    

# driver code 
print(isPowerOfThree(27)) #true
print(isPowerOfThree(45)) #false
print(isPowerOfThree(0)) #false

print(check(27))
print(check(45))
print(check(0))