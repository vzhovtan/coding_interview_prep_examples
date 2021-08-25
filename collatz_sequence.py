"""
Find the Collatz sequence starting from given positive integer
Starting with any positive integer N, Collatz sequence is defined corresponding to n as the numbers formed by the following operations:
- If n is even, then n = n / 2.
- If n is odd, then n = 3*n + 1.
- Repeat above steps, until it becomes 1.
"""

def printCollatz(n): 
    # We simply follow steps while we do not reach 1 
    while n != 1: 
        print(n, end = ' ') 
        # If n is odd  
        if n & 1: 
            n = 3 * n + 1
        # If even  
        else: 
            n = n // 2
    # Finally, print 1 at the end  
    print(n) 
  
# Driver code  
printCollatz(41) 