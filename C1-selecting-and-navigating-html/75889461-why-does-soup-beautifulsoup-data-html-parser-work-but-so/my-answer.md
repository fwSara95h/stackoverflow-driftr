---
title: "Why does soup=BeautifulSoup(data, \"html.parser\") work but soup2=... does not?"
site: stackoverflow
question_id: 75889461
answer_id: 75895103
url: https://stackoverflow.com/a/75895103
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-31T05:21:51Z
last_edited: 2023-03-31T17:15:31Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75895103/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f2e316aba2e7463ce9c43cec320fbd5bec81bbd72110b76b33e8068f8e8cd30a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-31

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75895103>, 2023-03-31, last edited 2023-03-31; score 0. Text as retrieved 2026-10-12.

As already mentioned in the comments, since `data` is [file object](https://docs.python.org/3/glossary.html#term-file-object), after it's [been read by][1] `BeautifulSoup` the first time, it needs to be re-opened before being read again. You probably wouldn't have that issue if you had used 

```py
with open(url, encoding="utf8") as f:
    data = f.read()
```

since `.read()` returns a string, so `data` would just be a string.

---

You can also just do away with `data` entirely and use

```py
# soup = BeautifulSoup(open(url, encoding="utf8"), "html.parser") ## less safe
with open(url, encoding="utf8") as f: soup = BeautifulSoup(f, "html.parser")
```

<sup>Btw, it's [better to use](https://stackoverflow.com/q/19711344/6146136) `with open`, since a bare `open` [should be](https://realpython.com/why-close-file-python/) followed by `.close` later [but you can't do that if you do it like in the commented line].</sup>

  [1]: https://i.sstatic.net/0IH84.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[henri.haiti](https://stackoverflow.com/users/21406103)** (2023-03-31): Hmm, I tested it but it doesn't work or I'm missing something else. Creating `soup` and `soup2` by opening the file like you propose and calling `data` for each returns empty when I `print(soup2)`. When I create a seperate `data2` for `soup2` both `print(soup)` and `print(soup2)` contain XHTML-Code. So this is what I'm doing for now, doesn't look nice but it works
- **me** (2023-03-31): @henri.haiti How strange - I [can't replicate](https://i.sstatic.net/4kPKs.png) such behavior at all, which I rather expected since a string object *shouldn't* empty out just like that... Are you sure you're not re-defining `data` anywhere in your code before trying to create `soup2`? Also, it's not *that* bad to have `data2`, but you could do away with `data` entirely if it only works the 1st time and just have pass `open...` to BeautifulSoup [I added an edit to my answer].
- **[henri.haiti](https://stackoverflow.com/users/21406103)** (2023-03-31): Ah, nice! This is a cleaner looking way to create `soup` without multiple `data` and does the same. This gets an entry in my Python cheat sheet document, thanks!
