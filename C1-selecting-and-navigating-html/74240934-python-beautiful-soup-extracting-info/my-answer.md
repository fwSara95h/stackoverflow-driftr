---
title: "python: beautiful soup extracting info"
site: stackoverflow
question_id: 74240934
answer_id: 74241299
url: https://stackoverflow.com/a/74241299
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-28T21:58:12Z
last_edited: 2022-10-28T22:05:26Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74241299/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 37cbd943e8fd3259b0bf295db88f87507f22528907f224f0b71c35d54d684806
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74241299>, 2022-10-28, last edited 2022-10-28; score 0. Text as retrieved 2026-10-12.

You can get it with just one statement (`select`) using [CSS selectors](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:-soup-contains) : 
```python
# t3selector = ....
t3 = soup.select_one(t3selector).get_text(strip=True) 
```
where
```python
t3selector = 'h3:-soup-contains("Investment") ~ * .amount'
```
if you just want the text from an element with a class `amount` inside a sibling of a `h3` containing "Investment", but if you want exactly

>  get h3 tag WITH text Investment and from there get next sibling and another next sibling with tag p then span and get the contents

you'll need a slightly more specific selector

```python
t3selector = 'h3:-soup-contains("Investment") + * + p span'
```

( if the `span` must be a child [direct descendant] of `p`, then end with `p > span` )

<hr>

And the correct way to utilize `lambda` here would be something like:

```python
t3 = soup.find(
    lambda tag:tag.name=="h3" and "Investment" in tag.text
).find_next_sibling("p").find("span").get_text(strip=True)
```

but I think the selector method is better because this has too many calls - if any of the `find`s return `None`, an error will be raised.

<hr>

Actually, even with the selector, it's safest to use
```python
t3 = soup.select_one(t3selector)
if t3 is not None: t3 = t3.get_text(strip=True) 
```
