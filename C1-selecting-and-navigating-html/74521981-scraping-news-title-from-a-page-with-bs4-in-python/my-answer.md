---
title: "Scraping news title from a page with bs4 in python"
site: stackoverflow
question_id: 74521981
answer_id: 74522447
url: https://stackoverflow.com/a/74522447
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-21T17:01:43Z
last_edited: 2022-11-24T09:47:00Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74522447/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ab6f05b3bf81d7193e7a3959d4db604c8fdc225cb954ab93f55bfad7e994f92c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74522447>, 2022-11-21, last edited 2022-11-24; **accepted**; score 0. Text as retrieved 2026-10-12.

The `entry-title` class is not of the link `a` tag, but of the `h2` wrapped around it.
You can use 
```python
names = [h.a for h in soup.find_all('h2', class_='entry-title')]
```
But I think using [CSS selectors](https://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors) would be better here
```python
names = soup.select('h2.entry-title > a[href]')
```
will select any `a` tag with a `href` attribute and with a `h2` parent of class `entry-title`.

---

Then, 
```python
for a in names: print(a.get_text().strip(), a.get('href'))
```
will print
```lang-none
AVVISO LEZIONI DI SCULTURA : PROF.BORRELLI https://www.abafg.it/avviso-lezioni-di-scultura-prof-borrelli/
ORARIO DELLE LEZIONI A.A.2022/2023 IN VIGORE DAL 21 NOVEMBRE 2022 https://www.abafg.it/orario-delle-lezioni-a-a-2022-2023-in-vigore-dal-21-novembre-2022/
PROROGA BANDO AFFIDAMENTI INTERNI D.D. N. 3 DEL 4.11.2022 https://www.abafg.it/proroga-bando-affidamenti-interni-d-d-n-3-del-4-11-2022/
D.D. n.  7 del 15.11.2022 DECRETO GRADUATORIA PROVVISORIA ABPR19 https://www.abafg.it/d-d-n-7-del-15-11-2022-decreto-graduatoria-provvisoria-abpr19/
D.D. n. 5 DEL 10.11.2022 DECRETO DI NOMINA COMMISSIONE ABPR19 https://www.abafg.it/d-d-n-5-del-10-11-2022-decreto-di-nomina-commissione-abpr19/
RIAPERTURA BANDO AFFIDAMENTI INTERNI D.D. N. 3 DEL 4.11.2022 https://www.abafg.it/riapertura-bando-affidamenti-interni-d-d-n-4-del-4-11-2022/
D.D.81 del 26.10.2022 GRADUATORIA DEFINITIVA ABST48 STORIA DELLE ARTI APPLICATE https://www.abafg.it/d-d-81-del-26-10-2022-graduatoria-definitiva-abst48-storia-delle-arti-applicate/
AVVISO PRESENTAZIONE DOMANDE CULTORE DELLA MATERIA A.A.22.23-SCADENZA 11.11.2022 https://www.abafg.it/avviso-presentazione-domande-cultore-della-materia-a-a-22-23-scadenza-11-11-2022/
D.D. N.78 DEL 19/10/2022 BANDO GRADUATORIE D’ISTITUTO-SCADENZA 9/11/2022. https://www.abafg.it/d-d-n-78-bando-graduatorie-distituto-scadenza-9-11-2022/
ORARIO PROVVISIORIO DELLE LEZIONI A.A. 2022/2023: TRIENNIO E BIENNIO https://www.abafg.it/orario-provvisiorio-delle-lezioni-a-a-2022-2023-triennio-e-biennio/
```

---
---

**Added EDIT:** to save the printed text into a file, you could first save it as one string with [`.join`](https://www.programiz.com/python-programming/methods/string/join) first
```python
asText = '\n'.join([f'{a.get_text().strip()} {a.get("href")}' for a in names])
```
and then you could save it with
```python
with open('./resources/titles.txt', 'w', encoding='utf-8') as f: 
    f.write(asText)
```

---


If you want something more visuals-friendly, I suggest using [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
```python
asDF = pandas.DataFrame([{
    'title': a.get_text().strip(), 'link': a.get('href')
} for a in names])
asText = asDF.to_markdown(index=False)
```
and now `asText` looks like
```lang-none
| title                                                                            | link                                                                                                   |
|:---------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| ORARIO DELLE LEZIONI A.A.2022/2023 IN VIGORE DAL 21 NOVEMBRE 2022                | https://www.abafg.it/orario-delle-lezioni-a-a-2022-2023-in-vigore-dal-21-novembre-2022/                |
| PROROGA BANDO AFFIDAMENTI INTERNI D.D. N. 3 DEL 4.11.2022                        | https://www.abafg.it/proroga-bando-affidamenti-interni-d-d-n-3-del-4-11-2022/                          |
| D.D. n.  7 del 15.11.2022 DECRETO GRADUATORIA PROVVISORIA ABPR19                 | https://www.abafg.it/d-d-n-7-del-15-11-2022-decreto-graduatoria-provvisoria-abpr19/                    |
| D.D. n. 5 DEL 10.11.2022 DECRETO DI NOMINA COMMISSIONE ABPR19                    | https://www.abafg.it/d-d-n-5-del-10-11-2022-decreto-di-nomina-commissione-abpr19/                      |
| RIAPERTURA BANDO AFFIDAMENTI INTERNI D.D. N. 3 DEL 4.11.2022                     | https://www.abafg.it/riapertura-bando-affidamenti-interni-d-d-n-4-del-4-11-2022/                       |
| D.D.81 del 26.10.2022 GRADUATORIA DEFINITIVA ABST48 STORIA DELLE ARTI APPLICATE  | https://www.abafg.it/d-d-81-del-26-10-2022-graduatoria-definitiva-abst48-storia-delle-arti-applicate/  |
| AVVISO PRESENTAZIONE DOMANDE CULTORE DELLA MATERIA A.A.22.23-SCADENZA 11.11.2022 | https://www.abafg.it/avviso-presentazione-domande-cultore-della-materia-a-a-22-23-scadenza-11-11-2022/ |
| D.D. N.78 DEL 19/10/2022 BANDO GRADUATORIE D’ISTITUTO-SCADENZA 9/11/2022.        | https://www.abafg.it/d-d-n-78-bando-graduatorie-distituto-scadenza-9-11-2022/                          |
| ORARIO PROVVISIORIO DELLE LEZIONI A.A. 2022/2023: TRIENNIO E BIENNIO             | https://www.abafg.it/orario-provvisiorio-delle-lezioni-a-a-2022-2023-triennio-e-biennio/               |
| GRADUATORIA DEFINITIVA  ABST47 STILE,STORIA DELL’ARTE E DEL COSTUME              | https://www.abafg.it/graduatoria-definitiva-abst47-stilestoria-dellarte-e-del-costume/                 |
```

And then, instead of TXT, you could also save it as CSV with
```python
asDF.to_csv('./resources/titles.csv', index=False)
```
so that you can view it as a spreadsheet
[![csv][1]][1]


  [1]: https://i.sstatic.net/ow7op.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Vito Esposito](https://stackoverflow.com/users/20564783)** (2022-11-22): https://i.imgur.com/XiXzcVn.png  Thank you so much for your dedication, but it actually wont print me anything out
- **me** (2022-11-23): @VitoEsposito weird. It worked for me... you should check `page` then to check if you're getting the right response with the right html. Please add the lines `print(page.status_code, page.reason)` [it should print "200 OK" or some kind of error status] and `with open('x.html', 'wb') as f: f.write(page.content)` [to save the fetched html]. Then, open "x.html" [*in an editor,  **not** a browser*] and search [using `CTRL`+`F` or some equivalent] for "entry-title". Please let me know what you find
- **[Vito Esposito](https://stackoverflow.com/users/20564783)** (2022-11-23): https://i.imgur.com/DqHPdeI.png That's the result
- **me** (2022-11-24): @VitoEsposito As you can see, you're getting [403 Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/403#:~:text=The%20HTTP%20403%20Forbidden%20response,but%20refuses%20to%20authorize%20it.) - i.e., the site is blocking your request so you're not getting the right html.
- **me** (2022-11-24): @VitoEsposito To solve the issue, you can try to [set the right headers](https://www.scrapehero.com/how-to-fake-and-rotate-user-agents-using-python-3/#therightwaytorotateuseragentsinanyprogram), but tbh I'm not very good at that so I just use [cloudscraper](https://pypi.org/project/cloudscraper/) or [HTMLSession](https://requests.readthedocs.io/projects/requests-html/en/latest/) instead
- **[Vito Esposito](https://stackoverflow.com/users/20564783)** (2022-11-24): https://i.imgur.com/Eh9fn3o.png Sweet that this worked, now the last step is saving in a file the link and in the other just the title of the first news, here's my attempt, how do i implement that?
- **me** (2022-11-24): @VitoEsposito the required input for [`.get`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#attributes) is *just the **name** of the attribute* that you want the value of, so it should be **`a.get('href')`** [and not `a.get('a[href]')`, which returns `None`]. I've also added some alternate ways to save the data to a file as an "Added EDIT" to my answer, if you're interested
