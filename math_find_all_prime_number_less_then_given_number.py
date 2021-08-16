"""
Count the number of prime numbers less than a non-negative number, n.
"""

def countPrimes(n):
    count = 0
    for num in range(2, n):
        for i in range(2, num):
            print(num, i)
            if (num % i) == 0:
                break
        else:
            count += 1

    return count

# driver code
print(countPrimes(10)) # 4

