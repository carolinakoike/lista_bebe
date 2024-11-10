import tkinter as tk
from tkinter import messagebox
from services.database import obter_itens_enxoval

def abrir_tela_categorias(usuario_id):
    janela_categorias = tk.Toplevel()
    janela_categorias.title("Categorias de Enxoval")
    janela_categorias.geometry("400x400")

    tk.Label(janela_categorias, text="Digite a Categoria").pack()
    entry_categoria = tk.Entry(janela_categorias)
    entry_categoria.pack()

    lista_categorias_itens = tk.Listbox(janela_categorias, width=50, height=10)
    lista_categorias_itens.pack()

    def filtrar_por_categoria():
        categoria = entry_categoria.get().strip()
        lista_categorias_itens.delete(0, tk.END)
        
        itens = obter_itens_enxoval(usuario_id)  
        itens_filtrados = [item for item in itens if item[2] == categoria]
        
        if itens_filtrados:
            for item in itens_filtrados:
                lista_categorias_itens.insert(tk.END, f"{item[1]} - Quantidade: {item[3]}")
        else:
            messagebox.showinfo("Aviso", f"Nenhum item encontrado na categoria '{categoria}'.")

    button_filtrar = tk.Button(janela_categorias, text="Filtrar", command=filtrar_por_categoria)
    button_filtrar.pack()
