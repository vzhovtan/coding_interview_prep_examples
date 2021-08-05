"""
Rotation of the original array over K element
For example, rotation over 5 element is:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9, 0, 1, 2, 3, 4
"""
def rotate(arr, k):
    for _ in range(k):
        arr.insert(0, arr.pop())  

# driver code
arr = [ x for x in range(10)]
print("original", arr)
k = 5
rotate(arr, k)
print("rotated", arr)
