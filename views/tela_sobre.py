import tkinter as tk

def abrir_tela_sobre():
    janela_sobre = tk.Toplevel()
    janela_sobre.title("Sobre o Projeto")
    janela_sobre.geometry("400x200")

    texto_sobre = """
    Tema: Lista de Enxoval para Bebê
    Objetivo: Organizar e gerenciar os itens de enxoval 
    necessários para um bebê.
    Além disso, o sistema permite que os usuários insiram 
    a localização do bebê e consultem informações sobre o 
    clima e feriados.
    Os itens podem ser exportados para um arquivo ZIP e 
    importados posteriormente.
        
    Desenvolvedoras:
    - Carolina Koike, RA: 2840482221014
    - Daniela Ferreira, RA: 2840482221009
    """
    tk.Label(janela_sobre, text=texto_sobre, justify="left").pack()
