"""
Filed and solution created with 2 lines/rows more to accomodate range functionality
Compose a program that takes three arguments m, n, and p and produces an m-by-n boolean array where each element is occupied with probability p. 
In the minesweeper game, occupied cells represent bombs and empty cells represent safe cells. Write the array using an asterisk for 
bombs and a period for safe cells. 
Then, replace each safe square with the number of neighboring bombs (above, below, left, right, or diagonal) and write the result
"""

import random

# first variation
def create_field(m, p):
    field = [["." for x in range(m+2)] for y in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            if random.random() < p:
                field[i][j] = "x"

    solution = [[0 for x in range(m+2)]for y in range(m+2)]
    for i in range(1, m+1):
        for j in range(1, m+1):
            # print(i, j)
            for ii in range(i-1, i+2):
                # print("II", ii)
                for jj in range(j-1, j+2):
                    # print("JJ", jj)
                    # print("curr field" , field[ii][jj])
                    if field[ii][jj] == "x":
                        solution[i][j] += 1

    return field, solution

# driver code
print("first variation\n")
field, solution = create_field(4, 0.5)
for line in field:
    print(line)
print()
for line in solution:
    print(line)

# second variation
def buidl_minefield(field_size, mines):
    field = [[0 for x in range (field_size)] for x in range (field_size)]
    # for i in field:
    #     print(i, end ="\n")
    while mines > 0:
        row = random.randrange(1, field_size-1)
        col = random.randrange(1, field_size-1)
        if field[row][col] == 0:
            field[row][col] = 1
            mines -= 1
    return field        

#Iterate over created minefiled add sum of all mines around the cells to the cell itself

def count_mines(field, field_size):
    new_field = [[0 for x in range (field_size)] for x in range (field_size)]
    for i in range(1, field_size-1):
        for j in range (1, field_size-1):  
                new_field[i][j] = field[i-1][j-1] + field[i-1][j] + field[i-1][j+1] + \
                    field[i][j-1] + field[i][j] + field[i][j+1] + \
                        field[i+1][j-1] + field[i+1][j] + field[i+1][j+1]
    return new_field

# driver code
size = 7
mines = 5
print("\nsecond variation\n")
built_field = buidl_minefield(size,mines)
for i in built_field:
    print(i, end ="\n")

counted_mines = count_mines(built_field, size)
print()
for i in counted_mines:
    print(i, end ="\n")

