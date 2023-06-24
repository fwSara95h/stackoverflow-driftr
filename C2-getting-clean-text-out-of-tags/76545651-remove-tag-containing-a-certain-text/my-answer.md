---
title: "Remove tag containing a certain text"
site: stackoverflow
question_id: 76545651
answer_id: 76546063
url: https://stackoverflow.com/a/76546063
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-24T12:26:37Z
last_edited: 2023-06-24T18:43:55Z
revisions: 2
revision_history: https://stackoverflow.com/posts/76546063/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0f54c22da87b5986f4831988ce37f1a7176b1e0df05972ccab4d79945e4e3838
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76546063>, 2023-06-24, last edited 2023-06-24; score 0. Text as retrieved 2026-10-12.

<sub>(It's generally a good idea to reverse the results if you're going to be removing them one by one, so that if there are nested tags that qualify, the inner tag gets removed first and none of the results are removed before the loop reaches them.)</sub> 

Using `string` argument instead of `text` used to work for a while, but it seems not any more; however, you can use a function or a `lambda` expression:

```py
for p in reversed(soup.find_all(lambda t: t.name=='p' and 'Read our full' in t.text)): 
    if 'Read our full' in p.text:
        p.decompose()
```

the additional `if` also keeps outer `p` from getting deleted after inner `p` has been deleted, like `<div><p><p>Read our full article</p> here</p></div>` would become `<div><p>here</p></div>` instead of just `<div></div>`.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Сергей Кох](https://stackoverflow.com/users/18400908)** (2023-06-24): Both of your suggestions didn't work.
- **me** (2023-06-24): @СергейКох thanks for pointing it out. using `string` instead of `text` is supposed to work according to the docs [and did work for a while] but it's no longer working the same...I've updated my answer but I'll freely admit that the other answer offers a much better solution
