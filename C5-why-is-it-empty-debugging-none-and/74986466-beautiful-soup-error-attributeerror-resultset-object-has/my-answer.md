---
title: "Beautiful Soup Error AttributeError: ResultSet object has no attribute 'get"
site: stackoverflow
question_id: 74986466
answer_id: 74987772
url: https://stackoverflow.com/a/74987772
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-02T23:06:08Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74987772/revisions
accepted: true
score: 0
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7a649e4b477e2d63354dcc0d6b04675d29cceb8e1bd2a3bbf7eeda6bc0de7a97
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74987772>, 2023-01-02; **accepted**; score 0. Text as retrieved 2026-10-12.

Your code has two different variables, both named `s`

> ```python
> s = requests.session()
> ```

and

> ```python
>         s = soup.find_all("loc") ## the ResultSet
> ```

that is why, in the a lofter the first iteration or the *`for urls in b:...`* loop,
`s.get(one_sitemap)` will raise error, because it is no longer a `requests.sessions.Session` object but is now a `bs4.element.ResultSet` object.

---

**You should rename one of them**, like

```python
        loc_rs = soup.find_all("loc") ## renamed var
        
        for url in loc_rs: ## use renamed var
            loc = url.getText() 
```

or

```python
sess = requests.session() ## renamed var

for a,b in all_sitemaps.items():
    for urls in b:
        one_sitemap = urls
        pip_sitemap = sess.get(one_sitemap) ## use renamed var
        soup= bs4.BeautifulSoup(pip_sitemap.text,'html.parser')
```

---

You can also just directly loop through `.find_all` - no need for saving the second `s` variable.

```python
        for url in soup.find_all("loc"):
            loc = url.getText() 
```
