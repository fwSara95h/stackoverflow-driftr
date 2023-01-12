---
title: "How to avoid running into IndexError: list index out of range error if an element is nonexistent while parsing xml with BeautifulSoup in python"
site: stackoverflow
question_id: 75095388
answer_id: 75102124
url: https://stackoverflow.com/a/75102124
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-12T20:44:35Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75102124/revisions
accepted: false
score: 0
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7737ca570d898d64ebaa5ce4eb984f88ae20a1415a0dff7b76608ff9c7acba41
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-12

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75102124>, 2023-01-12; score 0. Text as retrieved 2026-10-12.

If you just want to avoid raising the error, add a conditional `break`

```python
for i in range(0,len(ID)):
      if not i < len(Cat): break ## <-- break loop if length of Cat is exceeded

      if (Cat[i] == CatDict):
        Cat[i] == CatDict.get(Cat[i])
       
      rows = [ID[i].get_text(), Title[i].get_text(), Cat[i])
      dataDf.append(rows)
```
