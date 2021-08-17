"""
Filed and solution created with 2 lines/rows more to accomodate range functionality
Compose a program that takes three arguments m, n, and p and produces an m-by-n boolean array where each element is occupied with probability p. 
In the minesweeper game, occupied cells represent bombs and empty cells represent safe cells. Write the array using an asterisk for 
bombs and a period for safe cells. 
Then, replace each safe square with the number of neighboring bombs (above, below, left, right, or diagonal) and write the result
"""
import random

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
field, solution = create_field(4, 0.5)
for line in field:
    print(line)

for line in solution:
    print(line)