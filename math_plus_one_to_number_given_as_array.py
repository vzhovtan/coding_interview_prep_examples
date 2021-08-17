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

"""
We're given a list of digits, and the idea here is to convert that list to an integer, num. 
So each digit is multiplied by the proper place value and added to num. For example, 
if digits = [3, 8, 2, 5] then on the first iteration 3 is multiplied by 10 to the power of 4-1-0 = 3, 
so this results in 3000, which is added to num. Then 8 is multiplied by 10^2 and added to num, and so on.
The last step is to add 1 to num, convert it to a list and return that list.
"""

def plus_one(digits):
    num = 0
    for i in range(len(digits)):
    	num += int(digits[i]) * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

# driver code
dig = [9, 9, 9, 9]
print(plus_one(dig))