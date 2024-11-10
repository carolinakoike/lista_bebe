import sqlite3

def criar_banco():
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens_enxoval (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT,
        quantidade INTEGER,
        usuario_id INTEGER,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados_bebe (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data_nascimento TEXT,
        genero TEXT,
        peso_nascimento REAL,
        observacoes TEXT,
        usuario_id INTEGER,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)

    conn.commit()
    conn.close()

def autenticar_usuario(nome, senha):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, senha))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

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

def atualizar_usuario(id_usuario, novo_nome, nova_senha):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nome = ?, senha = ? WHERE id = ?", (novo_nome, nova_senha, id_usuario))
    conn.commit()
    conn.close()

def adicionar_item(nome_item, categoria_item, quantidade_item, usuario_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO itens_enxoval (nome, categoria, quantidade, usuario_id) VALUES (?, ?, ?, ?)",
                   (nome_item, categoria_item, quantidade_item, usuario_id))
    conn.commit()
    conn.close()

def obter_itens_enxoval(usuario_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM itens_enxoval WHERE usuario_id = ?", (usuario_id,))
    itens = cursor.fetchall()
    conn.close()
    return itens

def deletar_item(item_id, usuario_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM itens_enxoval WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

def inserir_dados_bebe(nome, data_nascimento, genero, peso_nascimento, observacoes, usuario_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO dados_bebe (nome, data_nascimento, genero, peso_nascimento, observacoes, usuario_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, data_nascimento, genero, peso_nascimento, observacoes, usuario_id))
    conn.commit()
    conn.close()

def obter_dados_bebe(usuario_id):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dados_bebe WHERE usuario_id = ?", (usuario_id,))
    dados = cursor.fetchone()
    conn.close()
    return dados

def atualizar_dados_bebe(id, nome, data_nascimento, genero, peso_nascimento, observacoes):
    conn = sqlite3.connect("enxoval_bebe.db")
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE dados_bebe SET nome = ?, data_nascimento = ?, genero = ?, peso_nascimento = ?, observacoes = ?
        WHERE id = ?
    """, (nome, data_nascimento, genero, peso_nascimento, observacoes, id))
    conn.commit()
    conn.close()
