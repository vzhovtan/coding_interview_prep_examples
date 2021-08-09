"""
Given a sorted array. Write a function that creates a Balanced Binary Search Tree using array elements.
Input:  Array {1, 2, 3}
Output: A Balanced BST
     2
   /  \
  1    3 
Input: Array {1, 2, 3, 4}
Output: A Balanced BST
      3
    /  \
   2    4
 /
1
Algo:
1) Get the Middle of the array and make it root.
2) Recursively do same for left half and right half.
      a) Get the middle of left half and make it left child of the root
          created in step 1.
      b) Get the middle of right half and make it right child of the
          root created in step 1.
"""

class BSTNode: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None

def sorted_to_bst(arr):
    if not arr:
        return None

    mid = len(arr)//2
    root = BSTNode(arr[mid])
    root.left = sorted_to_bst(arr[:mid])
    root.right = sorted_to_bst(arr[mid+1:])
    return root

def preOrder(node): 
    if not node: 
        return
    print(node.data) 
    preOrder(node.left)
    preOrder(node.right)  

# driver code
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sorted_to_bst(arr) 
print("PreOrder Traversal of constructed BST ") 
preOrder(root)