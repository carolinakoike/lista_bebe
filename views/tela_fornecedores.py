import tkinter as tk
from tkinter import messagebox
from services.api_requests import obter_fornecedores_proximos

API_KEY_FOURSQUARE = "fsq3QdloZQDELAzVTqhbh/jW4E0B+4zVmGX0GDL1x1b8z6Y="

def abrir_tela_fornecedores():
    janela_fornecedores = tk.Toplevel()
    janela_fornecedores.title("Fornecedores Próximos")
    janela_fornecedores.geometry("400x450")

    tk.Label(janela_fornecedores, text="Informe a cidade:").pack()
    entry_cidade = tk.Entry(janela_fornecedores)
    entry_cidade.pack()

    tk.Label(janela_fornecedores, text="Tipo de estabelecimento (ex: store, pharmacy, etc.):").pack()
    entry_tipo = tk.Entry(janela_fornecedores)
    entry_tipo.pack()

    frame_lista = tk.Frame(janela_fornecedores)
    frame_lista.pack(fill="both", expand=True)

    lista_fornecedores = tk.Listbox(frame_lista, width=50, height=15)
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=lista_fornecedores.yview)
    lista_fornecedores.config(yscrollcommand=scrollbar.set)

    lista_fornecedores.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def mostrar_fornecedores():
        cidade = entry_cidade.get().strip()
        tipo_estabelecimento = entry_tipo.get().strip()
        if not cidade or not tipo_estabelecimento:
            messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade e o tipo de estabelecimento.")
            return

        fornecedores = obter_fornecedores_proximos(cidade, tipo_estabelecimento, API_KEY_FOURSQUARE)
        if fornecedores:
            lista_fornecedores.delete(0, tk.END)
            for fornecedor in fornecedores:
                lista_fornecedores.insert(tk.END, f"{fornecedor['nome']} - {fornecedor['endereco']}")
        else:
            messagebox.showerror("Erro", "Não foi possível encontrar fornecedores para essa cidade.")

    button_fornecedores = tk.Button(janela_fornecedores, text="Ver Fornecedores Próximos", command=mostrar_fornecedores)
    button_fornecedores.pack()
