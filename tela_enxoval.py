import tkinter as tk
from tkinter import messagebox
from services.database import criar_banco, adicionar_item, obter_itens_enxoval, deletar_item

# Função para abrir a tela de enxoval
def abrir_tela_enxoval():
    criar_banco()  # Garante que o banco e a tabela de itens de enxoval estão criados

    janela_enxoval = tk.Toplevel()
    janela_enxoval.title("Lista de Enxoval")
    janela_enxoval.geometry("400x400")

    tk.Label(janela_enxoval, text="Nome do Item").pack()
    entry_nome = tk.Entry(janela_enxoval)
    entry_nome.pack()

    tk.Label(janela_enxoval, text="Categoria").pack()
    entry_categoria = tk.Entry(janela_enxoval)
    entry_categoria.pack()

    tk.Label(janela_enxoval, text="Quantidade").pack()
    entry_quantidade = tk.Entry(janela_enxoval)
    entry_quantidade.pack()

    # Frame para agrupar a lista e a scrollbar
    frame_lista = tk.Frame(janela_enxoval)
    frame_lista.pack(fill="both", expand=True)

    # Lista de itens e scrollbar
    lista_itens = tk.Listbox(frame_lista, width=50, height=10)
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=lista_itens.yview)
    lista_itens.config(yscrollcommand=scrollbar.set)

    lista_itens.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    button_adicionar = tk.Button(janela_enxoval, text="Adicionar Item", command=lambda: adicionar_item_interface(entry_nome, entry_categoria, entry_quantidade, lista_itens))
    button_adicionar.pack()

    button_deletar = tk.Button(janela_enxoval, text="Deletar Item", command=lambda: deletar_item_interface(lista_itens))
    button_deletar.pack()

    atualizar_lista(lista_itens)

# Função para adicionar item ao enxoval
def adicionar_item_interface(entry_nome, entry_categoria, entry_quantidade, lista_itens):
    nome_item = entry_nome.get()
    categoria_item = entry_categoria.get()
    quantidade_item = entry_quantidade.get()

    if nome_item and quantidade_item.isdigit():
        adicionar_item(nome_item, categoria_item, int(quantidade_item))
        messagebox.showinfo("Sucesso", "Item adicionado ao enxoval!")
        atualizar_lista(lista_itens)
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")

# Função para atualizar a lista de itens
def atualizar_lista(lista_itens):
    lista_itens.delete(0, tk.END)
    itens = obter_itens_enxoval()
    for item in itens:
        # Exibindo o item com seu id
        lista_itens.insert(tk.END, f"{item[0]} - {item[1]} - {item[2]} - Quantidade: {item[3]}")

# Função para deletar item do enxoval
def deletar_item_interface(lista_itens):
    try:
        item_selecionado = lista_itens.curselection()
        if not item_selecionado:
            messagebox.showerror("Erro", "Selecione um item para deletar.")
            return
        item_texto = lista_itens.get(item_selecionado)
        # Extraindo o ID do item selecionado
        item_id = int(item_texto.split(" - ")[0])
        
        deletar_item(item_id)
        messagebox.showinfo("Sucesso", "Item deletado do enxoval!")
        atualizar_lista(lista_itens)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao deletar item: {e}")
