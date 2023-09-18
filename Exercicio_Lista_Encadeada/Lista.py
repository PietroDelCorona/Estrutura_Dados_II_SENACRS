
from Tarefa import Tarefa

class Lista():
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def adicionar_inicio(self, tarefa):
        # Adiciona uma tarefa ao início da lista.
        item = Tarefa(tarefa)
        if self.inicio == None:
            self.inicio = item
            self.fim = item
        else:
            item.proximo = self.inicio
            self.inicio.anterior = item
            self.inicio = item
        self.tamanho += 1
        
    
    def adicionar_fim(self, tarefa):
        # Adiciona uma tarefa ao final da lista.
        item = Tarefa(tarefa)
        if self.inicio == None:
            self.inicio = item
            self.fim = item
        else:
            self.fim.proximo = item
            item.anterior = self.fim
            self.fim = item
        self.tamanho += 1
              
               
    def remover_inicio(self):
        # Remove a tarefa do final da lista.
        if self.inicio is None:
            print("Sua lista de tarefas está vazia")
        elif self.inicio.proximo is None:
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None
        self.tamanho -= 1
       
            
    def remover_fim(self):
        if self.inicio is None:
            print("Sua lista de tarefas está vazia")
        elif self.inicio.proximo is None:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None
            self.tamanho -= 1
                
    
    def imprimir(self):
        if self.inicio is None:
            print("Sua lista de tarefas está vazia")
        else:
            print("-------------")
            aux = self.inicio
            while( aux ):
                print( aux.dado)
                aux = aux.proximo
            print(" Total de tarefas: ", str(self.tamanho))
    
    def imprimir_reverso(self):
        if self.inicio is None:
            print("Sua lista de tarefas está vazia")
        else:
            print("---------------")
            aux = self.fim
            while(aux):
                print(aux.dado)
                aux = aux.anterior
            print("Total de elementos: ", str(self.tamanho))          
                      
    def __str__(self):
        # Retorna uma representação em string da lista de tarefas.
        if self.inicio is None:
            return "Sua lista de tarefas está vazia"
        result = "-------------\n"
        aux = self.inicio
        while aux:
            result += str(aux.dado) + "\n"
            aux = aux.proximo
        result += "Total de tarefas: " + str(self.tamanho)
        return result
        
        