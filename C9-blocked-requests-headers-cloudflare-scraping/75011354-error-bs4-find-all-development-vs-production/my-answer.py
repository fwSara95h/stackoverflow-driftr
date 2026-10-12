# Code from my Stack Overflow answer https://stackoverflow.com/a/75012357 (posted 2023-01-04), extracted verbatim; may need the question's context to run.

# --- block 1 ---
container_indicadores = exampleSoup.select('div.indicator-today-container div[title]')

# --- block 2 ---
exampleFile = requests.get(f'https://statusinvest.com.br/acoes/petr4',headers=headers)
print(exampleFile.status_code, exampleFile.reason, 'from', exampleFile.url)
