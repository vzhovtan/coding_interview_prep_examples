"""
Sum of the array recursiely
"""

def sum_array(arr):
    sum = 0
    if len(arr) == 1:
        return arr[0] + sum
    else:
        print(arr[1:])
        return arr[0] + sum + sum_array(arr[1:])    

# driver code
arr = [1, -5, 7, 10, 2, 30, 22, 18, 27, 3, 40, 50]
print(sum_array(arr))