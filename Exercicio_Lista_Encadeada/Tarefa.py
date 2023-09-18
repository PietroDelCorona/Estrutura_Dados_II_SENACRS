
class Tarefa:
    def __init__(self, tarefa, descricao, identificacao):
        self.descricao = descricao
        self.identificacao = identificacao
        self.dado = tarefa
        self.proximo = None
        self.anterior = None