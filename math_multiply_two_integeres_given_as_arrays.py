"""
Create a function to multiply 2 integers given as array of numbers
"""

def multi(a, b):
    result = [0 for x in range(len(a)) for x in range(len(b))]
    print(result)
    for idx_a, _ in enumerate(reversed(a)):
        for idx_b, _ in enumerate(reversed(b)):
            result[idx_a + idx_b + 1] += a[idx_a] * b[idx_b] 
            result[idx_a + idx_b] += result[idx_a + idx_b + 1] // 10 
            result[idx_a + idx_b + 1] %= 10
    return result

# driver code
a = [1, 1]
b = [2, 2]
print(multi(a, b))