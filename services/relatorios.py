from models.enums import Status, Prioridade

class Relatorios:
    def __init__(self, usuarios, projetos, tarefas):
        self.usuarios = usuarios
        self.projetos = projetos
        self.tarefas = tarefas

    def relatorioGeral(self):
        print("======================================")
        print("          RELATÓRIO GERAL             ")
        print("======================================")

        print(f"Total de usuários: {len(self.usuarios)}")
        print(f"Total de projetos: {len(self.projetos)}")
        print(f"Total de tarefas: {len(self.tarefas)}")
        print("======================================")

        pendentes = 0
        em_andamento = 0
        concluidas = 0

        baixas = 0
        medias = 0
        altas = 0
        urgentes = 0

        for tarefa in self.tarefas:

            if tarefa.status == Status.PENDENTE:
                pendentes += 1

            elif tarefa.status == Status.EM_ANDAMENTO:
                em_andamento += 1

            elif tarefa.status == Status.CONCLUIDA:
                concluidas += 1

            if tarefa.prioridade == Prioridade.BAIXA:
                baixas += 1

            elif tarefa.prioridade == Prioridade.MEDIA:
                medias += 1

            elif tarefa.prioridade == Prioridade.ALTA:
                altas += 1

            elif tarefa.prioridade == Prioridade.URGENTE:
                urgentes += 1

        print("======================================")
        print("          TAREFAS POR STATUS          ")
        print("======================================")
        print(f"Pendentes: {pendentes}")
        print(f"Em andamento: {em_andamento}")
        print(f"Concluídas: {concluidas}")
        print("======================================")

        print("======================================")
        print("        TAREFAS POR PRIORIDADE        ")
        print("======================================")
        print(f"Baixa: {baixas}")
        print(f"Média: {medias}")
        print(f"Alta: {altas}")
        print(f"Urgente: {urgentes}")
        print("======================================")


    def relatorioUsuarios(self):
        print("======================================")
        print("        RELATÓRIO DE USUÁRIOS         ")
        print("======================================")

        if not self.usuarios:
            print("\nNenhum usuário cadastrado.")
            print("======================================")
            return

        for usuario in self.usuarios:
            print("\n------------------------------------")
            print(f"ID: {usuario.id}")
            print(f"Nome: {usuario.nome}")
            print(f"Email: {usuario.email}")
            print(f"Projetos: {len(usuario.projetos)}")
            print("======================================")


    def relatorioProjetos(self):
        print("======================================")
        print("        RELATÓRIO DE PROJETOS         ")
        print("======================================")

        if not self.projetos:
            print("\nNenhum projeto cadastrado.")
            return

        for projeto in self.projetos:
            progresso = projeto.calcularProgresso()

            print("\n------------------------------------")
            print(f"ID: {projeto.id}")
            print(f"Nome: {projeto.nome}")
            print(f"Descrição: {projeto.descricao}")
            print(f"Usuário: {projeto.usuario.nome}")
            print(f"Tarefas: {len(projeto.tarefas)}")
            print(f"Progresso: {progresso:.2f}%")
            print("======================================")


    def relatorioTarefas(self):
        print("======================================")
        print("         RELATÓRIO DE TAREFAS         ")
        print("======================================")

        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
            return

        for tarefa in self.tarefas:
            print("\n------------------------------------")
            print(f"ID: {tarefa.id}")
            print(f"Título: {tarefa.titulo}")
            print(f"Descrição: {tarefa.descricao}")
            print(f"Prioridade: {tarefa.prioridade.value}")
            print(f"Status: {tarefa.status.value}")
            print(f"Data limite: {tarefa.dataLimite}")
            print(f"Projeto: {tarefa.projeto.nome}")
            print("======================================")


    def relatorioTarefasVencidas(self):
        print("======================================")
        print("           TAREFAS VENCIDAS           ")
        print("======================================")

        tarefas_vencidas = []

        for tarefa in self.tarefas:
            if tarefa.estaVencida():
                tarefas_vencidas.append(tarefa)

        if not tarefas_vencidas:
            print("\nNenhuma tarefa vencida.")
            return

        print(f"\nTotal de tarefas vencidas: {len(tarefas_vencidas)}")

        for tarefa in tarefas_vencidas:
            print("\n------------------------------------")
            print(f"ID: {tarefa.id}")
            print(f"Título: {tarefa.titulo}")
            print(f"Data limite: {tarefa.dataLimite}")
            print(f"Status: {tarefa.status.value}")
            print(f"Projeto: {tarefa.projeto.nome}")