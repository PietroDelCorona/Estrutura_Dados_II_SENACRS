
from BinarySearchTree import BinarySearchTree

class FunctionsMain:
    
    def call_first_tree():
        print("Primeira Árvore:")
        
        first_tree = BinarySearchTree(1)
        first_tree.insert(2)
        first_tree.insert(3)
        first_tree.insert(4)
        first_tree.insert(5)
        first_tree.insert(6)
        first_tree.insert(7)
        first_tree.insert(8)
        first_tree.insert(9)
        
        #Demonstração AVL Tree - Professora
        '''
        first_tree = BinarySearchTree(4)
        first_tree.insert(2)
        first_tree.insert(6)
        first_tree.insert(1)
        first_tree.insert(3)
        first_tree.insert(5)
        first_tree.insert(8)
        first_tree.insert(7)
        first_tree.insert(9)
        '''
        print(first_tree) 
        
        height = first_tree.height_tree()
        if height == 0:
            print("Árvore está vazia.")
        else:
            print(f"A altura da árvore é: {height}")
        print(f"Quantidade de nós na árvore: {len(first_tree)}")
        print(f"Preorder: {first_tree.print_tree('preorder')}")
        print(f"Inorder: {first_tree.print_tree('inorder')}")
        print(f"Postorder: {first_tree.print_tree('postorder')}")
        
        
        while True:
                node_remove = input("Você deseja remover algum nó da árvore atual (s/n)? ")
                        
                if node_remove == 's':
                    if first_tree.root is None:
                        print("A árvore está vazia.")
                        break 
                    else:
                        removed_value = int(input("Digite aqui qual nó você quer remover: "))
                        first_tree.remove(removed_value)
                        print(f"Árvore depois da remoção do nó {removed_value}:\n")
                        print(first_tree)
                else:
                    break       
                   
        
    def call_second_tree():
        print("Segunda Árvore:")
        second_tree = BinarySearchTree(9)
        second_tree.insert(8)
        second_tree.insert(7)
        second_tree.insert(6)
        second_tree.insert(5)
        second_tree.insert(4)
        second_tree.insert(3)
        second_tree.insert(2)
        second_tree.insert(1)
        
        print(second_tree)
        
        height = second_tree.height_tree()
        if height == 0:
            print("Árvore está vazia.")
        else:
            print(f"A altura da árvore é: {height}")
        print(f"Quantidade de nós na árvore: {len(second_tree)}")
        print(f"Preorder: {second_tree.print_tree('preorder')}")
        print(f"Inorder: {second_tree.print_tree('inorder')}")
        print(f"Postorder: {second_tree.print_tree('postorder')}")
        
        while True:
            node_remove = input("Você deseja remover algum nó da árvore atual (s/n)? ")
                      
            if node_remove == 's':
                if second_tree.root is None:
                    print("A árvore está vazia.")
                    break 
                else:
                    removed_value = int(input("Digite aqui qual nó você quer remover: "))
                    second_tree.remove(removed_value)
                    print(f"Árvore depois da remoção do nó {removed_value}:\n")
                    print(second_tree)
            else:
                break   
            

    def call_third_tree():
        print("Terceira Árvore:")
        third_tree = BinarySearchTree(-1)
        
        print(third_tree)
        
        height = third_tree.height_tree()
        if height == 0:
            print("Árvore está vazia.")
        else:
            print(f"A altura da árvore é: {height}")
        print(f"Quantidade de nós na árvore: {len(third_tree)}")
        print(f"Preorder: {third_tree.print_tree('preorder')}")
        print(f"Inorder: {third_tree.print_tree('inorder')}")
        print(f"Postorder: {third_tree.print_tree('postorder')}")
        
        while True:
            node_remove = input("Você deseja remover algum nó da árvore atual (s/n)? ")
                      
            if node_remove == 's':
                if third_tree.root is None:
                    print("A árvore está vazia.")
                    break 
                else:
                    removed_value = int(input("Digite aqui qual nó você quer remover: "))
                    third_tree.remove(removed_value)
                    print(f"Árvore depois da remoção do nó {removed_value}:\n")
                    print(third_tree)
            else:
                break
    
          