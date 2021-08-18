"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
find_max() -- Retrieve the maximum element in the stack.
"""

import collections
import heapq

class Stack:
    def __init__(self):
        self.storage = []
        self.my_max = float('-inf')
        self.heapmap = dict()
        self.id_count = 100000000

    def empty(self):
        if len(self.storage) == 0:
            return True
        else:
            return False

    def max(self):
        if self.empty != True:
            return self.my_max
        else:
            return Exception('Empty Stack has no max!')

    def pop(self):
        key = heapq.heappop(self.storage)
        val = self.heapmap[key]
        self.heapmap.pop(key, val)
        if val == self.my_max:
            self.my_max = self.find_map_max()
        return val

    def find_map_max(self):
        best_max = float('-inf')
        for key in self.heapmap:
            if self.heapmap[key] > best_max:
                best_max = self.heapmap[key]
        return best_max

    def push(self, x):
        if x > self.my_max:
            self.my_max = x
        key = self.id_count
        self.heapmap[key] = x
        heapq.heappush(self.storage, key)
        #print(self.heapmap)
        self.id_count -= 1

# driver code
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(my_stack.find_map_max())