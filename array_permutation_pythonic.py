"""
Permutation is an arrangement of objects in a specific order. Order of arrangement of object is very important. 
The number of permutations on a set of n elements is given by  n!.  
For example, there are 2! = 2*1 = 2 permutations of {1, 2}, namely {1, 2} and {2, 1}, 
and 3! = 3*2*1 = 6 permutations of {1, 2, 3}, namely {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2, 1}
There is pythonic solution using itertools
"""

import itertools

def pythonic_permutations(A):
    answer = list(itertools.permutations(A))
    return answer

# driver code
arr = [1, 2, 3]
print("Pythonic \n", pythonic_permutations(arr), "\n")
