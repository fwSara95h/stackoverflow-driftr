---
title: "Why can't Selenium find the table in this website?"
site: stackoverflow
question_id: 74576756
url: https://stackoverflow.com/q/74576756
asked: 2022-11-25T18:32:46Z
asked_by: "VitSD"
asked_by_url: https://stackoverflow.com/users/20600875
last_edited: 2022-11-28T09:39:39Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [html, python-3.x, pandas, selenium-webdriver, beautifulsoup]
score: 0
views_at_snapshot: 83
answer_count: 1
accepted_answer_id: 74579803
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fdc52304d59a99d0bb33b713bf190cffd521a0e4e9f70807f738b1beb0262981
---

# Why can't Selenium find the table in this website?

Asked by [VitSD](https://stackoverflow.com/users/20600875) on Stack Overflow, <https://stackoverflow.com/q/74576756>, 2022-11-25, last edited 2022-11-28 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm trying to scrape a table that appears in a new website when you fulfill a form, but it raises a ValueError: No tables found. You can see the code details below:


```python
ANS_TabNetMLR_URL = navegador.get("http://www.ans.gov.br/anstabnet/cgi-bin/dh?dados/tabnet_rc.def")
selecionarLinha = Select(navegador.find_element(By.XPATH, '//*[@id="L"]'))
selecionarLinhaOperadora = selecionarLinha.select_by_visible_text('Operadora')

selecionarColuna = Select(navegador.find_element(By.XPATH, '//*[@id="C"]'))
selecionarColunaModalidade = selecionarColuna.select_by_visible_text('Grupo Modalidade')

selecionarConteudo = Select(navegador.find_element(By.XPATH, '//*[@id="I"]'))
selecionarConteudo.deselect_by_visible_text('Receita de contraprestações')
selecionarConteudoMLR = selecionarConteudo.select_by_visible_text('Despesa assistencial')

selecionarMostra = navegador.find_element(By.XPATH, '//*[@id="geral"]/thead/tr[2]/td[2]/center/form/table[2]/tbody/tr[4]/td/p[2]/input[1]').click()

novaURL = 'http://www.ans.gov.br/anstabnet/cgi-bin/tabnet?dados/tabnet_rc.def'
aguardar = WebDriverWait(navegador, 10).until(ec.url_to_be(novaURL))

encontrarTabela = navegador.find_element(By.XPATH, '//*[@id="geral"]/thead/tr[2]/td[2]/center/table/tbody')

HTML_tabela_MLR = encontrarTabela.get_attribute('outerHTML')
sopa = BeautifulSoup(HTML_tabela_MLR, 'html.parser')

tabela = sopa.find(name = 'table border')
df_completo_MLR = pd.DataFrame()

lista_completa_MLR=pd.read_html(str(tabela),index_col=('Operadora'), header=(0), thousands='.')
```
And so the console output:


```lang-none
Traceback (most recent call last):

  File "C:\Users\vitor.dias\Documents\ANSMLR.py", line 206, in <module>
    lista_completa_MLR=pd.read_html(str(tabela),index_col=('Operadora'), header=(0), thousands='.')

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\io\html.py", line 1113, in read_html
    return _parse(

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\io\html.py", line 939, in _parse
    raise retained

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\io\html.py", line 919, in _parse
    tables = p.parse_tables()

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\io\html.py", line 239, in parse_tables
    tables = self._parse_tables(self._build_doc(), self.match, self.attrs)

  File "C:\Users\vitor.dias\Anaconda3\lib\site-packages\pandas\io\html.py", line 569, in _parse_tables
    raise ValueError("No tables found")

ValueError: No tables found
```

I'm grateful since now for any help and I'm sorry if it's too dumb LOL I'm just starting on the Stackoverflow and using Selenium.

I've tried to scrape a table through its HTML to transform it on dataframe in Pandas, but then it couldn't find the table, even that I could see it doing this process manually.
