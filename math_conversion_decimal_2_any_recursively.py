"""
Create a function to convert given number from one base to another
For example:
Input: 16
Output : 10 in hex base
"""

def conversion(num, base):
    conversion_string = "0123456789ABCDEF"
    if num < base:
        return conversion_string[num]
    else:
        print(num, base)
        return str(conversion(num // base, base)) + conversion_string[num % base]    

# driver code
num = 17
base = 16
print(conversion(num, base))


