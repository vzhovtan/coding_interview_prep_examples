"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
"""

class MinStack1:
    def __init__(self):
        self.min = None
        self.stack = []
        
    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x

    def pop(self):
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x

    def top(self):
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        
    def getMin(self):
        return self.min


class MinStack2:
    def __init__(self):
        self.stack, self.minStack = [], []

    def push(self, x):
        self.stack.append(x)
        if len(self.minStack):
            if x < self.minStack[-1][0]:
                self.minStack.append([x, 1])
            elif x == self.minStack[-1][0]:
                self.minStack[-1][1] += 1
        else:
            self.minStack.append([x, 1])

    def pop(self):
        x = self.stack.pop()
        if x == self.minStack[-1][0]:
            self.minStack[-1][1] -= 1
            if self.minStack[-1][1] == 0:
                self.minStack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.minStack[-1][0]

# driver code
stack = MinStack1()
stack.push(-1)
print([stack.top(), stack.getMin()])
    
stack = MinStack2()
stack.push(-2)
print([stack.top(), stack.getMin()])