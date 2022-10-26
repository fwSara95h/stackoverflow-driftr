---
title: "Beatifulsoup find_all when a tag is not inside another tag"
site: stackoverflow
question_id: 74212070
answer_id: 74213323
url: https://stackoverflow.com/a/74213323
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-26T19:32:32Z
last_edited: 2022-10-26T19:51:17Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74213323/revisions
accepted: true
score: 0
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ca4c2c793885191c881b38708e7205bf8b7d920ff38654ff2effd578cde80450
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74213323>, 2022-10-26, last edited 2022-10-26; **accepted**; score 0. Text as retrieved 2026-10-12.

> Basically I don't want to extract a specific tag if it is inside another tag

I think the simplest way might be to use `find_all` just as you are now, and then filter out the nested tags by checking if they have ancestors/parents in the list
```python
sel = soup.find_all(['p', 'li', 'dl', 'tr', 'div', re.compile("^h[1-6]$")])
sel = [s for s in sel if not [p for p in sel if p in s.parents]]
```

 -- same results as getting tags if their tagName is in a list as long as if none of their parents have one of the listed names:
```python
selTags = ['p', 'li', 'dl', 'tr', 'div'] + [f'h{i}' for i in range(1,7)]
sel = soup.find_all(lambda t: t.name in selTags and not t.find_parent(selTags))
```

<hr>

but if you want to filter by a map 

> is there any way i can have some mapping like below and use in the code don't extract when the key is inside value

you could use

```python
parentMap = {'div':'div', 'p': 'tr'}
for i in range(1,7): parentMap[f'h{i}'] = 'div'
# parentMap = {'div': 'div', 'p': 'tr', 'h1': 'div', 'h2': 'div', 'h3': 'div', 'h4': 'div', 'h5': 'div', 'h6': 'div'}

sel = soup.find_all(
    lambda t: t.name in 
    ['p', 'li', 'dl', 'tr', 'div']+[f'h{i}' for i in range(1,7)]
    and not (
        t.name in parentMap and 
        t.find_parent(parentMap[t.name]) is not None
    )
)
```

<hr><hr>

In *this* case, you should get the same results either way, but if your html contained
```html
<p><tr>I am a row in a paragraph</tr></p>
```
then the first methods will return only the outer `<p>` tag whereas the last method will return both the `<p>` tag and the inner `<tr>` tag [unless you add `'tr': 'p'` to `parentMap`].
