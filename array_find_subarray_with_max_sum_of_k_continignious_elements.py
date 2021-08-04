"""
Given an array arr[] of size N and an integer K. Find the maximum for each and 
every contiguous subarray of size K
"""

def maxSum(arr, k):
    max_sum = 0
    n = len(arr)

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        max_sum = max(current_sum, max_sum)

    return max_sum

def find_max_subarrays(arr, n, k):
    for i in range(n-1):
        if i+k <= n:
            subarray = arr[i:i+k]
            max_subarray = sum(subarray)
            print("Subarray ", subarray, " Max ", max_subarray)

# driver code
arr = [1, 4, -2, 10, 2, -10, 1, -1, 20]
n = len(arr)
k = 3
find_max_subarrays(arr, n, k)
print(maxSum(arr, k)) 
