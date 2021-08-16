"""
Creeate a function to calculate log2 of the given integer
"""

def log2(n):
    if(n == 1):
        return 0
    else:
        print(n//2)
        return 1 + log2(n//2)

# driver code
print(log2(8))