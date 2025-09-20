# Selenium

Scripts de automação de navegador utilizando Selenium.

## O que faz

- Automatização de workflows web (login, navegação, interações com formulários, scraping, etc.)
- Exemplos de utilização de WebDriver, waits, locators, etc.

## Requisitos

- Python 3.x
- Selenium instalado:

  `pip install selenium`

- WebDriver apropriado para o navegador usado (ex: ChromeDriver, geckodriver), compatível com a versão do navegador instalado

## Como usar

1. Navegue até o diretório:

   `cd selenium`

2. Ajuste no(s) script(s):
   - Caminho para o WebDriver, se necessário
   - URLs alvo, credenciais e seletores que o script usa
   - Outras configurações como headless ou não, tempo de espera, etc.

3. Execute o script desejado:

   `python script_selenium.py`

Exemplos

- login_example.py — script para login em site X
- scrape_data.py — coleta dados de uma página web
