"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting  with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
For instance, 13 is a happy number because  1**2 + 3**2 = 10  and 1**2 + 0**2 = 1
"""

def isHappy(n):
    k = n
    while n != 1:
        n = str(n)
        sum_square = 0
        for i in n:
            sum_square += int(i) ** 2
        n = sum_square
        print(n)
        if k == n:
            return False
    return True

# driver code
print(isHappy(4))

