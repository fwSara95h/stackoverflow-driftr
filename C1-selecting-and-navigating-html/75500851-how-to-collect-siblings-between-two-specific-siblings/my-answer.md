---
title: "How to collect siblings between two specific siblings?"
site: stackoverflow
question_id: 75500851
answer_id: 75504991
url: https://stackoverflow.com/a/75504991
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-20T03:21:40Z
last_edited: 2023-02-20T03:40:18Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75504991/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: [linkToSoup]
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a752b498ca7b825a99674b0facce612a4e26aa9e4e9c5d95b8a00c208115ad8f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-20

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75504991>, 2023-02-20, last edited 2023-02-20; score 0. Text as retrieved 2026-10-12.

How you did it is pretty much what I would do, but you should unindent the *`chapter_data.append...`* statement by a level since there is no need to append to `chapter_data` for every `sib`. The example below parses [this Wikipedia page](https://en.wikipedia.org/wiki/Coal_gas).

```python 
# [ linkToSoup defined at https://pastebin.com/rBTr06vy ]
# soup = linkToSoup('https://en.wikipedia.org/wiki/Coal_gas') 

headerTags = soup.select('h2')
chapter_data, totalCh = [], len(headerTags)
for ci, (h, nxt_h) in enumerate(zip(headerTags, headerTags[1:]+[None]), 1):
    print('', end=f'\rAdding chapter {ci} of {totalCh}') ## track progress

    texts, htmls = '', ''
    for sib in h.next_siblings:
        if sib == nxt_h: break
        if callable(getattr(sib, 'get_text', None)): 
            texts += '\n' + sib.get_text(' ', strip=True)
        htmls += '\n' + str(sib).strip()
    
    # texts = BeautifulSoup(htmls).get_text(' ', strip=True)
    chapter_data.append({
        'chapter': h.get_text(' ', strip=True),
        'text': texts.strip(), 'html': htmls.strip()
    })
print('\n')

chapters = pd.DataFrame(chapter_data)
```

Output:
> [![opdf][1]][1]

---

Btw, [this][2] is what it would look like if my *`chapter_data.append...`* statement was indented like yours - there would be many redundant `append`s for each chapter.

---

EDIT: just realized that you can probably get your `chapter_data` in one statement with [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```python
chapter_data = [{
    'chapter': h.get_text(' ', strip=True),
    'html': '\n'.join(
        str(sib) for sib in h.next_siblings if
        sib!=nxt_h and nxt_h not in sib.previous_siblings
    ).strip()
} for h, nxt_h in zip(headerTags, headerTags[1:]+[None])]
```

[View Screenshot with Output][3]


  [1]: https://i.sstatic.net/J5acG.png
  [2]: https://i.sstatic.net/7SAoe.png
  [3]: https://i.sstatic.net/qYh9D.png
