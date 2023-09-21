'''
To Do List : 
Desenvolva uma To Do List (Lista de Tarefas) em Python utilizando, obrigatoriamente, listas encadeadas (livre escolha de qual delas será a mais adequada). 
Como será essa aplicação? 
- Deve contemplar todas principais atividades de um CRUD simples, isto é: Inserir, Deleter, Remover e Alterar - uma tarefa ou várias. 
- Implementar um pequeno menu dando a opção de escolha ao usuário e, consequentemente, viabilizando maior interação com a aplicação. 
- Além das operações básicas também podem implementar outras funcionalidades, como por exemplo, marcar uma tarefa como feita e manter ela destacada na listagem (ou não). 
Dicas: 
- Procure modularizar a sua aplicação o máximo que conseguir, mantendo coesão e coerência do início ao fim. Não esquecendo dos quatro pilares da Programação Orientada a Objetos
- Use a criatividade, destaquei pontos essenciais apenas. 
'''
from Lista import Lista
from Tarefa import Tarefa

lista = Lista()


def validar_indice_input(mensagem):
    while True:
        try:
            indice = int(input(mensagem))
            if indice < 0 or indice >= lista.tamanho():
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
            print(f"[{aux.identificacao}] {'[X]' if aux.concluida else '[ ]'} {aux.descricao}")
        aux.proximo
    print("-------------------")
    
    indice = validar_indice_input("Digite o índice que da tarefa que deseja marcar como concluída: ")
    
    aux = lista.inicio
    while aux:
        if aux.identificacao == indice:
            aux.concluida = True
            print(f"Tarefa {aux.identificacao} marcada como concluída.")
            break
        aux = aux.proximo
    else:
        print("Tarefa não encontrada.")

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
            break
        prev = aux
        aux = aux.proximo
    else:
        print("Tarefa não encontrada.")


def inserir_tarefa_indice():
    print("Tarefas atuais:")
    print("---------------")
    aux = lista.inicio
    while aux:
        print(f"{aux.identificacao}, {aux.descricao}")
        aux = aux.proximo
    print("----------------")
    
    indice = validar_indice_input("Digite o índice onde deseja inserir a nova tarefa: ")
    
    nova_descricao = input("Digite a nova descrição da nova tarefa: ")
    
    nova_tarefa = Tarefa(nova_descricao)
    
    aux = lista.inicio
    prev = None
    
    for _ in range(indice):
        prev = aux
        aux = aux.proximo
    
    if prev:
        prev.proximo = nova_tarefa
    else:
        lista.inicio = nova_tarefa
    
    nova_tarefa.proximo = aux    
    print(f"Tarefa inserida com sucesso no índice {indice}.")


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
            6 - Inserir tarefas através dos índices
            7 - Deletar tarefas através dos índices
            8 - Sair do menu
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
                inserir_tarefa_indice()
            elif escolha == 7:
                remover_tarefa_indice()
            elif escolha == 8:
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