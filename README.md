# Python useful scripts

Repositório contendo vários scripts Python úteis organizados por tema:
**mysql**, **selenium**, **sqlite**, **xlsx**, ...

Cada diretório contém scripts relacionados com aquele domínio específico.

## Estrutura

- `mysql/` — scripts para interagir com bases MySQL
- `selenium/` — automações ou operações de navegador via Selenium
- `sqlite/` — scripts para trabalhar com banco de dados SQLite
- `xlsx/` — scripts para leitura/escrita/manipulação de arquivos Excel (.xlsx)
- ...

## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/xonorhc/python-useful-scripts.git
   cd python-useful-scripts
   ```

2. Instale dependências necessárias (ver cada diretório). Por exemplo, em geral:

   ```bash
   pip install -r requirements.txt
   ```

Se não existir arquivo requirements.txt em algum diretório, instale manualmente
as bibliotecas que os scripts usam (por ex. mysql-connector-python, selenium,
openpyxl, etc.)

3. Vá para o diretório de interesse e execute o(s) script(s) desejados:

   ```bash
   cd selenium
   python nome_do_script.py
   ```

4. Ajuste parâmetros dentro do script conforme necessário: credenciais de
   banco, caminhos de arquivos, configurações do WebDriver, etc.

5. (Opcional) Crie ambientes virtuais para isolar dependências:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   ```

## Contribuições

Se encontrar bugs ou quiser adicionar funcionalidades, fique à vontade para abrir pull requests

Documente novos scripts adicionados: inclua descrição, dependências, instruções de uso
