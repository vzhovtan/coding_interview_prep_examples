"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""

def removeDuplicates(nums):
    # two pointers solution 
    next_non_dup = 1
    idx = 1
    while idx < len(nums):
        if nums[next_non_dup-1] != nums[idx]:
            nums[next_non_dup] = nums[idx]
            next_non_dup += 1
        idx += 1    
    return next_non_dup

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,2,2]))
