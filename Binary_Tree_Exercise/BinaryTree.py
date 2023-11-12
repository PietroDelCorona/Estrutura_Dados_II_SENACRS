
from Node import Node

class BinaryTree():
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def get_root(self):
        return self.root

    def __str__(self):
        return self.str_helper(self.root)
    
    def str_helper(self, node):
        result = ""
        if node:
            result += str(node.data)
            if node.left or node.right:
                result += " -> "
                if node.left:
                    result += str(node.left.data)
                if node.right:
                    if node.left:
                        result += ", "
                    result += str(node.right.data)
            result += "\n"
            result += self.str_helper(node.left)
            result += self.str_helper(node.right)
        return result
    
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root)
        elif traversal_type == "inorder":
            return self.inorder_print(self.root)
        elif traversal_type == "postorder":
            return self.postorder_print(self.root)
        else:
            return "Tipo transversal não reconhecido."

    def preorder_print(self, start, traversal=""):
        if start:
            traversal += (str(start.data) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal=""):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal=""):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + " ")
        return traversal
    
            
        