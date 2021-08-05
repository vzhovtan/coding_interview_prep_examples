"""
Linear search
"""

def linear(array, item):
    for index, value in enumerate(array):
        if value == item:
            return index

    return False        

# driver code
print(linear([1, -5, 7, 10, 2, 30, 22, 18, 27, 3, 40], 40))