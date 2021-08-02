"""
Dutch flag problem
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
"""

def ducth_three_buckets(arr):
    buck0, buck1, buck2 = [], [], []
    for i in arr:
        if i == 0:
            buck0.append(i)
        elif i ==1:
            buck1.append(i)
        else:
            buck2.append(i)
    result = buck0 + buck1 + buck2
    return result

# driver code
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]     
print(ducth_three_buckets(arr)) 
