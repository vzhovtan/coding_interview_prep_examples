"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
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

def parChecker(arr):
    s = Stack()
    balanced = True
    for symbol in arr:
            if symbol == "(":
                s.push(symbol)
            elif not s.isEmpty():
                s.pop()
            elif s.isEmpty():
                balanced = False

    if balanced and s.isEmpty():
        return True
    else:
        return False

# driver code
print(parChecker('((()))'))
print(parChecker('(()())'))
