
from Tarefa import Tarefa

class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def addInicio(self, tarefa):
        item = Tarefa(tarefa)
        if self.inicio == None:
            self.inicio = item
        else:
            item.proximo = self.inicio
            self.inicio = item
        self.tamanho += 1
        self.imprimir()
    
    def addFim(self, tarefa):
        item = Tarefa(tarefa)
        if self.inicio == None:
            self.inicio = item
        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo
            aux.proximo = item
        self.tamanho += 1
        self.imprimir()      
               
    def removerInicio(self):
        if self.inicio is None:
            raise ValueError("Lista vazia")
        elif self.inicio.proximo is None:
            valor_removido = self.inicio.dado
            self.inicio = None
            self.tamanho -= 1
            return valor_removido
        else:
            valor_removido = self.inicio.dado
            self.inicio = self.inicio.proximo
            self.tamanho -= 1
            return valor_removido
            
    def removerFim(self):
        if self.inicio is None:
            raise ValueError("Lista vazia")
        elif self.inicio.proximo is None:
            valor_removido = self.inicio.dado
            self.inicio = None
            self.tamanho = 0
            return valor_removido
        else:
            ant = self.inicio
            aux = self.inicio.proximo
            while aux.proximo:
                ant = aux
                aux = aux.proximo
            valor_removido = aux.dado
            ant.proximo = None
            self.tamanho -= 1
            return valor_removido
    
    
    
    def imprimir(self):
        if self.inicio is None:
            raise ValueError("Lista vazia")
        else:
            print("-------------")
            aux = self.inicio
            while( aux ):
                print( aux.dado)
                aux = aux.proximo
            print(" Total de tarefas: ", str(self.tamanho))
            
    def __str__(self):
        if self.inicio is None:
            return "Lista vazia"
        result = "-------------\n"
        aux = self.inicio
        while aux:
            result += str(aux.dado) + "\n"
            aux = aux.proximo
        result += "Total de tarefas: " + str(self.tamanho)
        return result
        
        