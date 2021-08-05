"""
Split the give array so the sum of fist half is equal to the sum of second half
Example
arr = [5, 2, 3]
output = [[5],[2,3]], True
arr = [4, 2, 3]
output = False
"""

def split_arr(arr):
    if len(arr) <= 1:
        return False

    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i:]):
            print(arr[:i], arr[i:])
            return True

    return False

# driver code
a = [2, 2, 1, 1, 1, 1]
b = [2, 3, 4]
print(split_arr(a))
print(split_arr(b))


