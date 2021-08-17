"""
heapify function from "Inroduction to Algorithm"
"""

def left(i):
    return 2*i

def right(i):
    return 2*i +1

def parent(i):
    return i/2

def heapify(arr, i):
    l = left(i)
    r  = right(i) 
    if l <= len(arr)-1 and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= len(arr)-1 and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

    return arr

# driver code
arr = [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
for i in range(len(arr)//2, -1, -1):
    heapify(arr, i)

print(arr)