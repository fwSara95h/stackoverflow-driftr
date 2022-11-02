---
title: "Webscraping - Python - attribute href"
site: stackoverflow
question_id: 74282355
answer_id: 74283311
url: https://stackoverflow.com/a/74283311
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-02T00:57:53Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74283311/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ae977d403c7d4b15fbc99992f27cbda7b0a4f6413f776e79b5e7e08bd1e71584
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74283311>, 2022-11-02; score 0. Text as retrieved 2026-10-12.

Two issues here:

 - You're trying to run `.get` on *list* of tags (which is what `find_all` returns), when it's meant to be used directly on individual tags
 - The `h4` tag doesn't *have* a `href` attribute - that belongs to the `a` tag *inside* the header tag, so even if you defined it as `h4 = site_html.find('h4')` (to get just the *first* `h4` tag), `h4.get('href')` would still return `None`

You would need 
```python
h4 = site_html.find('h4')
h4.a.get('href')
```
to get the first `href` you want, and even that would raise an error if the first `h4` in the page did not contain an `a` tag ....

<hr><hr>

You can use 
```python
[h.a.get('href') for h in site_html.find_all('h4') if h.find('a') and h.a.get('href')]
``` 
or, with [CSS selectors](https://www.w3schools.com/cssref/css_selectors.php),
```python
[a.get('href') for a in site_html.select('h4 a[href]')]
```

<hr>

Either of the above should return
```lang-none
['https://www.eloscimento.com.br/diversos/',
 'https://www.eloscimento.com.br/pintura/',
 'https://www.eloscimento.com.br/acabamento/',
 'https://www.eloscimento.com.br/basico/',
 'https://www.eloscimento.com.br/eletrica/',
 'https://www.eloscimento.com.br/ferramentas/',
 'https://www.eloscimento.com.br/hidraulica/',
 'https://www.eloscimento.com.br/metais/',
 '#mobileMenui40',
 '#mobileMenui55',
 '#mobileMenui326',
 '#mobileMenui73',
 '#mobileMenui91',
 '#mobileMenui214',
 '#mobileMenui240',
 '#mobileMenui375',
 'https://www.eloscimento.com.br/cabecotes/',
 'https://www.eloscimento.com.br/climatizadores/']
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Hélder Neves](https://stackoverflow.com/users/20392176)** (2022-11-02): I love you, man. Its exctly what i need. I'm mean, seriously, thank you!!!!!
