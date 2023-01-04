---
title: "Error bs4: find_all | development vs production"
site: stackoverflow
question_id: 75011354
answer_id: 75012357
url: https://stackoverflow.com/a/75012357
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-04T23:15:48Z
last_edited: 2023-01-04T23:29:49Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75012357/revisions
accepted: false
score: 0
chapter: C9
chapter_title: "Blocked requests: headers, Cloudflare, scraping services"
cluster: scrape-blocked-headers-antibot
helpers_referenced: [linkToSoup_scrapingAnt]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 032d31eaba58382c0fa58926bcf242375398e8573843f601d60c4c45df95e05c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75012357>, 2023-01-04, last edited 2023-01-04; score 0. Text as retrieved 2026-10-12.

> My goal is to grab all **divs** who have anything inside **title** and are inside the `div class="indicator-today-container"`

To avoid raising errors like this in these cases, it's better to avoid chaining `.find`s and instead use [`.select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php).

```python
container_indicadores = exampleSoup.select('div.indicator-today-container div[title]')
```

That way, even if you don't find anything, you'll end up with an empty list, but no errors will be raised.

---

> `'NoneType' object has no attribute 'find_all'`

> But **first** variable is `None`

[So the last line of your first snippet is basically equivalent to `container_indicadores = None.find_all('div', {'title': True})` and ofc that will raise an error.] You should check whether your request [was successful](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses)

```python
exampleFile = requests.get(f'https://statusinvest.com.br/acoes/petr4',headers=headers)
print(exampleFile.status_code, exampleFile.reason, 'from', exampleFile.url)
```

For me, that prints ***`403 Forbidden from https://statusinvest.com.br/acoes/petr4`*** (and if I try with [cloudscraper](https://pypi.org/project/cloudscraper/) it raises a **`CloudflareChallengeError`** exception - *`Detected a Cloudflare version 2 Captcha challenge...`*, so they seem to have very good anti-bot blockers.)

---

> `example = exampleFile.text`

> Values:

Often, it's easier to spot the issue if you take a look at `exampleSoup.get_text()` instead:[![cfErr][1]][1]

---

[This is a screenshot](https://i.sstatic.net/ikUum.png) of what I get if I [use ScrapingAnt](https://pastebin.com/5ibz2F6p) [and I would expect similar results [with selenium](https://pastebin.com/VLZ2vPYK)].


  [1]: https://i.sstatic.net/LlDiM.png
