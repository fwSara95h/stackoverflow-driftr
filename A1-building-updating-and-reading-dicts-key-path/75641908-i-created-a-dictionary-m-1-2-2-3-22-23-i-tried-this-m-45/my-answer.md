---
title: "I created a dictionary, m={1: 2, (2, 3): (22, 23)}. I tried this m[#]=45, what happens?"
site: stackoverflow
question_id: 75641908
answer_id: 75643010
url: https://stackoverflow.com/a/75643010
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-05T14:42:15Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75643010/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6f0f7066538b35d6be1e207bf987fe8e78a58d4e00604edba3f3749d6c21cf26
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75643010>, 2023-03-05; score 0. Text as retrieved 2026-10-12.

> ```py
> m[#]=45
> ```

As you can see, everything after the `#` [is commented](https://cscircles.cemc.uwaterloo.ca/3-comments-literals/#:~:text=In%20Python%2C%20any%20line%20of,when%20the%20program%20is%20run.); so, what you were actually trying to have executed was <kbd>**`m[`**</kbd> which **isn't valid syntax**. 

<br>

You could instead have

```py
m['#'] = 45
```

since it will not get treated as a comment if it's within a string.
