from datetime import date
from .projeto import Projeto

class Usuario:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

        self.projetos = []

    def criarProjeto(self, id, nome, descricao):
        dataCriacao = date.today()

        projeto = Projeto(id, nome, descricao, dataCriacao, self)

        self.projetos.append(projeto)

        print("\nProjeto criado:")
        print(f"ID do projeto: {id}")
        print(f"Nome do projeto: {nome}")
        print(f"Descrição do projeto: {descricao}")
        print(f"Data de criação do projeto: {dataCriacao}")
        print(f"Usuário de criação do projeto: {self.id}")

        return projeto

    def listarProjetos(self):
        projetos = self.projetos
        
        print("\n\n======================================================")
        print("                       PROJETOS                       ")
        for projeto in projetos:
            if projeto.usuario is self:
                print("======================================================")
                print(f"Nome do projeto: {projeto.nome}")
                print(f"ID do projeto: {projeto.id}")
                print(f"Descrição do projeto: {projeto.descricao}")
                print(f"Data de criação do projeto: {projeto.dataCriacao}")
                print(f"Usuário de criação do projeto: {projeto.usuario.id}")
        print("======================================================")

    def removerProjeto(self,id_projeto):
        for projeto in self.projetos:
            if projeto.id == id_projeto:
                self.projetos.remove(projeto)
                print(f"\nProjeto apagado. ID: {projeto.id}")