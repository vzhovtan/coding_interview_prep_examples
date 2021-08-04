"""
Given an integer array and an integer K, find the number of sub array in which all elements are less than K.
"""

from itertools import combinations

def get_sub_array_sizes(a: [int], k: int):
    sub_size = 0
    for v in a:
        if v < k:
            sub_size += 1
        else:
            if sub_size > 0:
                yield sub_size
            sub_size = 0

    if sub_size > 0:
        yield sub_size


# Count the number of max size sub array with all elements less than K
# For the example above, sub array are: [1,2,3], [4, 5], [7].  num = 3
def num_sub_arrays(a: [int], k: int) -> int:
    return sum(1 for i in get_sub_array_sizes(a, k))


# number of non overlapping interval pairs in a range(n)
# e.g. range(1,3) can produce the following pairs:
# [[1,(2,3)], [1, 2], [1,3], [(1,2), 3], [2,3]
# for the total of 5 pairs
def num_range_interval_pairs(n: int) -> int:
    return sum((i + 1) * (n - i - 1) * (n - i) / 2 for i in range(n))


# Number of non overlapping subarray pairs size > 0 with all elements < K
def num_outer_sub_array_pairs(a: [int], k: int) -> int:
    return sum(a * (a+1)/2 * b * (b+1)/2
               for a, b in combinations(get_sub_array_sizes(a, k), 2))


def num_inner_sub_array_pairs(a: [int], k: int) -> int:
    return sum(num_range_interval_pairs(a) for a in get_sub_array_sizes(a, k))


def num_sub_array_pairs(a: [int], k: int) -> int:
    return num_inner_sub_array_pairs(a, k) + num_outer_sub_array_pairs(a, k)

# driver code
K = 10
a = [1, 2, 3, 11, 4, 5, 12, 13, 7]
print(num_sub_arrays(a, K))
print(num_sub_array_pairs(a, K))