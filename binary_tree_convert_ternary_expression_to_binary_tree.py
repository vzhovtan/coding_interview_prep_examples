"""
Create binary tree from ternary expression
"""
class Node: 
    def __init__(self, key): 
        self.data = key 
        self.left = None
        self.right = None
  
# Function to convert ternary expression to a Binary tree returning the root node of the tree 
def convert_expression(expression, i): 
    if i >= len(expression): 
        return None
  
    # Create a new node object for the expression at i'th index 
    root = Node(expression[i]) 
    i += 1
    # if current character of ternary expression is '?' then we add next character as a left child of current node 
    if (i < len(expression) and 
                expression[i] == "?"): 
        root.left = convert_expression(expression, i + 1) 
          
    # else we have to add it as a right child of current node expression[0] == ':' 
    elif i < len(expression): 
        root.right = convert_expression(expression, i + 1) 
    return root 
  
# pre-order traversal pattern 
def print_tree(root): 
    if not root: 
        return
    print(root.data, end=' ') 
    print_tree(root.left) 
    print_tree(root.right) 
  
# driver code
string_expression = "a?b?c:d:e"
root_node = convert_expression(string_expression, 0) 
print_tree(root_node) 
