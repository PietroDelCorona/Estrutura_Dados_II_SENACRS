
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def get_key(self):
        return self.key
    
    def set_key(self, key):
        self.key = key
    
    def get_left(self):
        return self.left
    
    def set_left(self, left):
        self.left = left
    
    def get_right(self):
        return self.right
    
    def set_right(self, right):
        self.right = right
    