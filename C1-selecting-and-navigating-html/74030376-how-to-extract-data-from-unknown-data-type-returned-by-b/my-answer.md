---
title: "How to extract data from unknown data type returned by BS html parser"
site: stackoverflow
question_id: 74030376
answer_id: 74071424
url: https://stackoverflow.com/a/74071424
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-14T15:19:11Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74071424/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f500c45d3eb866026aa628fcb6c77b8ec07bfbde225810003b53dca3435ce925
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74071424>, 2022-10-14; **accepted**; score 0. Text as retrieved 2026-10-12.

> Can anyone tell what is the data format

It looks like either json or stringified json - which you probably realized, since you're using `json.loads`; I don't think parsing with BeautifulSoup *before* parsing json is necessary at all, but I can't be sure without knowing what `response.content` looks like - in fact, if `response.json()` works, even `json.loads` becomes unnecessary.

<br>

>  ...the output of BeautifulSoup after html parsing...

> ...and why find() and find_all() not working with it.

There's not much point to using `BeautifulSoup` (which is for *html parsing* as you yourself have noted!) unless the input is in a html/lxml/xml format. Otherwise, it tends to be just parsed as document with a single NavigableString (and that's likely what happened here); so then it looks [to bs4] like there's nothing to `find`.

<br>

Anyway, I downloaded the document as a txt and then read it and extracted the one value [which is a HTML string] with
```python
docContents = open('Unknow Data Type.txt', mode='r', encoding='utf-8-sig').read()
formHtml = json.loads(docContents)['form']
```
(The encoding took a little bit of trial and error to figure out, but I expect that step will be unnecessary for you as you have the raw contents.)

After that, `formHtml` can be parsed like any HTML string with `BeautifulSoup`; since it's just tables, you can even [use `pandas.read_html` directly][1], but since  you asked about `find` and `find_all`, I tried this little example:
```python
formSoup = BeautifulSoup(formHtml, 'html.parser')

for t in formSoup.find_all('table'):
    print('+'*100)
    for r in t.find_all('tr'):
        cols = [c.text for c in r.find_all(['td', 'th'])]
        cols = [f'{c[:10].strip():^12}' for c in cols] #just formatting
        print(f'| {" | ".join(cols)} |')
    print('+'*100)
```
It prints the tables as output:
```lang-none
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  DISTRICT:   |   KASARGOD   |  LOCAL BODY  |  G14001-Kum  |
|    WARD:     |  001-ANNADU  |  POLLING ST  |  002-G J B   |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
|  Serial No   |     Name     |  Guardian's  |  New House   |  House Name  |  Gender / A  |  ID Card No  |
|      1       |              |     Adru     |      1       |              |    M / 55    |  KL/01/002/  |
|      2       |              |    Battya    |      1       |              |    F / 41    |  KL/01/002/  |
|      3       |              |              |  MOIDEEN KU  |     289      |  C.H.NAGAR   |    F / 22    |  SECID15757  |
|     566      |              |  MOHAMMED K  |     296      |  ANNADKA HO  |    M / 49    |  SECID15400  |
|     567      |              |  MOIDDEEN K  |     296      |  ANNADKA HO  |    F / 40    |  SECID15400  |
|     568      |              |  MOHAMMED K  |     296      |  MUNDRAKOLA  |    M / 36    |  SECID15400  |
|     569      |              |    RADHA     |     381      |  MACHAVU HO  |    M / 23    |  SECID15400  |
|     570      |              |  SHIVAPPA S  |     576      |  UJJANTHODY  |    F / 47    |  ZII0819813  |
|     571      |              |  SURESHA K   |     826      |  KARUVALTHA  |    F / 33    |  JWQ1718857  |
|  കൂട്ടിച്ചേ  |
|     572      |   DIVYA K    |  SUNDARA K   |     182      |  BHANDARA V  |    F / 24    |  ZII0767137  |
|     573      |   KUNHAMMA   |  ACHU BELCH  |     185      |  PODIPALLA   |    F / 84    |  KL/01/002/  |
|     574      |  SUJATHA M   |  KESHAVAN K  |     186      |  PODIPALLA   |    F / 48    |  JWQ1687797  |
|     575      |   SARATH M   |  SUJATHA M   |     186      |  PODIPALLA   |    M / 25    |  SECID4BCFE  |
|     576      |   SAJITH K   |  SUJATHA M   |     186      |  PODIPPALLA  |    M / 21    |  ZII3300043  |
|  തിരുത്തലുക  |
|     ഇല്ല     |
|  ഒഴിവാക്കലു  |
|     ഇല്ല     |
|  |
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
```


  [1]: https://i.sstatic.net/AGYuJ.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[user3384929](https://stackoverflow.com/users/3384929)** (2022-11-02): How can make this to pandas dataframe?
- **me** (2022-11-02): @user3384929 you can get dataframe from `formHtml` directly.  `dfList = pandas.read_html(formHtml)` and then `dfList[0]` will return the first table, and  `dfList[1]` will return the second table
