import tkinter as tk
from tela_enxoval import abrir_tela_enxoval
from tela_categorias import abrir_tela_categorias
from tela_sobre import abrir_tela_sobre
from tela_clima import abrir_tela_clima
from tela_feriados import abrir_tela_feriados
from tela_fornecedores import abrir_tela_fornecedores
from tela_exportacao import abrir_tela_exportacao
from tela_importacao import abrir_tela_importacao

def abrir_menu(root):
    menu_janela = tk.Toplevel(root)
    menu_janela.title("Menu Principal")
    menu_janela.geometry("300x550")
    
    tk.Label(menu_janela, text="Bem-vindo ao Menu Principal!").pack()
    tk.Button(menu_janela, text="Acessar Lista de Enxoval", command=abrir_tela_enxoval).pack()
    tk.Button(menu_janela, text="Categorias", command=abrir_tela_categorias).pack()
    tk.Button(menu_janela, text="Sobre", command=abrir_tela_sobre).pack()
    tk.Button(menu_janela, text="Clima e Localização", command=abrir_tela_clima).pack()
    tk.Button(menu_janela, text="Lembretes de Feriados", command=abrir_tela_feriados).pack()
    tk.Button(menu_janela, text="Fornecedores Próximos", command=abrir_tela_fornecedores).pack()
    tk.Button(menu_janela, text="Exportar Lista de Enxoval", command=abrir_tela_exportacao).pack()
    tk.Button(menu_janela, text="Importar Lista de Enxoval", command=abrir_tela_importacao).pack()
    tk.Button(menu_janela, text="Sair", command=menu_janela.destroy).pack()
