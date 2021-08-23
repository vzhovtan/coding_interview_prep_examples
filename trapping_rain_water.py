"""
Given an array arr[] of N non-negative integers representing height of 
blocks at index i as Ai where the width of each block is 1. 
Compute how much water can be trapped in between blocks after raining.
Structure is like below:
| |
|_|
We can trap 2 units of water in the middle gap.
"""

def max_water(arr, n):
    res = 0
    # For every element of the array 
    for i in range(1, n - 1): 
        # Find the maximum element on its left 
        left = arr[i] 
        for j in range(i) :
            left = max(left, arr[j]) 
         
        # Find the maximum element on its right 
        right = arr[i] 
        for j in range(i + 1 , n) : 
            right = max(right, arr[j])
             
        # Update the maximum water
        res = res + (min(left, right) - arr[i]) 
    return res 

# driver code
bars1 = [3, 0, 2, 0, 4]
bars2 = [1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1]
n = len(bars1)
m = len(bars2)
print(max_water(bars1, n))
print(max_water(bars2, m))