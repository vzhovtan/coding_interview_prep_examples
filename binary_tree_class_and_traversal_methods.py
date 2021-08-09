"""
Create binary tree class and implement preorder, inorder and postorder methods
"""

class BinaryTree():
    def __init__(self, root):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, new_node):
        if not self.left:
            self.left = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left = self.left
            self.left = new_child

    def insert_right(self, new_node):
        if not self.right:
            self.right = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right = self.right
            self.right = new_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_obj):
        self.key = new_obj

    root = property(get_root_val, set_root_val)

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def preorder(self):
        print(self.key)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key)    
        if self.right:
            self.right.inorder()

# driver code
tree = BinaryTree(5)
tree.insert_left(3)
tree.insert_right(6)
print("root", tree.root)
print("left", tree.get_left().root)
print("right", tree.get_right().root)
print("preorder")
tree.preorder()
print("inorder")
tree.inorder()

            


