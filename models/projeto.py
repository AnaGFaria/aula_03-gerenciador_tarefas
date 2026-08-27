from .tarefa import Tarefa
from .enums import Status, Prioridade

class Projeto:
    def __init__(self, id, nome, descricao, dataCriacao, usuario):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.dataCriacao = dataCriacao
        self.usuario = usuario
        self.tarefas = []

    def adicionarTarefa(self, id, titulo, descricao, prioridade, dataLimite, status):
        tarefa = Tarefa(id, titulo, descricao, prioridade, dataLimite, status, self)
        
        self.tarefas.append(tarefa)

        print("\nTarefa criada:")
        print(f"Nome da tarefa: {titulo}")
        print(f"Descrição da tarefa: {descricao}")
        print(f"Prioridade: {prioridade.value}")
        print(f"Data limite: {dataLimite}")
        print(f"Status: {status.value}")

        return tarefa

    def removerTarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                print(f"\nTarefa apagada. ID: {tarefa.id}")

    def calcularProgresso(self):
        if not self.tarefas:
            print("Progresso do projeto: 0%")
            return 0

        tarefas_concluidas = 0

        for tarefa in self.tarefas:
            if tarefa.status == Status.CONCLUIDA:
                tarefas_concluidas += 1

        progresso = (tarefas_concluidas / len(self.tarefas)) * 100
        print(f"Progresso do projeto: {progresso:.2f}%")

        return progresso

    def listarTarefas(self):
        tarefas = self.tarefas
        
        print("\n\n======================================================")
        print("                          TAREFAS                         ")
        for tarefa in tarefas:
            if tarefa.projeto is self:
                print("======================================================")
                print(f"ID: {tarefa.id}")
                print(f"Título: {tarefa.titulo}")
                print(f"Descrição: {tarefa.descricao}")
                print(f"Prioridade: {tarefa.prioridade.value}")
                print(f"Data limite: {tarefa.dataLimite}")
                print(f"Status: {tarefa.status.value}")
        print("======================================================")