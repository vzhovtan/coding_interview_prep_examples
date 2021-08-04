"""
Find subarray with max sum
"""

import itertools

def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
        print(max_sum, min_sum)

    return max_sum


# driver code
arr = [1, 4, -2, 10, 2, -10, 1, -1, 20]
print(find_maximum_subarray(arr))