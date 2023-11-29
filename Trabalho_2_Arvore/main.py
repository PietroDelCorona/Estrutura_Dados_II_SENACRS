
from BinarySearchTree import BinarySearchTree

print("Exercício da Construção das Árvores Binárias de pesquisa:\n")

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
    
    height = second_tree.height_tree()
    if height == 0:
        print("Árvore está vazia.")
    else:
        print(f"A altura da árvore é: {height}")
    print(f"Quantidade de nós na árvore: {len(second_tree)}")
    print(f"Preorder: {second_tree.print_tree('preorder')}")
    print(f"Inorder: {second_tree.print_tree('inorder')}")
    print(f"Postorder: {second_tree.print_tree('postorder')}")


def call_third_tree():
    print("Terceira Árvore:")
    third_tree = BinarySearchTree("")
    
    height = third_tree.height_tree()
    if height == 0:
        print("Árvore está vazia.")
    else:
        print(f"A altura da árvore é: {height}")
    print(f"Quantidade de nós na árvore: {len(third_tree)}")
    print(f"Preorder: {third_tree.print_tree('preorder')}")
    print(f"Inorder: {third_tree.print_tree('inorder')}")
    print(f"Postorder: {third_tree.print_tree('postorder')}")
    

def menu():
    while True:
        print("""
              Olá! Esse é o menu de visualização das árvores de pesquisa binária.
              As opções são:
              1 - Primeira Árvore
              2 - Segunda Árvore
              3 - Terceira Árvore
              4 - Sair do Menu
            """)
        
        try:
            choice = int(input("Digite uma das opções acima: "))
            if choice == 1:
                call_first_tree()
            elif choice == 2:
                call_second_tree()
            elif choice == 3:
                call_third_tree()
            elif choice == 4:
                print(f"""\nVocê tem certeza que quer sair desse menu?
                Se sim, pressione y.""")
                resposta_saida = input(f"\nAperte a tecla: ")
                if resposta_saida == 'y':
                    print(f"\nObrigado por utilizar esse menu!")
                    break
                else:
                    continue   
            else:
                print("Opção inválida. Por favor, insira um número correspondente ao menu.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número correspondente ao menu.")
            continue
    

menu()
    

