
from FunctionsMain import FunctionsMain

print("Trabalho da Construção das Árvores Binárias de Pesquisa:\n")

    
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
                FunctionsMain.call_first_tree()
            elif choice == 2:
                FunctionsMain.call_second_tree()
            elif choice == 3:
                FunctionsMain.call_third_tree()
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
    

