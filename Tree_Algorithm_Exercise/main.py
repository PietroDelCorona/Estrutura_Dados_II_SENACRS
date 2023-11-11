from Node import Node
from Tree import Tree

def search_node(node, name_to_find):
    if node.data == name_to_find:
        return node
    
    for child in node.children:
        found_node = search_node(child, name_to_find)
        if found_node:
            return found_node

    return None

t = Tree("A")

b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

b.add_child(c)
b.add_child(d)
c.add_child(e)
c.add_child(f)
e.add_child(g)

t.get_root().add_child(b)

print("Árvore:")
print(t)

while True:
    node_name_to_find = input("Qual nodo você quer buscar? ")

    node_to_find = search_node(t.get_root(), node_name_to_find)

    if node_to_find is not None:
        break
    else:
        print(f"Nodo '{node_name_to_find}' não encontrado. Tente novamente.")

if node_to_find is not None:
    parent_node = t.find_parent(t.get_root(), node_to_find)
    
    print(f"\n'{node_to_find.data}':")
    print(f"É interno? {t.is_internal(node_to_find)}")
    print(f"É externo? {t.is_external(node_to_find)}")
    print(f"É raiz? {t.is_root(node_to_find)}")