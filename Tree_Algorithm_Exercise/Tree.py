from Node import Node

class Tree():
    def __init__(self, root_data):
        self.root = Node(root_data)
    
    def __len__(self):
        return self.size()
    
    def size(self):
        return self.size_helper(self.root)
    
    def size_helper(self, node):
        if node is None:
            return 0
        count = 1
        for child in node.children:
            count += self.size_helper(child)
        return count
    
    def is_empty(self):
        return self.root is None
    
    def iterator(self):
        return self.iterator_helper(self.root)
    
    def iterator_helper(self, node):
        if node is not None:
            yield node.data
            for child in node.children:
                yield from self.iterator_helper(child)
                
    def positions(self):
        return self.iterator_helper(self.root)
    
    def replace_element(self, v, e):
        node_to_replace = self.get_root().search_node(v)
        if node_to_replace:
            old_data = node_to_replace.data
            node_to_replace.data = e
            return old_data, e
        else:
            return None
    
    def get_root(self):
        return self.root
    
    def __str__(self):
        return self.str_helper(self.root, 0)
    
    def str_helper(self, node, depth):
        result = "  " * depth + str(node.data) + "\n"
        for child in node.children:
            result += self.str_helper(child, depth + 1)
        return result
        
    def find_parent(self, node, n):
        if node == n:
            return None
        for child in node.children:
            if n in child.children:
                return child
            else:
                result = self.find_parent(child, n)
                if result:
                    return result
    
    def children(self, n):
        for node in self.root.children:
            if n == node:
                return node.children
        return None
    
    def is_internal(self, n):
        return bool(n.children)
    
    def is_external(self, n):
        return not bool(n.children)
    
    def is_root(self, n):
        return n == self.root
