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

lista = Lista()

def ListarTarefas():
    
    lista.imprimir()
    
def InserirTarefas():
    tarefa = input("Coloque aqui sua tarefa: ")
    lista.addInicio(tarefa)

def DeletarTarefas():
    pass

def AlterarTarefa():
    pass



def menu():
    while True:
        print("""
              Olá! Bem-vindo ao menu To-Do List. Essa é uma lista de tarefas.
              Você só poderá inserir ou remover tarefas no início ou no fim da lista.
              As opções são:
              1 - Ler as tarefas atuais
              2 - Inserir novas tarefas
              3 - Remover tarefas
              4 - Alterar tarefas
              """)
        try:
            escolha = int(input("Escolha uma das opções: "))
            if escolha == 1:
                ListarTarefas()
            elif escolha == 2:
                InserirTarefas()
            elif escolha == 3:
                DeletarTarefas()
            elif escolha == 4:
                AlterarTarefa()
            else:
                print("Opção inválida. Por favor, escolha uma das opções válidas.")
                return menu()
        except ValueError:
            print("Entrada inválida. Por favor, insira um número correspondente ao menu.")
            continue
                   

menu()