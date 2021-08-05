"""
Recursive binary search
"""

def binary(array, item, left, right):
    if right < left:
        return -1

    middle = left + (right-left)//2
    print("Middle index", middle)

    if array[middle] == item:
        return middle

    elif array[middle] > item:
        print("Checking left")
        return binary(array, item, left, middle-1)

    elif array[middle] < item:
        print("Checking right")
        return binary(array, item, middle+1, right)    

# driver code
data = [x for x in range(0, 100, 3)]
print(binary(data, 27, 0, len(data)-1))    