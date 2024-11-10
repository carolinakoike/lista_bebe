import tkinter as tk
from tkinter import messagebox
from services.database import obter_dados_bebe, atualizar_dados_bebe, inserir_dados_bebe

def abrir_tela_informacoes_bebe(usuario_id):
    janela_bebe = tk.Toplevel()
    janela_bebe.title("Informações do Bebê")
    janela_bebe.geometry("300x300")

    tk.Label(janela_bebe, text="Nome do Bebê").pack()
    entry_nome = tk.Entry(janela_bebe)
    entry_nome.pack()

    tk.Label(janela_bebe, text="Data de Nascimento (DD/MM/AAAA)").pack()
    entry_data_nascimento = tk.Entry(janela_bebe)
    entry_data_nascimento.pack()

    tk.Label(janela_bebe, text="Gênero").pack()
    entry_genero = tk.Entry(janela_bebe)
    entry_genero.pack()

    tk.Label(janela_bebe, text="Peso ao Nascer (kg)").pack()
    entry_peso = tk.Entry(janela_bebe)
    entry_peso.pack()

    tk.Label(janela_bebe, text="Observações").pack()
    entry_observacoes = tk.Entry(janela_bebe)
    entry_observacoes.pack()

    dados_bebe = obter_dados_bebe(usuario_id)
    if dados_bebe:
        entry_nome.insert(0, dados_bebe[1]) 
        entry_data_nascimento.insert(0, dados_bebe[2])  
        entry_genero.insert(0, dados_bebe[3])  
        entry_peso.insert(0, dados_bebe[4])  
        entry_observacoes.insert(0, dados_bebe[5])  

    def salvar_cadastro():
        nome = entry_nome.get().strip()
        data_nascimento = entry_data_nascimento.get().strip()
        genero = entry_genero.get().strip()
        peso = entry_peso.get().strip()
        observacoes = entry_observacoes.get().strip()

        if nome and data_nascimento and genero:
            if dados_bebe:
                atualizar_dados_bebe(dados_bebe[0], nome, data_nascimento, genero, peso, observacoes)
                messagebox.showinfo("Sucesso", "Cadastro atualizado com sucesso!")
            else:
                inserir_dados_bebe(nome, data_nascimento, genero, peso, observacoes, usuario_id)
                messagebox.showinfo("Sucesso", "Cadastro criado com sucesso!")
            janela_bebe.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    button_salvar = tk.Button(janela_bebe, text="Salvar/Atualizar Cadastro", command=salvar_cadastro)
    button_salvar.pack()

    button_cancelar = tk.Button(janela_bebe, text="Cancelar", command=janela_bebe.destroy)
    button_cancelar.pack()
