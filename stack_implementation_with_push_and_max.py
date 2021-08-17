"""
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
and
max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error 
or return null.
"""

def createStack():
    stack = []
    return stack

def push(stack, val):
    stack.append(val)
    return stack

def max(stack):
    if len(stack) == 0:
        return None
    maxim = stack[0]
    for item in stack:
        if maxim < item:
            maxim = item
    return maxim 
