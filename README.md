# Aplicativo de Lista de Enxoval para Bebê

Este projeto é uma aplicação desenvolvida em Python com interface gráfica feita em Tkinter, desenvolvida para organizar e gerenciar os itens de enxoval de um bebê. O sistema permite que os usuários gerenciem sua lista de enxoval, obtenham informações sobre clima e feriados, e localizem fornecedores próximos.

## Tema e Objetivo

**Tema**: Lista de Enxoval para Bebê
**Objetivo**: Organizar e gerenciar os itens necessários para o enxoval de um bebê. O sistema permite que os usuários insiram dados do bebê e consultem informações sobre o clima e feriados para planejar as compras e a organização do enxoval. Os itens podem ser exportados para um arquivo ZIP e importados posteriormente.


## Funcionalidades

**Cadastro e Login**: Interface para registro e autenticação de usuários.
**Gerenciamento de Enxoval**: Adicionar, visualizar, atualizar e remover itens do enxoval, com armazenamento persistente em banco de dados.
**Exportação e Importação de Dados**: Exporta a lista de itens para um arquivo JSON compactado em ZIP. É possível importar dados tanto de arquivos locais JSON quanto de URLs.
**Localização de Fornecedores**: Exibe fornecedores próximos com base na localização informada, para facilitar a aquisição de itens do enxoval.
**Informações de Clima**: Mostra a previsão do tempo para auxiliar no planejamento do enxoval e dos passeios do bebê.
**Lembretes de Feriados**: Informa sobre feriados importantes, para melhor planejamento das compras e organização.


### Tecnologias Utilizadas

-**Python 3.12**
-**Tkinter**: Utilizado para a construção da interface gráfica.
-**SQLite**: Banco de dados local para armazenamento dos dados dos usuários, itens do enxoval e informações do bebê.
-**Foursquare Places API**: Para busca e exibição de fornecedores locais.
-**OpenWeatherMap API**: Fornece informações climáticas com base na localização.
-**Calendarific API**: Exibe feriados de acordo com o país e o ano selecionados.


### Pré-requisitos
Python 3.12 instalado.
Instalação dos pacotes necessários listados no requirements.txt.
Instalação dos Pacotes
No diretório do projeto, instale os pacotes necessários com o comando:

```bash
pip install -r requirements.txt
