---
title: "How to split find() result in Beautifulsoup?"
site: stackoverflow
question_id: 75024482
answer_id: 75028807
url: https://stackoverflow.com/a/75028807
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-06T08:56:46Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75028807/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 569c6de3aa19de9267c2d7d9ed73d24815385ac0792dbfddd4ba7581906cebd0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75028807>, 2023-01-06; **accepted**; score 0. Text as retrieved 2026-10-12.

> I want to create a list with the name of the documents ("Despacho Homologatório", "DOU Resultado de Julgamento" etc) in panel "Arquivos de Licitação".

You can use [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) with `.find...` to get the `a` tags and filter out container tags (like the first one), or [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php).

---

**With List Comprehension**

```python
link_panel = soup.find("ul", {"class": "links"})
links = [l.a for l in link_panel.find_all('li') if l.a and not l.a.li]
```

---

**With `.select`**

```python
# link_panel is no longer necessary
links = soup.select('ul.links li>a:not(:has(li))')
```

the `find` equivalent would be

```python
links = soup.find_all(
    lambda l: l.name == 'a' and l.parent.name == 'li' 
    and l.find_parent("ul", {"class": "links"}) and not l.find('li')
)
```

so you might see why I much prefer using CSS selectors.

---

You can **get the names** with [`.get_text`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text)

```python
docNames = [l.get_text() for l in links]
```

and `docNames` would look something like

> ```python 
> ['Despacho Homologatório',  'DOU Resultado de Julgamento', 'Termo de Ajudicação',  
>  'Ata da sessão publica',  'Proposta de preço adequada CSR',  
>  'Documentos de Habilitação CSR',  'Análise da proposta e Doc. de habilitação',  
>  'Resposta a 1ª diligencia - CSR',  '1ª Diligência - CSR',  '1ª Errata',  
>  'Anexo da 1ª Errata',  'Instrução para acesso ao processo administrativo',  
>  'Edital 0286/2022-15',  'DOU aviso de licitação'] 
> ```

---

or you could get the links with the names as a list of dictionaries:

```python
# pgUrl = "https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109"
linkDocs = [{
    'name':l.get_text(' ').strip(), 'filename':l.get('href','').split('/')[-1],
    'link':urllib.parse.urljoin(pgUrl, l.get('href')) if l.get('href') else ''
} for l in soup.select('ul.links li>a:not(:has(li))')]# links]
```

and `linkDocs` looks something like

> ```python
> [{'name': 'Despacho Homologatório', 'filename': 'outros_edital0286_22-15_10.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_10.pdf'},
>  {'name': 'DOU Resultado de Julgamento', 'filename': 'outros_edital0286_22-15_9.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_9.pdf'},
>  {'name': 'Termo de Ajudicação', 'filename': 'outros_edital0286_22-15_8.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_8.pdf'},
>  {'name': 'Ata da sessão publica', 'filename': 'Ata_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/Ata/Ata_edital0286_22-15_0.pdf'},
>  {'name': 'Proposta de preço adequada CSR', 'filename': 'outros_edital0286_22-15_7.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_7.zip'},
>  {'name': 'Documentos de Habilitação CSR', 'filename': 'outros_edital0286_22-15_6.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_6.zip'},
>  {'name': 'Análise da proposta e Doc. de habilitação', 'filename': 'outros_edital0286_22-15_5.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_5.pdf'},
>  {'name': 'Resposta a 1ª diligencia - CSR', 'filename': 'outros_edital0286_22-15_4.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_4.zip'},
>  {'name': '1ª Diligência - CSR', 'filename': 'outros_edital0286_22-15_3.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_3.pdf'},
>  {'name': '1ª Errata', 'filename': 'Errata_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/Errata/Errata_edital0286_22-15_0.pdf'},
>  {'name': 'Anexo da 1ª Errata', 'filename': 'outros_edital0286_22-15_2.zip', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_2.zip'},
>  {'name': 'Instrução para acesso ao processo administrativo', 'filename': 'outros_edital0286_22-15_1.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_1.pdf'},
>  {'name': 'Edital 0286/2022-15', 'filename': 'Edital_edital0286_22-15_0.zip', 'link': 'https://www1.dnit.gov.br/anexo/Edital/Edital_edital0286_22-15_0.zip'},
>  {'name': 'DOU aviso de licitação', 'filename': 'outros_edital0286_22-15_0.pdf', 'link': 'https://www1.dnit.gov.br/anexo/outros/outros_edital0286_22-15_0.pdf'}]
> ```

---

Btw, about 
> ```python 
> page = urlopen("https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109")
> html = page.read().decode("utf-8") 
> soup = BeautifulSoup(html, "lxml")
> ```

You don't really *need* the `html` variable here - just getting `soup = BeautifulSoup(page, "lxml")` directly should be fine too, since `BeautifulSoup` accepts open filehandles and such.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[GovAuditor](https://stackoverflow.com/users/19510974)** (2023-01-06): Thanks for the complete answer and the tip at the end.
