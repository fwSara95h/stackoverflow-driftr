---
title: "Replace span tags with whitespace or parse contents as new column with pandas.read_html"
site: stackoverflow
question_id: 74409839
answer_id: 74410700
url: https://stackoverflow.com/a/74410700
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-12T05:54:42Z
last_edited: 2022-11-12T06:00:15Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74410700/revisions
accepted: false
score: 1
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b5b6b1223639ff3dd2f083c650198d8ece4f75189442fbda37c6e694e496b134
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74410700>, 2022-11-12, last edited 2022-11-12; score 1. Text as retrieved 2026-10-12.

Btw, <sub>you don't need to go through those steps with `soup` and `find_all` &nbsp; - &nbsp; `read_html` already uses the same [or at least very similar] parsers as bs4 so you could just have </sub>
```python
table = pd.read_html(driver.page_source)[0] # , flavor='lxml')[0] # default
```
<sub>or even directly `pd.read_html(get_url(page=1))` - it [doesn't always work for all pages](https://stackoverflow.com/questions/74305179/web-scraping-using-pandas/74333634#74333634), but **it seems to work for <i>your</i> page**; it won't allow for the solutions I'm about to suggest, but I thought it was worth mentioning this convenience in case you didn't already know.</sub>

---

Anyway, my first solution is going to seem a bit hacky, but it has worked for me so far - since, `read_html` doesn't seem to have any string-separator argument like bs4's [`get_text`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text) does, we can try to create the same effect by just adding spaces to the end of every tag in the html using `.replace`. 
```python
table = pd.read_html(driver.page_source.replace('</', '&nbsp;</'))
```

---

If you are wary of messing with text-replace on html strings, or are worried about adding unwanted spaces (even though it *doesn't*, as far I have seen), or just want more control of how the text is extracted from table cells, you can also convert the bs4 `table` tag to a python dictionary using [`get_text`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text) [with space (`' '`) separator] and [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp).
```python
tableSoup = soup.find('table')
tableHeaders = [
    h.get_text(' ', strip=True)
    for h in tableSoup.select('thead tr th')
]
tableData = [{h: c.get_text(' ', strip=True) for h, c in zip(
    tableHeaders, [cell for cell in r.select('td')]
)} for r in tableSoup.select('tbody tr')]
table = pd.DataFrame(tableData)
```
You could even replace `get_text` with your own function if you want to customize how cell values are extracted and/or processed, but as it is, it [and the first method with `.replace`] creates a DataFrame like: 

| Politician                                 | Traded Issuer                      | Published       | Traded      | Filed after   | Owner       | Type   | Size        | Price   |
|:-------------------------------------------|:-----------------------------------|:----------------|:------------|:--------------|:------------|:-------|:------------|:--------|
| Pete Sessions Republican House TX          | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 9 Nov  | days 1        | Undisclosed | buy    | 15K - 50K   | N/A     |
| Pete Sessions Republican House TX          | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 7 Nov  | days 3        | Undisclosed | buy    | 50K - 100K  | N/A     |
| Pete Sessions Republican House TX          | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 7 Nov  | days 3        | Undisclosed | buy    | 1K - 15K    | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 3 Nov  | days 7        | Undisclosed | sell   | 250K - 500K | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 3 Nov  | days 7        | Undisclosed | sell   | 500K - 1M   | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 3 Nov  | days 7        | Undisclosed | sell   | 250K - 500K | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 7 Nov  | days 3        | Undisclosed | sell   | 250K - 500K | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 3 Nov  | days 7        | Undisclosed | sell   | 250K - 500K | N/A     |
| Brad Sherman Democrat House CA             | US TREASURY NOTE N/A               | yesterday 14:05 | 2022 3 Nov  | days 7        | Undisclosed | sell   | 15K - 50K   | N/A     |
| Debbie Wasserman Schultz Democrat House FL | ADAMS RESOURCES & ENERGY INC AE:US | yesterday 14:05 | 2022 27 Oct | days 14       | Child       | sell   | 1K - 15K    | 32.27   |
| Kathy Manning Democrat House NC            | 3M Co MMM:US                       | yesterday 14:05 | 2022 12 Oct | days 29       | Spouse      | buy    | 1K - 15K    | 108.95  |
| Kathy Manning Democrat House NC            | Accenture PLC ACN:US               | yesterday 14:05 | 2022 12 Oct | days 29       | Spouse      | buy    | 1K - 15K    | 250.07  |
| Kathy Manning Democrat House NC            | Adobe Inc ADBE:US                  | yesterday 14:05 | 2022 12 Oct | days 29       | Spouse      | sell   | 1K - 15K    | 286.15  |
| Kathy Manning Democrat House NC            | Alphabet Inc GOOGL:US              | yesterday 14:05 | 2022 12 Oct | days 29       | Spouse      | buy    | 1K - 15K    | 97.56   |
| Kathy Manning Democrat House NC            | Amazon.com Inc AMZN:US             | yesterday 14:05 | 2022 12 Oct | days 29       | Spouse      | buy    | 1K - 15K    | 112.9   |

[Markdown for the table above was copied from the output of `print(table.drop([''], 'columns').to_markdown(index=False))`.]
