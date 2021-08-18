"""
Given an array of positive integers. The task is to find the size of the 
smallest subset such that the Bitwise OR of that subset is Maximum possible

Current implementation found max Bitwise OR for every subset with 2 items
"""

def find_subset(arr):
    res = 0
    for i in range(len(arr)):
        for j in range (i+1, len(arr)):
            # print(arr[i], arr[j], arr[i]|arr[j])
            res = max(res, arr[i]|arr[j])
    return res    

# driver code
arr = [2, 6, 2, 8, 4, 5]
print(find_subset(arr))