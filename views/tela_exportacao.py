import tkinter as tk
from tkinter import messagebox
from services.export_utils import exportar_enxoval_para_zip

def abrir_tela_exportacao(usuario_id):
    janela_exportacao = tk.Toplevel()
    janela_exportacao.title("Exportação de Enxoval")
    janela_exportacao.geometry("300x200")

    tk.Label(janela_exportacao, text="Exportar a lista de enxoval").pack(pady=10)

    def exportar():
        try:
            caminho_zip = exportar_enxoval_para_zip(usuario_id)  
            messagebox.showinfo("Exportação", f"Exportação concluída: {caminho_zip}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {e}")

    button_exportar = tk.Button(janela_exportacao, text="Exportar para ZIP", command=exportar)
    button_exportar.pack(pady=20)
