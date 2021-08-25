"""
Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Match nuts and bolts efficiently. 
Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. 
It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.
Other way of asking this problem is, given a box with locks and keys where one lock can be opened by one key in the box. We need to match the pair.

Input : nuts=['@', '#', '$', '%', '^', '&']
        bolts=['$', '%', '&', '^', '@', '#']
Output : Matched nuts and bolts are-
        $ % & ^ @ # 
        $ % & ^ @ # 
Algo:
Traverse the nuts array and create a hashmap
Traverse the bolts array and search for it in hashmap.
If it is found in the hashmap of nuts then this means bolts exist for that nut.
"""

def find_match(nuts, bolts, n):
    map1 = {}
    for i in range(n):
        map1[nuts[i]] = i
    print(map1)

    for i in range(n):
        if bolts[i] in map1.keys():
            map1[bolts[i]] = bolts[i]
    print(map1)            

# driver code
nuts=['@', '#', '$', '%', '^', '&']
bolts=['$', '%', '&', '^', '@', '#']
n = len(nuts)
find_match(nuts, bolts, n)
