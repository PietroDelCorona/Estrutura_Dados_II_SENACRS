
from Node import Node

class BinarySearchTree:
    def __init__(self, root_data = None):
        if root_data is not None and root_data != -1:
            self.root = Node(root_data)
        else:
            self.root = None
       
    def is_empty(self):
        if self.root is None:
            return True
        return False
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return self.size_helper(self.root) 
    
    def size_helper(self, node):
        if node is None:
            return 0
        
        return 1 + self.size_helper(node.left) + self.size_helper(node.right)
    
    def __str__(self):
        return self.str_helper(self.root)

    def str_helper(self, node):
        result = ""
        if node:
            result += str(node.key)
            if node.left or node.right:
                result += " -> "
                if node.left:
                    result += str(node.left.key)
                if node.right:
                    if node.left:
                        result += ", "
                    result += str(node.right.key)
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
            return "Tipo de travessia não reconhecido."

    def preorder_print(self, start=None, traversal=""):
        if self.root is None:
            return "Árvore está vazia"
        elif start is not None:
            traversal += (str(start.key) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start=None, traversal=""):
        if self.root is None:
            return "Árvore está vazia"
        elif start is not None:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.key) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start=None, traversal=""):
        if self.root is None:
            return "Árvore está vazia"
        elif start is not None:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.key) + " ")
        return traversal
        
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)
            
    def _insert_rec(self, node, key):
        if node is None:
            return Node(key)
        
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)
    
    def get_father(self, key):
        if self.root is None or self.root.key == key:
            return None
        return self.get_father_helper(self.root, key)
    
    def get_father_helper(self, key, node):
        if node is None:
            return None
        
        if (node.left and node.left.key == key) or (node.right and node.right.key == key):
            return node
        
        if key < node.key:
            return self.get_father_helper(node.left, key)
        else:
            return self.get_father_helper(node.right, key)
    
    def height_tree(self):
        if self.root is None:
            return 0
        else:
            return self.height_tree_helper(self.root)
    
    def height_tree_helper(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height_tree_helper(node.left)
            right_height = self.height_tree_helper(node.right)
            
            return max(left_height, right_height) +1
        
    def remove(self, key):
        self.root = self.remove_node_rec(self.root, key)
    
    def remove_node_rec(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self.remove_node_rec(node.left, key)
        elif key > node.key:
            node.right = self.remove_node_rec(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.min_value_node(node.right)
            
            node.key = temp.key
            
            node.right = self.remove_node_rec(node.right, temp.key)
            
        return node          
            
    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current