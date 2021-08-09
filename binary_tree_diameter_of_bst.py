"""
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes
The diameter of a tree T is the largest of the following quantities:
-the diameter of T’s left subtree.
-the diameter of T’s right subtree.
-the longest path between leaves that goes through the root of T (this can be computed from the heights of the subtrees of T) 
"""

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

# The function Compute the "height" of a tree. Height is the  number f nodes along the longest path from the root node down to the farthest leaf node. 
  
def height(node): 
    # Base Case : Tree is empty 
    if node is None: 
        return 0
  
    # If tree is not empty then height = 1 + max of left height and right heights 
    return 1 + max(height(node.left), height(node.right)) 
  
# Get the diamtere of a binary tree 
def diameter(root): 
    # Base Case when tree is empty 
    if root is None: 
        return 0
  
    # Get the height of left and right sub-trees 
    lheight = height(root.left) 
    rheight = height(root.right) 
  
    # Get the diameter of left and right sub-trees 
    ldiameter = diameter(root.left) 
    rdiameter = diameter(root.right) 
  
    # Return max of the following tree: 
    # 1) Diameter of left subtree 
    # 2) Diameter of right subtree 
    # 3) Height of left subtree + height of right subtree +1 
    return max(lheight + rheight + 1, max(ldiameter, rdiameter)) 
  
  
# driver code
""" 
Constructed binary tree is  
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print(diameter(root))