import tkinter as tk
from views.tela_enxoval import abrir_tela_enxoval
from views.tela_categorias import abrir_tela_categorias
from views.tela_sobre import abrir_tela_sobre
from views.tela_clima import abrir_tela_clima
from views.tela_feriados import abrir_tela_feriados
from views.tela_fornecedores import abrir_tela_fornecedores
from views.tela_exportacao import abrir_tela_exportacao
from views.tela_importacao import abrir_tela_importacao
from views.tela_edicao_cadastro import abrir_tela_edicao_cadastro  
from views.tela_cadastro_bebe import abrir_tela_informacoes_bebe 

def abrir_menu(root, usuario_id, nome_atual):
    menu_janela = tk.Toplevel(root)
    menu_janela.title("Menu Principal")
    menu_janela.geometry("300x600")
    
    tk.Label(menu_janela, text="Bem-vindo ao Menu Principal!").pack()
    tk.Button(menu_janela, text="Informações do Bebê", command=lambda: abrir_tela_informacoes_bebe(usuario_id)).pack()
    tk.Button(menu_janela, text="Acessar Lista de Enxoval", command=lambda: abrir_tela_enxoval(usuario_id)).pack()
    tk.Button(menu_janela, text="Categorias", command=lambda: abrir_tela_categorias(usuario_id)).pack()
    tk.Button(menu_janela, text="Clima e Localização", command=abrir_tela_clima).pack()
    tk.Button(menu_janela, text="Feriados", command=abrir_tela_feriados).pack()
    tk.Button(menu_janela, text="Fornecedores Próximos", command=abrir_tela_fornecedores).pack()
    tk.Button(menu_janela, text="Exportar Lista de Enxoval", command=lambda: abrir_tela_exportacao(usuario_id)).pack()
    tk.Button(menu_janela, text="Importar Lista de Enxoval", command=lambda: abrir_tela_importacao(usuario_id)).pack()
    tk.Button(menu_janela, text="Editar Cadastro Usuário", command=lambda: abrir_tela_edicao_cadastro(usuario_id, nome_atual)).pack() 
    tk.Button(menu_janela, text="Sobre", command=abrir_tela_sobre).pack()
    tk.Button(menu_janela, text="Sair", command=menu_janela.destroy).pack()
