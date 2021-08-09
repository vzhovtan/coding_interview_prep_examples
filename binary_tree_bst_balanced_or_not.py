"""
Height-balanced binary tree  is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1
Find if given binary tree balanced or not
"""

class Node:  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        
def is_balanced_binary_tree(tree):
    left = dfs(tree.left, 1)
    right = dfs(tree.right, 1)
    print("FINAL === Left: " + str(left) + " and Right: " + str(right))
    if abs(left-right) <= 1:
        return True
    else:
        return False

def dfs(root, depth):
    if root == None:
        return depth
    else:
        left = dfs(root.left, depth + 1)
        right = dfs(root.right, depth + 1)
        print("Left: " + str(left) + " and Right: " + str(right))
        if abs(left-right) <= 1:
            return depth
        else:
            return False

# drive code
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (is_balanced_binary_tree(root)): 
    print("balanced")
else: 
    print("not balanced")