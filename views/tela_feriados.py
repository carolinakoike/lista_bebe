import tkinter as tk
from tkinter import messagebox
from services.api_requests import obter_feriados

API_KEY_FERIADOS = "RBQoX99PA9jeiqKUba09TYQmIEksOIc1"

def abrir_tela_feriados():
    janela_feriados = tk.Toplevel()
    janela_feriados.title("Lembretes de Feriados")
    janela_feriados.geometry("400x400")

    tk.Label(janela_feriados, text="Informe o ano:").pack()
    entry_ano = tk.Entry(janela_feriados)
    entry_ano.pack()

    tk.Label(janela_feriados, text="Informe o código do país (ex: BR para Brasil):").pack()
    entry_pais = tk.Entry(janela_feriados)
    entry_pais.pack()

    frame_lista = tk.Frame(janela_feriados)
    frame_lista.pack(fill="both", expand=True)

    lista_feriados = tk.Listbox(frame_lista, width=50, height=15)
    scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=lista_feriados.yview)
    lista_feriados.config(yscrollcommand=scrollbar.set)

    lista_feriados.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    def mostrar_feriados():
        ano = entry_ano.get().strip()
        pais = entry_pais.get().strip().upper()
        if not ano.isdigit() or not pais:
            messagebox.showerror("Erro", "Por favor, insira o ano e o código do país corretamente.")
            return

        feriados = obter_feriados(pais, ano, API_KEY_FERIADOS)
        if feriados:
            lista_feriados.delete(0, tk.END)
            for feriado in feriados:
                lista_feriados.insert(tk.END, f"{feriado['data']} - {feriado['nome']} ({', '.join(feriado['tipo'])})")
        else:
            messagebox.showerror("Erro", "Não foi possível obter os feriados para este país e ano.")

    button_feriados = tk.Button(janela_feriados, text="Ver Feriados", command=mostrar_feriados)
    button_feriados.pack()
