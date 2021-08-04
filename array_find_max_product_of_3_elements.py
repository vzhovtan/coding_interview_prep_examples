"""
Given a list of integers, return the largest product  that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we 
should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

def largest_product1(arr): 
    arr.sort()
    return max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])

def largest_product2(l):
    maximum = l[1]
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(i+2, len(l)):

                maximum = max(l[i] * l[j] * l[k], maximum)

    return maximum

# driver code
print(largest_product1([-10, -10, 5, 2]))
print(largest_product1([-10, -1, 5, 2]))
print(largest_product1([-1, -1, 5, 2, 8, 10, 100]))

print(largest_product2([-10, -10, 5, 2]))
print(largest_product2([-10, -1, 5, 2]))
print(largest_product2([-1, -1, 5, 2, 8, 10, 100]))