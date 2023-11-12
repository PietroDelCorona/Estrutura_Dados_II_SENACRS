
from Node import Node

class BinaryTree():
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print()
        elif traversal_type == "inorder":
            return self.inorder_print()
        elif traversal_type == "postorder":
            return self.postorder_print()
        else:
            return "Tipo transversal não reconhecido."
        
    
    def preorder_print():
        pass
    
    def inorder_print():
        pass
    
    def postorder_print():
        pass