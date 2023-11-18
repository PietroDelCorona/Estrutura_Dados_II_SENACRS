
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

while True:
    node_name_to_find = input("Qual nodo você quer buscar? ")

    node_to_find = t.search_node(node_name_to_find)

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

node_to_replace = t.search_node(old_data, t.get_root())

if node_to_replace is not None:
    parent_node = t.find_parent(t.get_root(), node_to_replace)

    new_data = input("Digite o novo valor do nodo: ")

    result = t.replace_element(old_data, new_data)
    if result is not None:
        old_value, new_value = result
        print(f"Substituindo o antigo valor pelo novo.\n Antigo valor: {old_value}.\n Novo valor: {new_value}")
        print("Nova Árvore:")
        print(t)
    else:
        print(f"Nodo '{old_data}' não encontrado para substituição.")

else:
    print(f"Nodo '{old_data}' não encontrado. Tente novamente.")
    

remove_value = input("Qual nodo você quer remover? ")
t.remove_node_with_message(remove_value)  # Aqui 't' representa a sua árvore
print("Nova Árvore:")
print(t)