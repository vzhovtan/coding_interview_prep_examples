"""
In the board game, a player has to try to advance through a sequence of positions. 
Each position has a nonnegative integer associated with it, representing the maximum you can advance from that position in one move.
Write a program which takes an array of integers, where A[i] denotes the maximum you can advance from index , 
and returns whether it is possible to advance to the last index starting from the beginning of the array
"""

def furthest(arr):
    i, largest, last = 0, 0, len(arr)-1

    while largest >= i and largest < last:
        largest = max(largest, i + arr[i])
        # print("i is", i, "largest is", largest, "arr[i] is", arr[i])
        i += 1

    return largest == len(arr)-1  

# driver code
input_array_1 = [2, 4, 1, 1, 0, 1, 3]
input_array_2 = [2, 4, 1, 1, 0, -2, 3]
print(furthest(input_array_1))
print(furthest(input_array_2))