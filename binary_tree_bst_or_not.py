"""
Find if given binary tree balanced or not
A binary search tree (BST) is a node based binary tree data structure which has the following properties. 
- The left subtree of a node contains only nodes with keys less than the node’s key. 
- The right subtree of a node contains only nodes with keys greater than the node’s key. 
 -Both the left and right subtrees must also be binary search trees.
"""

INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# Returns true if the given tree is a binary search tree 
def isBST(node): 
    return (isBSThelper(node, INT_MIN, INT_MAX)) 
  
# Retusn true if the given tree is a BST and its values >= min and <= max 
def isBSThelper(node, mini, maxi): 
    # An empty tree is BST 
    if node is None: 
        return True
  
    # False if this node violates min/max constraint 
    if node.data < mini or node.data > maxi: 
        return False
  
    # Otherwise check the subtrees recursively tightening the min or max constraint 
    return (isBSThelper(node.left, mini, node.data -1) and
          isBSThelper(node.right, node.data+1, maxi)) 
  
# driver code
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print("BST")
else: 
    print("Not a BST")