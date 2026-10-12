# Code from my Stack Overflow answer https://stackoverflow.com/a/74579803 (posted 2022-11-26), extracted verbatim; may need the question's context to run.

# --- block 1 ---
tableEl = navegador.find_element(By.XPATH, '//center/table')
tableHtml = tableEl.get_attribute('outerHTML')

lista_completa_MLR=pd.read_html(tableHtml) # ,index_col=('Operadora'), header=(0), thousands='.')
# [I recommend trying without extra arguments first; if it works, try again with all arguments.]

# --- block 2 ---
> tabela = sopa.find(name='table', attrs={'border': ''})
>

# --- block 3 ---
> tabela = sopa.select('table[border=""]')
>
