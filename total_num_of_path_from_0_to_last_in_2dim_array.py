"""
Given a two dimensional array, find total number of possible paths from top-left cell to 
bottom-right cell if we are allowed to move only rightward and downward.
"""

def count_path(i, j):
    #base
    if i == 0 and j == 0:
        return 0

    if i == 0 or j == 0:
        return 1

    return count_path(i-1, j) + count_path(i, j-1)

# driver code
print(count_path(7, 7))         
