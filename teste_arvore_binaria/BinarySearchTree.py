from Node import Node

class BinarySearchTree():
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def get_root(self):
        return self.root
    
    def set_root(self, root_data):
        self.root = Node(root_data)
    
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
    """
    def replace_element(self, v, e):
        node_to_replace, _ = self.search_node(v)
        if node_to_replace:
            old_data = node_to_replace.data
            node_to_replace.data = e
            return old_data, e
        else:
            return None
    """
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
    
    def add_left_child(self, parent_node_data, new_node_data):
        parent_node, parent, found = self.search_node(parent_node_data)
        if not found:
            print(f'Nodo {parent_node_data} não encontrado para adicionar um filho à esquerda.')
            return False
        
        if parent_node.left is None:
            parent_node.left = Node(new_node_data)
            return True
        else:
            print(f'Já existe um nodo à esquerda do valor {parent_node_data}.')
            return False
    
    def add_right_child(self, parent_node_data, new_node_data):
        parent_node, parent, found = self.search_node(parent_node_data)
        if not found:
            print(f'Nodo {parent_node_data} não encontrado para adicionar um filho à direita.')
            return False
        
        if parent_node.right is None:
            parent_node.right = Node(new_node_data)
            return True
        else:
            print(f'Já existe um nodo à direita do valor {parent_node_data}.')
            return False
        
    def add_left_child(self, parent_node_data, new_node_data):
        parent_node, parent, found = self.search_node(parent_node_data)
        if not found:
            print(f'Nodo {parent_node_data} não encontrado para adicionar um filho à esquerda.')
            return False
        
        if parent_node.left is None:
            parent_node.left = Node(new_node_data)
            return True
        else:
            print(f'Já existe um nodo à esquerda do valor {parent_node_data}.')
            return False
            
    def remove_right_child(self, parent_value):
            parent_node = self.search_node(parent_value)
            if parent_node:
                if parent_node.right:
                    parent_node.right = None
                    return True
                else:
                    print("Não há filho à direita para remover.")
                    return False
            else:
                print(f'Nodo {parent_value} não encontrado.')
                return False
    
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
    
    def find_parent(self, start, node_to_find):
        if start is None or start == node_to_find:
            return None

        if (start.left == node_to_find) or (start.right == node_to_find):
            return start

        left_parent = self.find_parent(start.left, node_to_find)
        if left_parent:
            return left_parent

        right_parent = self.find_parent(start.right, node_to_find)
        if right_parent:
            return right_parent

        return None
    
    def is_internal(self, node):
        return node.left is not None or node.right is not None

    def is_external(self, node):
        return node.left is None and node.right is None

    def is_root(self, node):
        return node == self.root

    def search_node(self, value, start=None):
        if start is None:
            start = self.root

        parent = None
        current = start

        while current:
            if int(value) == current.data:
                return current, parent, True
            
            parent = current

            if int(value) < current.data:
                current = current.left
            else:
                current = current.right

        return None, parent, False

    def remove_node_message(self, value):
        node_to_remove = self.search_node(value)

        if node_to_remove is None:
            print(f"Nodo '{value}' não encontrado para remoção.")
            return

        parent_node = self.find_parent(self.get_root(), node_to_remove)

        if self.is_root(node_to_remove):
            removed_node = self.get_root().data
            self.root = None
            print(f"Removendo nodo '{removed_node}' que era a raiz.")
            return

        if self.is_internal(node_to_remove):
            node_type = "interno"
        elif self.is_external(node_to_remove):
            node_type = "externo"

        removed_node = node_to_remove.data

        if parent_node.left == node_to_remove:
            parent_node.left = None  
        else:
            parent_node.right = None  

        print(f"Removendo nodo '{removed_node}' que era {node_type}.")
        