"""
Validate if a given string is numeric. Some examples:
"0" - true 
"0.1" - true 
"abc" - false
"""

def valid1(number):
    if len(number) == 1 and number.isdigit():
        return True
    else:
        if number[-1].isdigit() or number[-1] == ".":
            return valid1(number[:-1])

    return False        

def valid2(number):
    valid = True
    # no needs to check all chars, if even one is not a  digit return False
    for char in number:
        if char != "." and not char.isdigit():
            valid = False
    return valid        

# driver code
number1 = "a234"
number2 = "1.234"
print(valid1(number1)) # False
print(valid2(number1)) # False
print(valid1(number2)) # True
print(valid2(number2)) # True