
class Tarefa:
    def __init__(self, descricao, identificacao):
        self.descricao = descricao
        self.identificacao = identificacao
        self.proximo = None
        self.anterior = None