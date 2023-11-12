
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def add_left_child(self, child_node):
        self.left = child_node
    
    def add_right_child(self, child_node):
        self.right = child_node
    
    def remove_left_child(self):
        if self.left:
            self.left = None
        else:
            print("Não há filho à esquerda para remover.")
            
    def remove_right_child(self):
        if self.right:
            self.right = None
        else:
            print("Não há filho à direita para remover.")