import sqlite3
from datetime import datetime

def criar_tabela():
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            setor TEXT,
            descricao TEXT,
            prioridade TEXT,
            status TEXT DEFAULT 'Aberto',
            data_abertura TEXT
        )
    """)
    conn.commit()
    conn.close()

def abrir_chamado():
    usuario = input("Nome do usuário: ")
    setor = input("Setor: ")
    descricao = input("Descrição do problema: ")
    prioridade = input("Prioridade (Baixa/Média/Alta): ")
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO chamados (usuario, setor, descricao, prioridade, data_abertura)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario, setor, descricao, prioridade, datetime.now().strftime("%d/%m/%Y %H:%M")))
    conn.commit()
    conn.close()
    print("Chamado aberto com sucesso!")

def listar_chamados():
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, usuario, setor, descricao, prioridade, status, data_abertura FROM chamados WHERE status = 'Aberto'")
    chamados = cursor.fetchall()
    if not chamados:
        print("Nenhum chamado aberto.")
    else:
        for c in chamados:
            print(f"ID: {c[0]} | Usuário: {c[1]} | Setor: {c[2]} | Prioridade: {c[4]} | Status: {c[5]} | Data: {c[6]}")
            print(f"   Descrição: {c[3]}")
    conn.close()

def resolver_chamado():
    id_chamado = input("ID do chamado a resolver: ")
    conn = sqlite3.connect("chamados.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE chamados SET status = 'Resolvido' WHERE id = ?", (id_chamado,))
    conn.commit()
    if cursor.rowcount > 0:
        print("Chamado marcado como resolvido.")
    else:
        print("Chamado não encontrado.")
    conn.close()

if __name__ == "__main__":
    criar_tabela()
    while True:
        print("\n=== HELP DESK ===")
        print("1 - Abrir chamado")
        print("2 - Listar chamados abertos")
        print("3 - Resolver chamado")
        print("4 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            abrir_chamado()
        elif opcao == "2":
            listar_chamados()
        elif opcao == "3":
            resolver_chamado()
        elif opcao == "4":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")