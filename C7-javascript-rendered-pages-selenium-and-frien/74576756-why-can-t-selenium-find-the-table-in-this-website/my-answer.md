---
title: "Why can't Selenium find the table in this website?"
site: stackoverflow
question_id: 74576756
answer_id: 74579803
url: https://stackoverflow.com/a/74579803
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-26T04:49:45Z
last_edited: 2022-11-26T04:55:06Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74579803/revisions
accepted: true
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3c2e38bcd57446a59855ce8b28a8cf7a8a805e94c5bc815b8f1d451601e5536e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74579803>, 2022-11-26, last edited 2022-11-26; **accepted**; score 0. Text as retrieved 2026-10-12.

**Suggested solution:** I don't think you need bs4 at all here - you should try 
```python
tableEl = navegador.find_element(By.XPATH, '//center/table')
tableHtml = tableEl.get_attribute('outerHTML')

lista_completa_MLR=pd.read_html(tableHtml) # ,index_col=('Operadora'), header=(0), thousands='.')
# [I recommend trying without extra arguments first; if it works, try again with all arguments.]
```

<br>

---
---

**Explanation[s]:** There are a few things I feel the need to point out about your code:
- there is no need to use `BeautifulSoup` on `outerHTML` only to stringify the soup [it's redundant]

- `table border` is not a tag name [I don't think tag names can have spaces in them]. `table` is the tag name and `border` is an [attribute](https://www.w3schools.com/html/html_attributes.asp), so `.find(name = 'table border')` is pretty much guaranteed to always return `None`. The correct way would have been 
> ```python
> tabela = sopa.find(name='table', attrs={'border': ''})
> ```
> or, with [CSS selectors](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) [which I prefer]:
> ```python
> tabela = sopa.select('table[border=""]')
> ```
> **However**, this would still return `None` since

- the table needs to be **inside** `encontrarTabela`, but `encontrarTabela` has *already gone inside the table!*
> [![the table you want][1]][1]
> 
> [`tbody` is inside the table], so `str(tabela)` will just be `"None"` for two separate reasons, and
- for `pd.read_html` to work, there needs to be at least one `table` tag in the input

---

> Why can't Selenium find the table in this website?

Given that the code ran without errors before the last line in the snippet, I'd say that Selenium *did* find the table. It was *Pandas* that couldn't find the table, because there *were no table tags* to find in the input that was passed to `read_html`


  [1]: https://i.sstatic.net/2dlcK.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[VitSD](https://stackoverflow.com/users/20600875)** (2022-11-29): Thanks for the help! The point on BeautifulSoup is in virtue to the dynamic table presence that it would be different regarding to the options selected on the forms, I thought it wouldn't find the table so it won't return the HTML desired, something that sometimes happens. That table border was a try to get the table without using .find(name = tbody), what I was trying to do in the first place and thanks to you I understood why didn't work haha.
