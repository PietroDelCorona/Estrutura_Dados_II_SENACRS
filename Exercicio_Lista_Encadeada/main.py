
from Lista import Lista
from Tarefa import Tarefa

lista = Lista()


def validar_indice_input(mensagem):
    while True:
        try:
            indice = int(input(mensagem))
            if indice < 0 or indice > lista.tamanho:
                print("Índice inválido. Tente novamente.")
                continue
            return indice
        except ValueError:
            print("Entrada inválida. Insira um número válido")



def listar_tarefas():
    print("---------------")
    lista.imprimir_reverso()
    print("---------------")
    
def inserir_tarefas():
    descricao = input("Coloque aqui sua tarefa: ")
    lista.adicionar_inicio(descricao)

def deletar_tarefas():
    print("""Você quer remover a tarefa do início ou do fim da lista?
          Se for no ínicio pressione a tecla i, se no final pressione a tecla f
          Se quiser retornar ao menu inicial, aperte qualquer tecla.""")
    tecla_deletar = input("Aperte a tecla que você desejar: ")
    if tecla_deletar == 'i':
        lista.remover_fim()
    elif tecla_deletar == 'f':
        lista.remover_inicio()
    else:
        menu()

def marcar_tarefa_concluida(lista):
    print("Tarefas pendentes:")
    print("------------------")
    aux = lista.inicio
    while aux:
        if not aux.concluida:
            print(f"{aux.identificacao} {'[X]' if aux.concluida else '[ ]'} {aux.descricao}")
        aux = aux.proximo
    print("-------------------")
    
    indice = validar_indice_input("Digite o índice da tarefa que deseja marcar como concluída: ")
    
    aux = lista.inicio
    while aux:
        if aux.identificacao == indice:
            if aux.concluida:
                print(f"Tarefa {aux.identificacao} já está marcada como concluída.")
            else:
                aux.concluida = True
                print(f"Tarefa {aux.identificacao} marcada como concluída.")
            break
        aux = aux.proximo
    

def remover_tarefa_indice():
    print("Tarefas atuais:")
    print("---------------")
    aux = lista.inicio
    while aux:
        print(f"{aux.identificacao}, {aux.descricao}")
        aux = aux.proximo
    print("----------------")  
    
    indice = validar_indice_input("Digite o índice da tarefa que deseja remover: ")
    
    aux = lista.inicio
    prev = None
    
    while aux:
        if aux.identificacao == indice:
            if prev:
                prev.proximo = aux.proximo
            else:
                lista.inicio = aux.proximo
            print(f"Tarefa: {aux.identificacao} removida")
            lista.tamanho -= 1
            listar_tarefas()
            break
        prev = aux
        aux = aux.proximo
    else:
        print("Tarefa não encontrada.")
    


def alterar_tarefa_indice():
    print("Tarefas atuais:")
    print("------------------")
    aux = lista.inicio
    while aux:
        print(f"{aux.identificacao}, {aux.descricao}")
        aux = aux.proximo
    print("----------------")
    
    indice = validar_indice_input("Digite o índice da tarefa que deseja alterar: ")
    
    aux = lista.inicio
    while aux:
        if aux.identificacao == indice:
            nova_descricao = input("Digite a nova descrição da tarefa: ")
            aux.descricao = nova_descricao
            print(f"Tarefa {aux.descricao} alterada para: {nova_descricao}")
            break
        aux = aux.proximo
    else:
        print("Tarefa não encontrada.")
            
        

def menu():
    while True:
        print("""
            Olá! Bem-vindo ao menu To-Do List. Essa é uma lista de tarefas.
            Você só poderá inserir ou remover tarefas no início ou no fim da lista.
            As opções são:
            1 - Ler as tarefas atuais
            2 - Inserir novas tarefas
            3 - Remover tarefas
            4 - Alterar tarefas pelo índice
            5 - Marcar tarefas como concluídas
            6 - Deletar tarefas através dos índices
            7 - Sair do menu
            """)
        
        try:
            escolha = int(input("Escolha uma das opções: "))
            if escolha == 1:
                listar_tarefas()
            elif escolha == 2:
                inserir_tarefas()
            elif escolha == 3:
                deletar_tarefas()
            elif escolha == 4:
                alterar_tarefa_indice()
            elif escolha == 5:
                marcar_tarefa_concluida(lista)
            elif escolha == 6:
                remover_tarefa_indice()
            elif escolha == 7:
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