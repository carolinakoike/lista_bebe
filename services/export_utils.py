import json
import zipfile
import os
from services.database import obter_itens_enxoval

# Função para exportar itens em JSON e compactá-los em ZIP
def exportar_enxoval_para_zip():
    # Obter itens do banco de dados
    itens = obter_itens_enxoval()
    dados_enxoval = [
        {"id": item[0], "nome": item[1], "categoria": item[2], "quantidade": item[3]}
        for item in itens
    ]
    
    # Criar arquivo JSON
    nome_arquivo_json = "enxoval_bebe.json"
    with open(nome_arquivo_json, "w") as json_file:
        json.dump(dados_enxoval, json_file, indent=4)
    
    # Compactar em arquivo ZIP
    nome_arquivo_zip = "enxoval_bebe.zip"
    with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_file:
        zip_file.write(nome_arquivo_json)
    
    # Remover o arquivo JSON após compactação
    os.remove(nome_arquivo_json)

    return nome_arquivo_zip  # Retorna o caminho do arquivo ZIP
