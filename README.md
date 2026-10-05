# Help Desk Python

Sistema simples de abertura e gerenciamento de chamados técnicos, simulando um service desk. Projeto voltado para prática de ITIL, organização de atendimentos N1/N2 e manipulação de banco de dados com SQLite.

## Funcionalidades

- Abrir chamado com nome do usuário, setor, descrição e prioridade
- Listar chamados abertos
- Marcar chamado como resolvido
- Persistência de dados em SQLite
- Menu interativo no terminal

## Tecnologias

- Python 3.10+
- SQLite (nativo do Python)
- Biblioteca `datetime`

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/WolfiBr66/help-desk-python.git
cd help-desk-python
```

2. Execute o script:
```bash
python main.py
```

3. Use o menu para abrir, listar ou resolver chamados.

## Estrutura do projeto
```
help-desk-python/
├── main.py
├── chamados.db
└── README.md
```

## Aprendizados

- Modelagem de dados com SQLite
- Aplicação de conceitos de ITIL (incidentes e solicitações)
- Estruturação de menus e fluxo de atendimento

## Autor

Marcelo Junio Siqueira Gonçalo
[LinkedIn](https://www.linkedin.com/in/marcelogoncalo/) | [GitHub](https://github.com/WolfiBr66)