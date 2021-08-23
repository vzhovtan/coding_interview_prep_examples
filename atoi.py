"""
Implement atoi which converts a string to an integer.

- The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this 
character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
- The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of 
this function.
- If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty 
or it contains only whitespace characters, no conversion is performed.
- If no valid conversion could be performed, a zero value is returned.

Note:
- Only the space character ' ' is considered as whitespace character.

Possible additional limitation is:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
If the numerical value is out of the range of representable values, INT_MAX (231 − 1)  or INT_MIN (−231) is returned.

Examples:
Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit  signed integer. Hence, INT_MIN (−231) is returned.
"""

def atoi_1(str):  
    number = ""
    ints = "0123456789"
    flag = False
    for char in str:
        if char == " " and flag == True:
            break
        elif char == " " and number == "":
            continue
        elif char == "-" and number == "" and flag == False:
            number += "-"
            flag = True
        elif char == "+" and number == "" and flag == False:
            number == ""
            flag = True
        elif char in ints:
            number += char
        else: 
            break
    
    if number == "" or number == "-" or number == "+":
        return 0
    elif int(number) < ((2 ** 31)*-1):
        number = ((2 ** 31)*-1)
        return number
    elif int(number) > 2 ** 31 - 1:
        number = 2 ** 31 - 1
        return number
    elif number.startswith("-") and number[1:].isdigit():
        return int(number)
    else: 
        return int(number) 
                
def atoi_2(str):
    """    
    The key point is to check for overlflow. For 32-bit integer we can use limit as 2**31
    If given limit 2**31 we can do limit % 10 and final % 10 and check if final % 10 less than limit % 10
    """
    new_data = str.strip().replace(" ", "")
    final = 0
    for index, value in enumerate(new_data[::-1]):
        if value.isdigit():
            #  print(index, value)
            #  print(type(index), type(value))
            final += int(value) * 10**index
        elif value == "-":
            final = -final   
    return final

def atoi_3(str):
    # pythonic one - in case there is no alphabet chars in given str
    # flexible with using base
    new_data = str.strip().replace(" ", "")
    outcome = int(new_data, base=10)
    return outcome

# driver code
print(atoi_1("-91283472332"))
print(atoi_1(" + 420"))
print(atoi_1("  -420"))
print(atoi_1(" w  -420"))
print(atoi_1("420"))
print()
print(atoi_2("-91283472332"))
print(atoi_2(" + 420"))
print(atoi_2("  -420"))
print(atoi_2(" w  -420"))
print(atoi_2("420"))
print()
print(atoi_3("91283472332"))
print(atoi_3("420"))