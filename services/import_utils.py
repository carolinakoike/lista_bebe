import json
from services.database import adicionar_item

# Função para importar dados de um arquivo JSON
def importar_enxoval_de_json(caminho_arquivo_json):
    try:
        with open(caminho_arquivo_json, "r") as json_file:
            dados_enxoval = json.load(json_file)
        
        for item in dados_enxoval:
            nome = item.get("nome")
            categoria = item.get("categoria")
            quantidade = item.get("quantidade")
            if nome and quantidade:
                adicionar_item(nome, categoria, quantidade)
        
        return True
    except Exception as e:
        print(f"Erro ao importar dados: {e}")
        return False
