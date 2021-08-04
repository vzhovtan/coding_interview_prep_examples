"""
Given an array and a number K where K is smaller than size of array, we need to find the 
K’th greatest element in the given array. It is given that all array elements are distinct.
Examples:
Input: arr=[7, 10, 4, 3, 20, 15]
K = 2
Output: 4

TIPS: use heapq module from  STL
heapq.nlargest(n, iterable, key=None)
"""

def greatest_elem_2(arr, n, k):
    if n == k:
        return

    for i in range(n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr[-1])
    arr.pop(-1)
    greatest_elem_2(arr, n-1, k) 

# driver code
arr = [7, 10, 4, 3, 20, 15]
k = len(arr)-1-2 # 2 is K
n = len(arr)-1 # n is lenght of the array
greatest_elem_2(arr, n, k)