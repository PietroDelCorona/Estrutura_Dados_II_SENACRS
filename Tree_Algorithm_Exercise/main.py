from Node import Node
from Tree import Tree


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

def search_node(node, name_to_find):
    if node.data == name_to_find:
        return node
    
    for child in node.children:
        found_node = search_node(child, name_to_find)
        if found_node:
            return found_node

    return None

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


print(f"Tamanho da árvore: {len(t)}")
print(f"A árvore está vazia? {t.is_empty()}")

print(f"Elementos na árvore:")
for element in t.iterator():
    print(element)

print("Nodos na Árvore:")
for position in t.positions():
    print(position)

old_data = input("Digite o nodo que você quer substituir: ")

new_data = input("Digite o novo valor do nodo: ")

t.replace_element(old_data, new_data)
print(f"Substituindo o antigo valor pelo novo.\n Antigo valor: {old_data}.\n Novo valor: {new_data}")
print("Árvore após a substituição:")
print(t)

print("Testando conexão git")