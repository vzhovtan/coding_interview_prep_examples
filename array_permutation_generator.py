"""
Permutation is an arrangement of objects in a specific order. Order of arrangement of object is very important. 
The number of permutations on a set of n elements is given by  n!.  
For example, there are 2! = 2*1 = 2 permutations of {1, 2}, namely {1, 2} and {2, 1}, 
and 3! = 3*2*1 = 6 permutations of {1, 2, 3}, namely {1, 2, 3}, {1, 3, 2}, {2, 1, 3}, {2, 3, 1}, {3, 1, 2} and {3, 2, 1}
"""

def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

# A generator for the creation of k-permuations of n objects looks very similar to previous permutations generator:

def k_permutations(items, n):
    if n==0: 
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n-1):
                if item not in kp:
                    yield [item] + kp
                    
# driver code
for p in permutations(['r','e','d']): 
    print(''.join(p))

for kp in k_permutations("abcd", 3):
    print(kp) 