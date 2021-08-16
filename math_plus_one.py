"""
Create a function to add 1 to the integer given as array
"""

def plusone(digit):
    for idx in range(len(digit)-1, -1, -1):
        curr_number = digit[idx]
        if curr_number < 9:
            digit[idx] = curr_number + 1
            break
        else:
            digit[idx] = 0

    digit.insert(0, 1)    
    return digit

# driver code
dig = [9, 9, 9, 9]
print(plusone(dig))