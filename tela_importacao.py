import tkinter as tk
from tkinter import filedialog, messagebox
from services.import_utils import importar_enxoval_de_json

# Função para abrir a tela de importação
def abrir_tela_importacao():
    janela_importacao = tk.Toplevel()
    janela_importacao.title("Importação de Itens de Enxoval")
    janela_importacao.geometry("300x200")

    tk.Label(janela_importacao, text="Importar lista de enxoval de um arquivo JSON").pack(pady=10)

    # Função para selecionar o arquivo e realizar a importação
    def importar():
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if caminho_arquivo:
            sucesso = importar_enxoval_de_json(caminho_arquivo)
            if sucesso:
                messagebox.showinfo("Importação Concluída", "Itens importados com sucesso!")
            else:
                messagebox.showerror("Erro", "Erro ao importar o arquivo.")

    # Botão para selecionar e importar o arquivo JSON
    button_importar = tk.Button(janela_importacao, text="Selecionar Arquivo e Importar", command=importar)
    button_importar.pack(pady=20)
