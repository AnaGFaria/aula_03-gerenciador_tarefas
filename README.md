# Gerenciador Inteligente de Tarefas
Projeto desenvolvido para a aula 03 de Programação Orientada a Objetos

## 1. Sobre o projeto
Este projeto é um sistema de gerenciamento de tarefas desenvolvido em Python, aplicando os principais conceitos de Programação Orientada a Objetos.\
O sistema permite criar usuários, cadastrar projetos e tarefas, definir prioridades, acompanhar o progresso e gerar relatórios de produtividade.

## 2. Objetivo
Praticar os pilares da POO na construção de um sistema completo, modular e reutilizável.

## 3. Funcionalidades
- [x] Cadastro de usuários
- [x] Gerenciamento de projetos
- [x] Gerenciamento de tarefas
- [x] Definição de prioridades
- [x] Acompanhamento de progresso
- [x] Relatórios

## 4. Tecnologias utilizadas
![Python](https://img.shields.io/badge/Python-3.14+-blue?logo=python&logoColor=white)
![POO](https://img.shields.io/badge/Paradigma-POO-purple)
![CLI](https://img.shields.io/badge/Interface-CLI-black?logo=windowsterminal)

## 5. Estrutura do projeto

```
aula_03-gerenciador_tarefas/
├── main.py              # Ponto de entrada do programa
├── models/              # Classes de domínio (entidades)
│   ├── enums.py         # Enumerações para status e prioridade das tarefas
│   ├── projeto.py       # Classe Projeto
│   └── tarefa.py        # Classe Tarefa
│   └── usuario.py       # Classe Usuario
├── services/            # Regras de negócio
│   ├── relatorios.py    # Classe Relatório
└── README.md            # Documentação do projeto
```

## 6. Como executar

```
# 1. Clone o repositório
git clone https://github.com/AnaGFaria/aula_03-gerenciador_tarefas.git
cd aula_03-gerenciador_tarefas

# 2. Execute o projeto
python main.py
```

## 7. Exemplo de uso
<img width="1482" height="762" alt="image" src="https://github.com/user-attachments/assets/aa3ddba2-8502-4567-b3df-2e4a9b27353e" />

## 8. Autor
Desenvolvido por **Ana Gabriela de Faria**\
Estudante de Ciência da Computação
