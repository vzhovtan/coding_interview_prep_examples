"""
Create a function from decimal integer to binary using stack
"""

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []    

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)  


# driver code
def dec2bin(value):
    if value == 0:
        return 0
    
    res = ""
    s = Stack()
    print("starting value", value)
    while value != 0:
        rem = value % 2
        print(rem)
        s.push(rem)
        value = value // 2
        print("curr value", value) 

    while not s.isEmpty():
        res += str(s.pop())

    return res

print(dec2bin(10))        





