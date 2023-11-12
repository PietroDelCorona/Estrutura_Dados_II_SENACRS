
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children.remove(child_node)
    
    def search_node(self, name_to_find):
        if self.data == name_to_find:
            return self

        for child in self.children:
            found_node = child.search_node(name_to_find)
            if found_node:
                return found_node

        return None

    