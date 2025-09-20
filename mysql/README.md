# MySQL

Este diretório contém scripts para trabalhar com bancos de dados MySQL.

## O que faz

- Conectar a um servidor MySQL
- Executar queries de leitura e escrita
- Criar / modificar tabelas ou bancos
- Outras operações utilitárias envolvendo MySQL (backup, etc.), conforme os scripts existentes

## Requisitos

- Python 3.x
- Biblioteca para MySQL (por exemplo `mysql-connector-python` ou `pymysql`)
- Acesso a um servidor/banco MySQL, com credenciais válidas

## Como usar

1. Navegue até este diretório:

   `cd mysql`

2. Instale a(s) dependência(s):

   ```bash
   pip install mysql-connector-python
   # ou
   pip install pymysql
   ```

3. Edite os scripts para configurar host, usuário, senha, nome do banco, porta, etc.

4. Rode o script desejado:

   `python meu_script_mysql.py`

5. Verifique os resultados/saídas conforme esperado.

Exemplos:

- connect.py — script que demonstra como conectar e executar uma query simples
- backup.py — script para fazer backup de tabelas ou bancos
