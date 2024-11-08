import sqlite3

# Conexão e criação das tabelas do banco de dados
def criar_banco():
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    
    # Tabela de usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)

    # Tabela de itens de enxoval
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens_enxoval (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        quantidade INTEGER
    )
    """)

    conn.commit()
    conn.close()

# Função para autenticar o login
def autenticar_usuario(nome, senha):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

# Função para cadastrar um novo usuário
def cadastrar_usuario(nome, senha):
    try:
        conn = sqlite3.connect("enxoval_bebe.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", (nome, senha))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

# Função para adicionar um novo item ao enxoval
def adicionar_item(nome_item, categoria_item, quantidade_item):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO itens_enxoval (nome, categoria, quantidade) VALUES (?, ?, ?)",
                   (nome_item, categoria_item, quantidade_item))
    conn.commit()
    conn.close()

# Função para obter itens do enxoval
def obter_itens_enxoval():
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens_enxoval")
    itens = cursor.fetchall()
    conn.close()
    return itens

# Função para deletar um item do enxoval pelo ID
def deletar_item(item_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM itens_enxoval WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
