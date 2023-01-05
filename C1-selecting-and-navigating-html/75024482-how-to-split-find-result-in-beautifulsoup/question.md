---
title: "How to split find() result in Beautifulsoup?"
site: stackoverflow
question_id: 75024482
url: https://stackoverflow.com/q/75024482
asked: 2023-01-05T21:21:15Z
asked_by: "GovAuditor"
asked_by_url: https://stackoverflow.com/users/19510974
last_edited: 2023-01-05T21:25:05Z
tags: [python, web-scraping, beautifulsoup]
score: 1
views_at_snapshot: 63
answer_count: 1
accepted_answer_id: 75028807
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e8628032bceb885ecd5dc4c2118a983f3cfec8323c83208a43a38890884d5820
---

# How to split find() result in Beautifulsoup?

Asked by [GovAuditor](https://stackoverflow.com/users/19510974) on Stack Overflow, <https://stackoverflow.com/q/75024482>, 2023-01-05, last edited 2023-01-05. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm a complete beginner in Python (also in programming) and I'm trying to scrape some data from this site (https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109).

I want to create a list with the name of the documents ("Despacho Homologatório", "DOU Resultado de Julgamento" etc) in panel "Arquivos de Licitação". The code I'm using:

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
page = urlopen("https://www1.dnit.gov.br/editais/consulta/resumo.asp?NUMIDEdital=9109")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "lxml")
link_panel = soup.find("ul", {"class": "links"})
links = link_panel.find_all('li')
```

However, each of the items in the resultset object have several tags together (the text below is just part of the item[0]):

```python
print(links[0])
<li><a href="/anexo/outros/outros_edital0420_22-12_4.pdf" target="_blank"><li><a href="/anexo/outros/outros_edital0420_22-12_4.pdf" target="_blank">Publicação D.O.U. - Resultado de Julgamento PE nº 0420/2022-12</a></li>
<!--  <font color="#FF0000" size="1">(17/11/2022)</font> </font> </td>-->
<li><a href="/anexo/outros/Homologação_edital0420_22-12_0.pdf" target="_blank"><li><a href="/anexo/outros/Homologação_edital0420_22-12_0.pdf" target="_blank">Termo de Homologação - Pregão Eletrônico nº 0420/2022-12</a></li>
<!--  <font color="#FF0000" size="1">(16/11/2022)</font> </font> </td>-->
<li><a href="/anexo/outros/outros_edital0420_22-12_3.pdf" target="_blank"><li><a href="/anexo/outros/outros_edital0420_22-12_3.pdf" target="_blank">Termo de Adjudicação - Pregão Eletrônico nº 0420/2022-12</a></li>
<!--  <font color="#FF0000" size="1">(11/11/2022)</font> </font> </td>-->
<li><a href="/anexo/Ata/Ata_edital0420_22-12_2.pdf" target="_blank"><li><a href="/anexo/Ata/Ata_edital0420_22-12_2.pdf" target="_blank">Ata de Realização do Pregão Eletrônico nº 0420/2022-12</a></li>
<!--  <font color="#FF0000" size="1">(11/11/2022)</font> </font> </td>-->
<li><a href="/anexo/Ata/Ata_edital0420_22-12_0.pdf" target="_blank"><li><a href="/anexo/Ata/Ata_edital0420_22-12_0.pdf" target="_blank">Ata de Realização do Pregão Eletrônico nº 0420/2022-12</a></li>
<!--  <font color="#FF0000" size="1">(11/11/2022)</font> </font> </td>-->
<li><a href="/anexo/Relatório/Relatório_edital0420_22-12_0.pdf" target="_blank"><li><a href="/anexo/Relatório/Relatório_edital0420_22-12_0.pdf" target="_blank">Relatório de Análise da Proposta de Preços e Doc. de Habilitação (Pregoeira) - ETHOS ENGENHARIA</a></li>
```

How can I use find_all() to find separately each document?


Besides using the code above, I've tried to use find_all() in the first result (valores_links[0]), to no avail.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[nicomp](https://stackoverflow.com/users/1169091)** (2023-01-05): We can't reproduce your issue with the code you've provided.
- **[Shmack](https://stackoverflow.com/users/3155240)** (2023-01-05): You have all the links. I would just iterate over them and `get_text()`. -> `[e.get_text() for e in links]`
