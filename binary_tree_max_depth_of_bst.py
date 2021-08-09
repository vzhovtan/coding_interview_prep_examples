"""
Given a binary tree, find its maximum depth. 
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def maxDepth(node): 
    if node is None: 
        return 0
    else : 
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
  
# driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print (f"Height of tree is {(maxDepth(root))}") 