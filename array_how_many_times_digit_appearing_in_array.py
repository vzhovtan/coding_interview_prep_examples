"""
find how many time digit appeared in array [0,... N] with lenght of len_array 
eg: in 0..20 digit 2 will be appearing as 2, 12, 20
"""

import math

def find_occurences(len_array, digit):
    result = 0
    result_array = []
    iter = digit
    while iter <= len_array:
        if iter % 10 == digit:
            result += 1
            result_array.append(iter)

        if math.floor(iter/10) == digit:
            result += 1
            result_array.append(iter)

        iter += 1    
    return result, result_array    

# driver code
len_arr = 30
n = 2
print(find_occurences(len_arr, n))