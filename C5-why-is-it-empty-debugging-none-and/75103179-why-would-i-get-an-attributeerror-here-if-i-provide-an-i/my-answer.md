---
title: "Why would I get an AttributeError here if I provide an if statement to get around it?"
site: stackoverflow
question_id: 75103179
answer_id: 75104085
url: https://stackoverflow.com/a/75104085
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-13T01:48:57Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75104085/revisions
accepted: true
score: 1
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ba575a10aa39cee60ae46d14f3ed4a5785f06559be8657f446caca1de91c6ad
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75104085>, 2023-01-13; **accepted**; score 1. Text as retrieved 2026-10-12.

You should use **`if table_row.a is not None:`** instead, since `table_row.a` is the *"'NoneType' object"* mentioned in the error.

> ```python
>     if table_row.a.text is not None:
>         print(table_row.a.text) 
> ```

You've just shifted the error from the *`print...`* line to the *`if...`* line, since the **`.text`** part is what raised the error.

---

> I even did a version where I put an else statement that tells it to `continue` and I still get the same error

You probably tried something like *`if table_row.a.text is None: continue`*, but same issue there - it should be

```python
for i, table_row in enumerate(df_tr): 
    if not table_row.a: continue
    print(table_row.a.text) 
```
