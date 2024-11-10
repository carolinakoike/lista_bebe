import json
import zipfile
import os
from services.database import obter_itens_enxoval

def exportar_enxoval_para_zip(usuario_id):
    itens = obter_itens_enxoval(usuario_id)  
    dados_enxoval = [
        {"id": item[0], "nome": item[1], "categoria": item[2], "quantidade": item[3]}
        for item in itens
    ]
    
    nome_arquivo_json = "enxoval_bebe.json"
    with open(nome_arquivo_json, "w") as json_file:
        json.dump(dados_enxoval, json_file, indent=4)

    nome_arquivo_zip = "enxoval_bebe.zip"
    with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_file:
        zip_file.write(nome_arquivo_json)

    os.remove(nome_arquivo_json)

    return nome_arquivo_zip 
