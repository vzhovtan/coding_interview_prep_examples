"""
Create a function to evaluate math epression given as fully parenthesized expressions
Using two stacks and classic Dijkstra algo
Upon encountering a “(“ : Ignore
Upon encountering an operand (Number value) : Push onto the values stack.
Upon encountering an operator (symbol) : Push onto the operator stack.
Upon encountering a “)“ : Pop requisite operands , Pop Operator , Push operation result onto values stack.
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

values = Stack()
operators = Stack()

expression = "(2+3)-(2-1)+(2+2)"
for item in expression:
    if item.isdigit():
        values.push(item)
    elif item == "(":
        continue
    elif item == "+" or item == "-":
        operators.push(item)
    elif item == ")":
        while operators.size() and values.size():
            curr_value = int(values.pop())
            curr_oper = operators.pop()
            if curr_oper == "+":
                curr_value = curr_value + int(values.pop())
            else:
                 curr_value = int(values.pop()) - curr_value
            values.push(curr_value)

# driver code
print(values.pop())

