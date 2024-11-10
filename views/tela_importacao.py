import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import json
from services.database import adicionar_item  

def abrir_tela_importacao(usuario_id):
    janela_importacao = tk.Toplevel()
    janela_importacao.title("Importação de Itens de Enxoval")
    janela_importacao.geometry("400x300")

    tk.Label(janela_importacao, text="Importar lista de enxoval").pack(pady=10)

    tk.Label(janela_importacao, text="1. Selecionar um arquivo JSON do computador:").pack()
    button_arquivo = tk.Button(janela_importacao, text="Selecionar Arquivo", command=lambda: importar_de_arquivo(usuario_id))
    button_arquivo.pack(pady=5)

    tk.Label(janela_importacao, text="2. Ou inserir o URL do arquivo JSON: ").pack()
    tk.Label(janela_importacao, text="Exemplo: https://raw.githubusercontent.com/carolinakoike/lista_bebe/refs/heads/main/export/exemplo_1.json").pack()
    entry_url = tk.Entry(janela_importacao, width=50)
    entry_url.pack(pady=5)
    button_url = tk.Button(janela_importacao, text="Importar do URL", command=lambda: importar_de_url(entry_url.get().strip(), usuario_id))
    button_url.pack(pady=5)

    def importar_de_arquivo(usuario_id):
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
        if caminho_arquivo:
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                    dados_json = json.load(arquivo)
                    processar_dados(dados_json, usuario_id)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao importar o arquivo: {e}")

    def importar_de_url(url, usuario_id):
        if not url:
            messagebox.showerror("Erro", "Por favor, insira um URL.")
            return

        try:
            response = requests.get(url)
            response.raise_for_status()  
            dados_json = response.json()
            processar_dados(dados_json, usuario_id)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Erro ao buscar dados do URL: {e}")
        except ValueError:
            messagebox.showerror("Erro", "Erro ao processar o JSON. Verifique o formato do arquivo.")

    def processar_dados(dados_json, usuario_id):
        try:
            for item in dados_json:
                nome_item = item.get("nome")
                categoria_item = item.get("categoria")
                quantidade_item = item.get("quantidade")
                if nome_item and categoria_item and isinstance(quantidade_item, int):
                    adicionar_item(nome_item, categoria_item, quantidade_item, usuario_id)
            messagebox.showinfo("Importação Concluída", "Itens importados com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar itens ao banco: {e}")
