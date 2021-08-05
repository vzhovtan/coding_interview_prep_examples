"""
Dutch flag problem
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
"""

# Function to sort array 
def part_it(a, arr_size): 
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi: 
        if a[mid] == 0: 
            a[lo], a[mid] = a[mid], a[lo] 
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[hi] = a[hi], a[mid]  
            hi = hi - 1
    return a 
        
# driver code
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
arr_size = len(arr) 
print(part_it(arr, arr_size))