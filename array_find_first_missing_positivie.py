"""
Find first positive element missed in unsorted array

Example:
for given array [3,5,4,1,5,1,-2,0,1] first missed positive element is 2
"""

def first_missing_positive(arr):
    arr.sort()
    print(arr)
    for i in range (len(arr)-1):
        if arr[i] > 0 and arr[i-1] > 0 and (arr[i]-arr[i-1]) >= 2:
            return arr[i-1]+1
    return arr[-1]+1    

def first_missing(int_list):
    if len(int_list) == 0:
        return 1
        
    int_list.sort()
    smallest_int = 0
    
    for i in range(len(int_list) - 1):
        if int_list[i] <= 0 or int_list[i] == int_list[i + 1]:
            continue
        else:
            if int_list[i + 1] - int_list[i] != 1:
                smallest_int = int_list[i] + 1
                return smallest_int
    
    if smallest_int == 0:
        smallest_int = int_list[-1] + 1

    return smallest_int

# driver code
arr = [3,5,4,1,5,1,-2,0,1]
print(first_missing_positive(arr))
print(first_missing(arr))