"""
Create function to reverse given integer without extra space
Pay attention that reveresed integer may result in overflow
"""

def reverse(digit):
    result = 0
    while digit:
        result = result * 10 + digit % 10
        print("curr result", result)
        digit = digit//10
        print("curr digit", digit)

    return result

# driver code
print(reverse(102))