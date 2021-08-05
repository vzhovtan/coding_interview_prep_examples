"""
Bubble sort
"""

class Solution:
    def __init__(self, arr):
        self.arr = arr

    def bubble(self):
        for i in range(len(self.arr)-1):
            for j in range(i+1, len(self.arr)):
                print(self.arr[i], self.arr[j])
                if self.arr[i] > self.arr[j]:
                    self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
                print(self.arr)    

        return self.arr
            
# driver code
s = Solution([5, 6, 7, 8, 9, 0, 1, 2, 3, 4])
print(s.bubble())