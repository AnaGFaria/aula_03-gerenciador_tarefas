from datetime import date
from .enums import Status, Prioridade

class Tarefa:
    def __init__(self, id, titulo, descricao, prioridade, dataLimite, status, projeto):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.dataLimite = dataLimite
        self.status = status
        self.projeto = projeto

    def alterarStatus(self,status):
        self.status = status
        print(f"Status alterado para {self.status.value}")

    def estaVencida(self):
        if self.status == Status.CONCLUIDA:
            return False

        return date.today() > self.dataLimite