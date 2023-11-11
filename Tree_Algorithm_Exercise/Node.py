
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)
    
    def remove_child(self, child_node):
        self.children.remove(child_node)
    