import tkinter as tk
from tkinter import messagebox
from services.api_requests import obter_clima

# Defina sua chave de API do OpenWeatherMap aqui
API_KEY_OPENWEATHER = "8c670a616961f5649d5cc34338f1a10d"

# Função para abrir a tela de clima
def abrir_tela_clima():
    janela_clima = tk.Toplevel()
    janela_clima.title("Clima e Localização")
    janela_clima.geometry("400x300")

    tk.Label(janela_clima, text="Digite a cidade para verificar o clima:").pack()
    entry_cidade = tk.Entry(janela_clima)
    entry_cidade.pack()

    # Função para exibir o clima
    def mostrar_clima():
        cidade = entry_cidade.get().strip()
        if not cidade:
            messagebox.showerror("Erro", "Por favor, insira o nome de uma cidade.")
            return

        clima_info = obter_clima(cidade, API_KEY_OPENWEATHER)
        if clima_info:
            resultado = f"Clima em {clima_info['cidade']}, {clima_info['pais']}:\n"
            resultado += f"Temperatura: {clima_info['temperatura']}°C\n"
            resultado += f"Descrição: {clima_info['descricao'].capitalize()}"
            label_resultado.config(text=resultado)
        else:
            messagebox.showerror("Erro", "Não foi possível obter o clima para esta cidade.")

    # Botão e Label para exibir o resultado
    button_clima = tk.Button(janela_clima, text="Ver Clima", command=mostrar_clima)
    button_clima.pack()

    label_resultado = tk.Label(janela_clima, text="", justify="left")
    label_resultado.pack()
