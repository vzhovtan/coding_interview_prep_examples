"""
Create a function to build minefiled with provided size and put provided and put of mines randomly
"""
import random

def buidl_minefiled(field_size, mines):
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

# driver code
size = 7
mines = 5
built_field = buidl_minefiled(size,mines)
for i in built_field:
    print(i, end ="\n")

"""
Iterate over created minefiled add sum of all mines around to cells
"""

def count_mines(field, field_size):
    new_field = [[0 for x in range (field_size)] for x in range (field_size)]
    for i in range(1, field_size-1):
        for j in range (1, field_size-1):  
                new_field[i][j] = field[i-1][j-1] + field[i-1][j] + field[i-1][j+1] + \
                    field[i][j-1] + field[i][j] + field[i][j+1] + \
                        field[i+1][j-1] + field[i+1][j] + field[i+1][j+1]
    return new_field

counted_mines = count_mines(built_field, size)
print()
for i in counted_mines:
    print(i, end ="\n")

