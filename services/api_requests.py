import requests

# Função para obter informações de clima usando a API OpenWeatherMap
def obter_clima(cidade, chave_api):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt&units=metric"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        clima = {
            "temperatura": dados["main"]["temp"],
            "descricao": dados["weather"][0]["description"],
            "cidade": dados["name"],
            "pais": dados["sys"]["country"]
        }
        return clima
    else:
        return None

# Função para obter informações de localização básica (exemplo de consulta de cidade)
def obter_cidade(cidade, chave_api_geodb):
    url = f"http://geodb-free-service.wirefreethought.com/v1/geo/cities?namePrefix={cidade}"
    headers = {"x-rapidapi-key": chave_api_geodb}
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        dados = resposta.json()
        if dados["data"]:
            cidade_info = {
                "nome": dados["data"][0]["city"],
                "pais": dados["data"][0]["country"]
            }
            return cidade_info
    return None

# Função para obter feriados usando a API Calendarific
def obter_feriados(pais, ano, chave_api_feriados):
    url = f"https://calendarific.com/api/v2/holidays?api_key={chave_api_feriados}&country={pais}&year={ano}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        feriados = [
            {
                "nome": feriado["name"],
                "data": feriado["date"]["iso"],
                "tipo": feriado["type"]
            }
            for feriado in dados["response"]["holidays"]
        ]
        return feriados
    else:
        print(f"Erro: {resposta.status_code}, {resposta.json()}")
        return None

# Função para obter fornecedores próximos usando a Foursquare Places API
def obter_fornecedores_proximos(cidade, tipo_estabelecimento, chave_api_foursquare):
    # URL para buscar locais com base em uma cidade e tipo
    url = f"https://api.foursquare.com/v3/places/search?query={tipo_estabelecimento}&near={cidade}&limit=10"
    headers = {
        "Authorization": chave_api_foursquare,
    }
    resposta = requests.get(url, headers=headers)
    if resposta.status_code == 200:
        dados = resposta.json()
        fornecedores = [
            {
                "nome": lugar["name"],
                "endereco": lugar.get("location", {}).get("formatted_address", "Endereço não disponível")
            }
            for lugar in dados.get("results", [])
        ]
        return fornecedores
    else:
        print(f"Erro: {resposta.status_code}, {resposta.json()}")
        return None
