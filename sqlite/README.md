# SQLite

Scripts que utilizam banco de dados SQLite.

## O que faz

- Cria / altera bancos de dados SQLite
- Executa queries de leitura e escrita
- Manipulação de dados locais sem necessidade de servidor externo

## Requisitos

- Python 3.x
- Biblioteca `sqlite3` (já incluída na biblioteca padrão do Python)

## Como usar

1. Entre no diretório:

   `cd sqlite`

2. Se houver algum script que exija dependências adicionais, instale-as.

3. Edite os scripts para definir o caminho para o arquivo .sqlite ou .db, tabelas, etc.

4. Execute o script desejado:

   `python script_sqlite.py`

Exemplos:

- create_db.py — cria um novo banco SQLite
- query_db.py — faz consultas e imprime resultados
