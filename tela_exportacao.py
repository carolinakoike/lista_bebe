import tkinter as tk
from tkinter import messagebox
from services.export_utils import exportar_enxoval_para_zip

# Função para abrir a tela de exportação
def abrir_tela_exportacao():
    janela_exportacao = tk.Toplevel()
    janela_exportacao.title("Exportação de Enxoval")
    janela_exportacao.geometry("300x200")

    tk.Label(janela_exportacao, text="Exportar a lista de enxoval").pack(pady=10)

    # Função para realizar a exportação
    def exportar():
        caminho_zip = exportar_enxoval_para_zip()
        if caminho_zip:
            messagebox.showinfo("Exportação Concluída", f"Arquivo exportado com sucesso: {caminho_zip}")
        else:
            messagebox.showerror("Erro", "Erro ao exportar o arquivo.")

    # Botão para exportar o arquivo ZIP
    button_exportar = tk.Button(janela_exportacao, text="Exportar para ZIP", command=exportar)
    button_exportar.pack(pady=20)
