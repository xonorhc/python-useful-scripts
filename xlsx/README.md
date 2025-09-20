# xlsx

Scripts para trabalhar com arquivos Excel no formato `.xlsx`.

## O que faz

- Leitura de planilhas Excel
- Escrita em arquivos `.xlsx`, criação de novas planilhas ou modificação de existentes
- Transformações de dados vindos de/para Excel

## Requisitos

- Python 3.x
- Biblioteca para manipulação de Excel, por exemplo `openpyxl`, `pandas`, `xlrd`, `xlsxwriter`, dependendo do que os scripts usam

## Como usar

1. Vá para o diretório:

   `cd xlsx`

2. Instale dependências necessárias:

   ```bash
   pip install openpyxl
   # ou pandas, etc
   ```

3. Ajuste os caminhos dos arquivos Excel nos scripts: entrada, saída, nomes de planilhas, etc.

4. Execute o script:

`python script_xlsx.py`

Exemplos:

- read_excel.py — abre e lê planilha Excel
- write_excel.py — gera uma nova planilha com dados processados
- modify_excel.py — altera células ou estruturas existentes
