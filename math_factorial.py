"""
Recursive function to calculate factorial
"""

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

# driver code
print(factorial(50)) 