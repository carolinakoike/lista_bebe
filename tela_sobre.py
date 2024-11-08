import tkinter as tk

# Função para abrir a tela "Sobre"
def abrir_tela_sobre():
    janela_sobre = tk.Toplevel()
    janela_sobre.title("Sobre o Projeto")
    janela_sobre.geometry("400x200")

    # Texto informativo sobre o projeto
    texto_sobre = """
    Tema: Lista de Enxoval para Bebê
    Objetivo: Organizar e gerenciar os itens de enxoval necessários para um bebê.
    
    Desenvolvedores:
    - Carolina Koike
    - Daniela Ferreira
    """
    tk.Label(janela_sobre, text=texto_sobre, justify="left").pack()
