---
title: "How can I align columns if rows have different number of values?"
site: stackoverflow
question_id: 75004850
answer_id: 75014335
url: https://stackoverflow.com/a/75014335
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-05T05:52:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75014335/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d2f91d1466dd62e9df50880e70c4a83eceff18900861087b82df06ceaf8963b0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75014335>, 2023-01-05; **accepted**; score 0. Text as retrieved 2026-10-12.

> make the columns merge if there are two statuses for example or other solutions

[If by "statuses" you mean the yellow labels ending in OPEN/UPCOMING/etc, then] it should be taken care of by the following parts of the `getDetails_iiaRow` (below the dividing line):

```python
    labels = cssSelect(iiaEl, 'div.field span.label')
```

and then

```python
        'labels': ', '.join([l.text.strip() for l in labels])
```

So, multiple labels will be separated by commas (or any other separator you apply `.join` to).
[![screenshot][1]][1]

---

> ```python
>     initiative_item = browser.find_elements(By.CSS_SELECTOR, "initivative-item")
>     initiatives = [item.text for item in initiative_item] 
> ````

Instead of doing it like this and then having to split and clean things, you should consider extracting each `item` in a more specific manner and have each "row" be represented as a dictionary (with the column-names as the keys, so nothing gets mis-aligned later). If you wrap it as a function:

```python
def cssSelect(el, sel): return el.find_elements(By.CSS_SELECTOR, sel)
def getDetails_iiaRow(iiaEl):
    title = cssSelect(iiaEl, 'div.search-result-title')
    labels = cssSelect(iiaEl, 'div.field span.label')
    iiarDets = {
        'title': title[0].text.strip() if title else None,
        'labels': ', '.join([l.text.strip() for l in labels])
    }

    cvSel = 'div[translate]+div:last-child'
    for c in cssSelect(iiaEl, f'div:has(>{cvSel})'):
        colName = cssSelect(c, 'div[translate]')[0].text.strip()
        iiarDets[colName] = cssSelect(c, cvSel)[0].text.strip()

    link = iiaEl.get_attribute('href')
    if link[:1] == '/':
        link = f'https://ec.europa.eu/{link}'
    iiarDets['link'] = iiaEl.get_attribute('href')

    return iiarDets
```

then you can simply loop through the pages like:

```python
initiative_list = []
for i in range(0, 2):
    url = f'https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives_de?page={i}'
    browser.get(url)
    time.sleep(random.randint(5, 10))
    initiative_list += [
        getDetails_iiaRow(iia) for iia in
        cssSelect(browser, 'initivative-item>article>a ')
    ]
```

and the since it's all cleaned already, you can directly save the data with

```python
pd.DataFrame(initiative_list).to_csv('Initiativen.csv', index=False)
```

The output I got for the first 3 pages looks like:
[![Initiativen.csv][2]][2]


  [1]: https://i.sstatic.net/3ngRl.png
  [2]: https://i.sstatic.net/lg2LO.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[JRGN1](https://stackoverflow.com/users/20469445)** (2023-01-06): thanks, that is really helpful and seems to be working. But unfortunatelly it has created a new issue. For example in the 8th line of the output the title contains a comma: 'Überarbeitung der EU-Rechtsvorschriften zur Einstufung, Kennzeichnung und Verpackung von Chemikalien' and thus the part behind the comma is moved into the next column and erverything is shifted within that row. Why does your output not do that?
- **[JRGN1](https://stackoverflow.com/users/20469445)** (2023-01-06): I have changed the separator from , to ; and now it looks nice :)
- **me** (2023-01-06): @JRGN1 good to hear! although it's strange bc CSV viewers/editors/etc are suppose to ignore commas inside quotes and pandas is supposed to take care or that. But still, you could also use [`.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) if you don't want to worry about separators
- **[JRGN1](https://stackoverflow.com/users/20469445)** (2023-01-10): ok, thanks. Maybe I will try that as well or are there also advantages of CSV compared to excel?
- **me** (2023-01-10): @JRGN1 CSV takes up less memory and is faster to process; and since it's such a simple format, it's fairly human-readable in raw form
