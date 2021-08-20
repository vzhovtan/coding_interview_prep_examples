"""
Create a function which reverse given string
"""

class Stack:
    # only push(), pop() and isEmpty() methods are needed
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []    

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

# driver code
s = Stack()
string = "Take a string and return reversed chars in string"
result = ""

for letter in string:
    s.push(letter)

while not s.isEmpty():
    result += s.pop()

print(result)