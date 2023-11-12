
from Node import Node
from BinaryTree import BinaryTree

t = BinaryTree("A")

b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")
h = Node("H")

t.root.add_left_child(b)
t.root.add_right_child(c)

b.add_left_child(d)
b.add_right_child(e)
c.add_left_child(f)
c.add_right_child(g)
e.add_right_child(h)

print("Árvore:")
print(t)

print(f"Preorder: {t.print_tree('preorder')}")
print(f"Inorder: {t.print_tree('inorder')}")
print(f"Postorder: {t.print_tree('postorder')}")