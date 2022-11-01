---
title: "beautifulsoup - obtaining the tag and it's parent from the text inside?"
site: stackoverflow
question_id: 74270903
answer_id: 74271340
url: https://stackoverflow.com/a/74271340
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-01T03:48:49Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74271340/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6e2d81aec573260871384e843ccf999034a7c280ef051d5e37f3b46c7484241
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74271340>, 2022-11-01; **accepted**; score 1. Text as retrieved 2026-10-12.

There are quite a few ways.

If you know the *exact* text, you can use `text` or `string` argument like 
```python
tags = soup.find_all(True, string="Top Rated Movies")
```
for more ways to use the `string` argument, like when you only know part of the text, you can check out the relevant section of [the documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#the-string-argument).

<hr>

Also, for partial text you can use `lambda`
```python
tags = soup.find_all(lambda x: x.name and x.text and 'Top Rated Movies' in x.text)
```

or, using `select` and the [`-soup-contains`](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#:-soup-contains) selector
```python
tags = soup.select(':-soup-contains("Top Rated Movies")')
```

<br>

Of course, with the partial-match methods, you'll end up getting the parent tags as well, but you can filter them out with 
```python
tags = [t for t in tags if not [p for p in t.parents if p in tags]]
```
or, if you're sure the target tag doesn't have any more tags nested within it,
```python
tags = [t for t in tags if t.find() is None]
```
although, in that case, you could have used the `:-soup-contains-own` selector and not needed to filter.

(Please note that you probably need to use the `html5lib` [parser](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser) for pseudo-classes like `-soup-contains`.)

<hr><hr>

If you want the tag name specifically, follow any of the above with: 
```python
for t in tags: print(t.name)
```
