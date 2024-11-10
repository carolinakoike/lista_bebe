import tkinter as tk
from tkinter import messagebox
from views.tela_menu import abrir_menu
from services.database import criar_banco, autenticar_usuario, cadastrar_usuario

def iniciar_tela_login():
    global entry_usuario, entry_senha, root
    root = tk.Tk()
    root.title("Login - Enxoval de Bebê")
    root.geometry("300x200")
    
    criar_banco()

    tk.Label(root, text="Usuário").pack()
    entry_usuario = tk.Entry(root)
    entry_usuario.pack()

    tk.Label(root, text="Senha").pack()
    entry_senha = tk.Entry(root, show="*")
    entry_senha.pack()

    button_login = tk.Button(root, text="Login", command=login)
    button_login.pack()

    button_cadastro = tk.Button(root, text="Cadastrar Novo Usuário", command=abrir_cadastro)
    button_cadastro.pack()

    root.mainloop()

def login():
    nome_usuario = entry_usuario.get()
    senha_usuario = entry_senha.get()

    usuario = autenticar_usuario(nome_usuario, senha_usuario)  

    if usuario:
        messagebox.showinfo("Login", "Login bem-sucedido!")
        usuario_id = usuario[0]  
        nome_atual = usuario[1] 
        root.withdraw()  
        abrir_menu(root, usuario_id, nome_atual)  
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")

def abrir_cadastro():
    global cadastro_janela, entry_cadastro_usuario, entry_cadastro_senha
    cadastro_janela = tk.Toplevel(root)
    cadastro_janela.title("Cadastro de Usuário")
    cadastro_janela.geometry("300x200")

    tk.Label(cadastro_janela, text="Usuário").pack()
    entry_cadastro_usuario = tk.Entry(cadastro_janela)
    entry_cadastro_usuario.pack()

    tk.Label(cadastro_janela, text="Senha").pack()
    entry_cadastro_senha = tk.Entry(cadastro_janela, show="*")
    entry_cadastro_senha.pack()

    button_confirmar_cadastro = tk.Button(cadastro_janela, text="Cadastrar", command=cadastrar)
    button_confirmar_cadastro.pack()

def cadastrar():
    nome_usuario = entry_cadastro_usuario.get()
    senha_usuario = entry_cadastro_senha.get()

    if nome_usuario and senha_usuario:
        if cadastrar_usuario(nome_usuario, senha_usuario):
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            cadastro_janela.destroy()
        else:
            messagebox.showerror("Erro", "Nome de usuário já existente!")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos!")
