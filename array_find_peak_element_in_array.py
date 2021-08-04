"""
Given an array of integers. Find a peak element in it. 
An array element is a peak if it is NOT smaller than its neighbours. 
For corner elements, we need to consider only one neighbour.
EG:
Input: array = [10, 20, 15, 2, 23, 90, 67]
Output: 20 or 90
The element 20 has neighbours 10 and 15, 
both of them are less than 20, similarly 90 has neighbous 23 and 67.
"""

def find_peak(arr):
    res = []
    if arr[0] > arr[1]:
        res.append(arr[0])
    if arr[-1] > arr[-2]:
        res.append(arr[-1])
    for i in range(len(arr)-2):
        if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
            res.append(arr[i+1])

    return res

# driver code
array = [10, 20, 15, 2, 23, 90, 67]
print(find_peak(array))
