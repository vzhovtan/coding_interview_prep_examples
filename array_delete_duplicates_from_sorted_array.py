"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new array.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""

# pythonic way - returning the modified array
def delete_duplicates_pythonic(arr):
    result = list(set(arr))
    return result

# without python tools - simple deletion - returning modified array - remove
def delete_duplicates(arr):
    idx = 1
    for item in arr:
        if arr[idx -1] != item:
            arr[idx] = item
            idx += 1
    return arr[:idx]

# two pointers solution - returned length
def delete_duplicates_pointers(nums):
    next_non_dup = 1
    idx = 1
    while idx < len(nums):
        if nums[next_non_dup-1] != nums[idx]:
            nums[next_non_dup] = nums[idx]
            next_non_dup += 1
        idx += 1    
    return next_non_dup

# driver code
print(delete_duplicates_pythonic([0, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]))
print(delete_duplicates([0, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]))
print(delete_duplicates_pointers([0, 1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9]))