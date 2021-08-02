"""
Counting elements in the array recursively
"""

def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

# driver code
arr = [1, -5, 7, 70, 80, 30, 22, 18, 27, 3, 40, 50]
print(count(arr))    