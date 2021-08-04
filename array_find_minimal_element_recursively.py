"""
Find a minimal element without Python tools recursively
"""

def find_min(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        cur_min = find_min(arr[1:])
        print(arr[1:])
        print(arr[0], cur_min)
        return cur_min if cur_min < arr[0] else arr[0]

# driver code
arr = [1, -5, 7, 70, 80, 30, 22, 18, 27, 3, 40, 50]
print(find_min(arr))