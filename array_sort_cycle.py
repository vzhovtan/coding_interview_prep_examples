"""
Cycle sort
"""

def cycle(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        print(arr[i], arr[j])
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    return arr

# driver code
arr = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
print(arr)
print(cycle(arr))