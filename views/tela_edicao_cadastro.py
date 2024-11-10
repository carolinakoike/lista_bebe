import tkinter as tk
from tkinter import messagebox
from services.database import atualizar_usuario, autenticar_usuario

def abrir_tela_edicao_cadastro(usuario_id, nome_atual):
    janela_edicao = tk.Toplevel()
    janela_edicao.title("Editar Cadastro")
    janela_edicao.geometry("300x250")

    tk.Label(janela_edicao, text="Nome Atual:").pack()
    tk.Label(janela_edicao, text=nome_atual).pack()

    tk.Label(janela_edicao, text="Novo Nome:").pack()
    entry_novo_nome = tk.Entry(janela_edicao)
    entry_novo_nome.pack()

    tk.Label(janela_edicao, text="Nova Senha:").pack()
    entry_nova_senha = tk.Entry(janela_edicao, show="*")
    entry_nova_senha.pack()

    def salvar_alteracoes():
        novo_nome = entry_novo_nome.get().strip()
        nova_senha = entry_nova_senha.get().strip()
        
        if novo_nome and nova_senha:
            atualizar_usuario(usuario_id, novo_nome, nova_senha)
            messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
            janela_edicao.destroy()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    tk.Button(janela_edicao, text="Salvar Alterações", command=salvar_alteracoes).pack(pady=10)
