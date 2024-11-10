import json
from services.database import adicionar_item

def importar_enxoval_de_json(caminho_arquivo, usuario_id):
    try:
        with open(caminho_arquivo, 'r') as file:
            dados = json.load(file)

        for item in dados:
            nome = item.get("nome")
            categoria = item.get("categoria")
            quantidade = item.get("quantidade")

            adicionar_item(nome, categoria, quantidade, usuario_id)
        
        return True
    except Exception as e:
        print(f"Erro ao importar itens: {e}")
        return False
