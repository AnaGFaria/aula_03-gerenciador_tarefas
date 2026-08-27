from models.usuario import Usuario
from models.enums import Status, Prioridade
from services.relatorios import Relatorios

from datetime import datetime

import os

usuarios = []
projetos = []
tarefas = []

id_usuario_input = 1
id_tarefa_input = 1
id_projeto_input = 1

while True:

    os.system('cls')
    print("====================================")
    print("       GERENCIADOR DE TAREFAS       ")
    print("====================================")

    print("1 - Cadastrar usuário")
    print("2 - Criar projeto")
    print("3 - Adicionar tarefa")
    print("4 - Listar projetos")
    print("5 - Listar tarefas")
    print("6 - Alterar status da tarefa")
    print("7 - Ver progresso do projeto")
    print("8 - Relatórios")
    print("9 - Remover usuário")
    print("0 - Sair")

    user_input = input("Digite o número correspondente: ")

    match user_input:
        case "0":
            break

        case "1":
            nome = input("Informe o nome do usuário: ")
            email = input("Informe o email do usuário: ")
            senha = input("Informe a senha do usuário: ")

            usuario = Usuario(id_usuario_input, nome, email, senha)

            usuarios.append(usuario)

            print(f"Usuário criado.\nID de Usuário: {id_usuario_input}")

            id_usuario_input += 1

            input("Digite qualquer tecla para sair...")

        case "2":
            try:
                id_usuario = int(input("Informe o id do usuário: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if not usuarios:
                print("Nenhum usuário cadastrado.")
                input("Digite qualquer tecla para sair...")
                continue

            if usuarios:
                for usuario in usuarios:
                    if usuario.id == id_usuario:
                        nome = input("Informe o nome do projeto: ")
                        descricao = input("Informe a descrição do projeto: ")

                        projeto = usuario.criarProjeto(id_projeto_input, nome, descricao)
                        
                        id_projeto_input += 1
            
                        projetos.append(projeto)
                        break
                else:
                    print("Usuario não encontrado")
            
            input("Digite qualquer tecla para sair...")

        case "3":
            try:
                id_projeto = int(input("Informe o id do projeto: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if projetos:
                for projeto in projetos:
                    if projeto.id == id_projeto:
                        titulo = input("Informe o título da tarefa: ")
                        descricao = input("Informe a descrição da tarefa: ")

                        while True:
                            print("\nNíveis de prioridade")
                            print("1 - Baixa")
                            print("2 - Média")
                            print("3 - Alta")
                            print("4 - Urgente")

                            prioridade_input = input("Informe o número de prioridade da tarefa: ")

                            match prioridade_input:
                                case "1":
                                    prioridade = Prioridade.BAIXA
                                    break
                                case "2":
                                    prioridade = Prioridade.MEDIA
                                    break
                                case "3":
                                    prioridade = Prioridade.ALTA
                                    break
                                case "4":
                                    prioridade = Prioridade.URGENTE
                                    break
                                case _:
                                    print("Opção inválida!")

                        while True:
                            print("\nNíveis de status")
                            print("1 - Pendente")
                            print("2 - Em andamento")
                            print("3 - Concluída")
                            status_input = input("Informe o número do status da tarefa: ")

                            match status_input:
                                case "1":
                                    status = Status.PENDENTE
                                    break
                                case "2":
                                    status = Status.EM_ANDAMENTO
                                    break
                                case "3":
                                    status = Status.CONCLUIDA
                                    break
                                case _:
                                    print("Opção inválida!")

                        while True:
                            data = input("Informe a data limite da tarefa (ANO-MÊS-DIA): ")

                            try:
                                data = datetime.strptime(data, "%Y-%m-%d").date()
                                break
                            except ValueError:
                                print("Data inválida! Use o formato ANO-MÊS-DIA.")
                                
                        tarefa = projeto.adicionarTarefa(id_tarefa_input, titulo, descricao, prioridade, data, status)
                                 
                        id_tarefa_input += 1
                        
                        tarefas.append(tarefa)
                        break
                else:
                    print("Projeto não encontrado")

            input("Digite qualquer tecla para sair...")

        case "4":
            try:
                id_usuario = int(input("Informe o id do usuário: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if usuarios:
                for usuario in usuarios:
                    if usuario.id == id_usuario:
                        usuario.listarProjetos()
                        break
                else:
                    print("Usuário não encontrado")

            
            input("Digite qualquer tecla para sair...")
                    
        case "5":
            try:
                id_projeto = int(input("Informe o id do projeto: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if projetos:
                for projeto in projetos:
                    if projeto.id == id_projeto:
                        projeto.listarTarefas()
                        break
                else:
                    print("Projeto não encontrado")

            input("Digite qualquer tecla para sair...")

        case "6":
            try:
                id_tarefa = int(input("Informe o id do tarefa: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if tarefas:
                for tarefa in tarefas:
                    if tarefa.id == id_tarefa:
                        print("\nNíveis de status")
                        print("1 - Pendente")
                        print("2 - Em andamento")
                        print("3 - Concluída")

                        while True:
                            status_input = input("Informe o número correspondente ao status da tarefa: ")
                            match status_input:
                                case "1":
                                    status = Status.PENDENTE
                                    break
                                case "2":
                                    status = Status.EM_ANDAMENTO
                                    break
                                case "3":
                                    status = Status.CONCLUIDA
                                    break
                                case _:
                                    print("Opção inválida!")

                        tarefa.alterarStatus(status)
                        break
                else:
                    print("Tarefa não encontrado")

            input("Digite qualquer tecla para sair...")

        case "7":
            try:
                id_projeto = int(input("Informe o id do projeto: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                input("Digite qualquer tecla para sair...")
                continue

            if projetos:
                for projeto in projetos:
                    if projeto.id == id_projeto:
                        projeto.calcularProgresso()
                        break
                else:
                    print("Projeto não encontrado")

            input("Digite qualquer tecla para sair...")

        case "8":
            relatorio = Relatorios(usuarios, projetos, tarefas)

            while True:
                os.system('cls')

                print("====================================")
                print("             RELATÓRIOS             ")
                print("====================================")

                print("1 - Relatório geral")
                print("2 - Relatório de usuários")
                print("3 - Relatório de projetos")
                print("4 - Relatório de tarefas")
                print("5 - Tarefas vencidas")
                print("0 - Voltar")

                relatorio_input = input("Digite o número correspondente: ")

                match relatorio_input:

                    case "1":
                        os.system('cls')
                        relatorio.relatorioGeral()
                        input("\nDigite qualquer tecla para continuar...")

                    case "2":
                        os.system('cls')
                        relatorio.relatorioUsuarios()
                        input("\nDigite qualquer tecla para continuar...")

                    case "3":
                        os.system('cls')
                        relatorio.relatorioProjetos()
                        input("\nDigite qualquer tecla para continuar...")

                    case "4":
                        os.system('cls')
                        relatorio.relatorioTarefas()
                        input("\nDigite qualquer tecla para continuar...")

                    case "5":
                        os.system('cls')
                        relatorio.relatorioTarefasVencidas()
                        input("\nDigite qualquer tecla para continuar...")

                    case "0":
                        break

                    case _:
                        print("\nOpção inválida!")
                        input("\nDigite qualquer tecla para continuar...")

        case "9":
            try:
                id_usuario = int(input("Informe o ID do usuário que deseja remover: "))
            except ValueError:
                print("ID inválido! Digite apenas números.")
                continue

            usuario_encontrado = None

            if usuarios:
                for usuario in usuarios:
                    if usuario.id == id_usuario:
                        usuario.listarProjetos()
                        usuario_encontrado = usuario
                        break
                else:
                    print("Usuário não encontrado")

            if usuario_encontrado is None:
                print("\nUsuário não encontrado.")
                input("\nDigite qualquer tecla para continuar...")
                continue

            print("\nUsuário encontrado!")
            print(f"ID: {usuario_encontrado.id}")
            print(f"Nome: {usuario_encontrado.nome}")
            print(f"Email: {usuario_encontrado.email}")
            print(
                f"Projetos: "
                f"{len(usuario_encontrado.projetos)}"
            )

            confirmacao = input("\nTem certeza que deseja remover este usuário? (s/n): ").lower()

            if confirmacao != "s":
                print("\nOperação cancelada.")
                continue

            for projeto in usuario_encontrado.projetos:
                for tarefa in projeto.tarefas:
                    if tarefa in tarefas:
                        tarefas.remove(tarefa)

                if projeto in projetos:
                    projetos.remove(projeto)

            usuarios.remove(usuario_encontrado)

            print("\nUsuário removido com sucesso!")
            input("\nDigite qualquer tecla para continuar...")

        case _:
            print("\nOpção inválida! Digite uma opção válida.")