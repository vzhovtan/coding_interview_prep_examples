"""
We are given a set of nnn positive integers and we have to find all the possible subsets of integers that sum up to a number KKK
arr = [1, 3, 5, 21, 19, 7, 2]
K = 10
solution = (3,7), (3,5,2), (1,7,2)
"""

import itertools

def solution_pythonic(arr):
    result = []
    print(len(arr))
    for i in range(1, len(arr)):
        for item in itertools.combinations(arr, i):
            if sum(item) == 10:
                result.append(item)
    return result            

# dirver code
arr = [1, 3, 5, 21, 19, 7, 2]
print(solution_pythonic(arr))
