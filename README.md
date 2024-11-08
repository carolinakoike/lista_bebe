# Aplicativo de Lista de Enxoval para Bebê

Este projeto é uma aplicação desenvolvida em Python com Tkinter para gerenciar uma lista de itens de enxoval para bebês. O aplicativo permite ao usuário adicionar, visualizar, exportar e importar itens para o enxoval, além de acessar funcionalidades adicionais como previsão do tempo e localização de fornecedores próximos.

## Funcionalidades

- **Cadastro e Login**: Tela para cadastro de novos usuários e autenticação.
- **Gerenciamento de Enxoval**: Adicionar, visualizar, atualizar e remover itens do enxoval.
- **Exportação e Importação de Dados**: Exporta a lista de itens para um arquivo JSON compactado em ZIP e importa dados a partir de um arquivo JSON.
- **Localização de Fornecedores**: Exibe fornecedores próximos com base na localização informada.
- **Informações de Clima**: Mostra a previsão do tempo para auxiliar no planejamento.
- **Lembretes de Feriados**: Informa sobre feriados importantes.

## Tecnologias Utilizadas

- **Python 3.12**
- **Tkinter**: Para construção da interface gráfica.
- **SQLite**: Banco de dados local para armazenar dados dos itens e dos usuários.
- **Foursquare Places API**: Para busca de fornecedores locais.
- **OpenWeatherMap API**: Para exibir informações climáticas.

## Pré-requisitos

1. **Python 3.12** instalado.
2. **Instalar pacotes necessários** listados em `requirements.txt`.

### Instalação dos Pacotes

No diretório do projeto, instale os pacotes com o comando:

```bash
pip install -r requirements.txt
