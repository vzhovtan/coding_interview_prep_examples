"""
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.
Example:
Input: Root of below tree
       1
      / \
     2   3
Output: 1+2+3 = 6
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def findMaxUtil(root): 
    if root is None: 
        return 0 

    l = findMaxUtil(root.left) 
    r = findMaxUtil(root.right) 
    max_single = max(max(l, r) + root.data, root.data)  
  
    return max_single 
  
# driver code
root = Node(10) 
root.left = Node(2) 
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print (f"Max path sum is {findMaxUtil(root)}")