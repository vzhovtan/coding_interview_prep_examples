"""
Find a row in a 2 dimensional matrix with maximal amount of 1
"""

def find_row(arr):
    for i in range(1, len(arr)):
        print(i, arr[i])
        if sum(arr[i]) > sum(arr[i-1]):
            index = i
        else:
            index = i-1
    print(index)           

# driver code
data = [[0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]]

find_row(data)    