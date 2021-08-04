"""
Given an array and a number K where K is smaller than size of array, we need to find the 
K’th smallest element in the given array. It is given that all array elements are distinct.
Examples:
Input: arr=[7, 10, 4, 3, 20, 15]
K = 3
Output: 7

Input: arr=[7, 10, 4, 3, 20, 15]
K = 4
Output: 10

TIPS: use heapq module from  STL
heapq.nsmallest(n, iterable, key=None)
"""

def smallest_elem_1(arr, k):
    return sorted(arr)[k-1]

def smallest_elem_2(arr,k):
    j = len(arr)
    while j >= 0:
        for i in range (0,j-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        j -= 1
    return arr[k-1]    

# driver code
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(smallest_elem_1(arr,k))
print(smallest_elem_2(arr,k))    