
from Node import Node
from BinaryTree import BinaryTree

t = BinaryTree("A")

b = Node.add_left_child("B")
c = Node.add_right_child("C")
d = Node.add_left_child("D")
e = Node.add_right_child("E")
f = Node.add_left_child("F")
g = Node.add_left_child("G")
h = Node.add_right_child("H")

print("Árvore:")
print(t)