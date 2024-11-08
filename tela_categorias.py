import tkinter as tk
from tkinter import messagebox
from services.database import obter_itens_enxoval

# Função para abrir a tela de categorias
def abrir_tela_categorias():
    janela_categorias = tk.Toplevel()
    janela_categorias.title("Categorias de Enxoval")
    janela_categorias.geometry("400x400")

    tk.Label(janela_categorias, text="Digite a Categoria").pack()
    entry_categoria = tk.Entry(janela_categorias)
    entry_categoria.pack()

    # Frame para agrupar a lista e a scrollbar
    frame_lista = tk.Frame(janela_categorias)
    frame_lista.pack(fill="both", expand=True)

    # Lista de itens e barra de rolagem
    lista_categorias_itens = tk.Listbox(frame_lista, width=50, height=10)
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=lista_categorias_itens.yview)
    lista_categorias_itens.config(yscrollcommand=scrollbar.set)

    lista_categorias_itens.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Função interna para filtrar os itens pela categoria inserida
    def filtrar_por_categoria():
        categoria = entry_categoria.get().strip()
        lista_categorias_itens.delete(0, tk.END)
        
        itens = obter_itens_enxoval()
        itens_filtrados = [item for item in itens if item[2] == categoria]
        
        if itens_filtrados:
            for item in itens_filtrados:
                lista_categorias_itens.insert(tk.END, f"{item[1]} - Quantidade: {item[3]}")
        else:
            messagebox.showinfo("Aviso", f"Nenhum item encontrado na categoria '{categoria}'.")

    # Botão para filtrar
    button_filtrar = tk.Button(janela_categorias, text="Filtrar", command=filtrar_por_categoria)
    button_filtrar.pack()
