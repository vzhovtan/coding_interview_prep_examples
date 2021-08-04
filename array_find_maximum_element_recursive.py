"""
Returns max element in the array recursively
"""

def find_max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        return arr[0] if arr[0] > find_max(arr[1:]) else find_max(arr[1:])  


# driver code
array = [1, -5, 7, 70, 80, 30, 22, 18, 27, 3, 40, 50]
print(find_max(array))    