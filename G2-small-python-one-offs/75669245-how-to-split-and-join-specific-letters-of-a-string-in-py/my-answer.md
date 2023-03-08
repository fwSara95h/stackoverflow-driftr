---
title: "How to split and join specific letters of a string in Python?"
site: stackoverflow
question_id: 75669245
answer_id: 75669353
url: https://stackoverflow.com/a/75669353
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-08T04:04:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75669353/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e149768b92cc51dd4428106629dd5e5f804fa569df81250856377c62197fff0d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75669353>, 2023-03-08; score 0. Text as retrieved 2026-10-12.

I thing the simplest way would be to [`split`](https://www.programiz.com/python-programming/methods/string/split) by "al" before collecting all letters:

```py
keep_substring = 'al'
keep_whitespace = False # set True to keep spaces, newline characters, etc
original_words = "installation altitude international"

opList = []
for ss in original_words.split('al'):
    if opList: opList.append(keep_substring)
    opList += [c for c in ss if c.strip() or keep_whitespace]
print(opList)
```

After the loop, `opList` should be as you wanted the output to be

> ```py
> ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', 'al', 't', 'i', 't', 'u', 'd', 'e', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
> ```

But if you set `keep_whitespace = True`, the spaces will also be included in `opList`

> ```py
> ['i', 'n', 's', 't', 'al', 'l', 'a', 't', 'i', 'o', 'n', ' ', 'al', 't', 'i', 't', 'u', 'd', 'e', ' ', 'i', 'n', 't', 'e', 'r', 'n', 'a', 't', 'i', 'o', 'n', 'al']
> ```
