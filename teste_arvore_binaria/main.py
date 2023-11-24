
from BinarySearchTree import BinarySearchTree


root_value = int(input("Digite o valor da raiz da arvore: "))

t = BinarySearchTree(root_value)
t.set_root(root_value)

print("Árvore inicial:")
print(t)

while True:
    add_node = input("Você deseja adicionar um novo nodo? (s/n): ")
    
    if add_node.lower() == 's':
        new_value = int(input("Digite o valor do novo nodo: "))
        
        if new_value < t.root.data:
            success = t.add_left_child(t.root.data, new_value)
        elif new_value > t.root.data:
            success = t.add_right_child(t.root.data, new_value)
        else:
            print("O novo valor é igual ao valor da raiz. Não pode ser adicionado.")
        
        if not success:
            print("Falha ao adicionar o novo nodo.")
    else:
        break    

print("Árvore final:")
print(t)

print(f"Preorder: {t.print_tree('preorder')}")
print(f"Inorder: {t.print_tree('inorder')}")
print(f"Postorder: {t.print_tree('postorder')}")

while True:
    node_name_to_find = input("Qual nodo você quer buscar? ")

    node_to_find, _, message = t.search_node(node_name_to_find)

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
    
"""

old_data = int(input("Digite o nodo que você quer substituir: "))

node_to_replace = t.search_node(old_data)

if node_to_replace is not None:
    parent_node = t.find_parent(t.set_root(root_value), node_to_replace)

    new_data = int(input("Digite o novo valor do nodo: "))

    result = t.replace_element(node_to_replace, new_data)
    if result is not None:
        old_value, new_value = result
        print(f"Substituindo o antigo valor pelo novo.\n Antigo valor: {old_value}.\n Novo valor: {new_value}")
        print("Nova Árvore:")
        print(t)
    else:
        print(f"Nodo '{old_data}' não encontrado para substituição.")

else:
    print(f"Nodo '{old_data}' não encontrado. Tente novamente.")
    
"""
remove = input("Você quer remover algum nodo? ")

if remove == "y":
    remove_value = input("Qual nodo você quer remover? ")
    t.remove_node_message(remove_value)  
    print("Nova Árvore:")
    print(t)
else:
    print("Árvore existente:")
    print(t)
    
    