"""
Find Kth largest node in BST
"""

class Node:  
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def find_k_largest_in_bst(root, k):
    node_list = []
    def pre_order(root):
        if root == None:
            return
        else:
            node_list.append(root.data)
            pre_order(root.left)
            pre_order(root.right)
    pre_order(root)
    sorted_data = sorted(node_list)
    return sorted_data[(len(sorted_data)-k):]

# driver code
root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
print(find_k_largest_in_bst(root, 2))    