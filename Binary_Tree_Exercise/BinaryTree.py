
from Node import Node

class BinaryTree():
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def get_root(self):
        return self.root
    
    def __len__(self):
        return self.size()

    def size(self):
        return self.size_helper(self.root)

    def size_helper(self, node):
        if node is None:
            return 0
        left_size = self.size_helper(node.left)
        right_size = self.size_helper(node.right)
        return 1 + left_size + right_size
    
    def is_empty(self):
        return self.root is None
    
    def iterator(self):
        return self.iterator_helper(self.root)

    def iterator_helper(self, node):
        if node is not None:
            yield node.data
            yield from self.iterator_helper(node.left)
            yield from self.iterator_helper(node.right)
    
    def positions(self):
        return self.iterator_helper(self.root)
    
    def replace_element(self, v, e):
        node_to_replace = self.search_node(v, self.root)
        if node_to_replace:
            old_data = node_to_replace.data
            node_to_replace.data = e
            return old_data, e
        else:
            return None

    def __str__(self):
        return self.str_helper(self.root,)
    
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
    
    def find_parent(self, start, node_to_find, parent=None):
        if start is None:
            return None

        if start.data == node_to_find.data:
            return parent

        left_parent = self.find_parent(start.left, node_to_find, start)
        right_parent = self.find_parent(start.right, node_to_find, start)

        return left_parent or right_parent
    
    def is_internal(self, node):
        return node.left is not None or node.right is not None

    def is_external(self, node):
        return node.left is None and node.right is None

    def is_root(self, node):
        return node == self.root
    
    def search_node(self, name_to_find):
        return self._search_node(name_to_find, self.root)

    def search_node(self, value, start=None):
        if start is None:
            start = self.root

        stack = [start]
        while stack:
            current = stack.pop()
            if current.data == value:
                return current
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return None
    
   
    
    
    
            
        