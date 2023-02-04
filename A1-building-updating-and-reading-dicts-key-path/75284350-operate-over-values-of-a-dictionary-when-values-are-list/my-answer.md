---
title: "operate over values of a dictionary when values are lists"
site: stackoverflow
question_id: 75284350
answer_id: 75343141
url: https://stackoverflow.com/a/75343141
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-04T05:19:45Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75343141/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8f26bea8b6c21c215a3e94f230576a1d29b469c3dbf64177c0e9e1578c5db797
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75343141>, 2023-02-04; **accepted**; score 1. Text as retrieved 2026-10-12.

> ```python
>     data[key] = [value for value in values if value not in stop_words]
> ```

You're comparing the full string (`value`) against the words in `stop_words`, when you actually want to *remove words **from*** the string - for which you need to `split` each string into words and check each word to filter before joining them up again:

```python
def remove_stopwords(orig, swList):
    return ' '.join(w for w in str(orig).split() if w.lower() not in swList)
```

You can apply this function to every string.

```python
stop_words = set(sw.lower() for sw in stopwords.words("english"))


for key, values in data.items():
    # data[key] = [remove_stopwords(v, stop_words) for v in values] # keeps empty strings
    swFil_gen = (remove_stopwords(v,stop_words) for v in values) # generator [not list]
    data[key] = [cleanStr for cleanStr in swFil_gen if cleanStr] # no empty strings
```

<sup>[The `.lower()`s make everything lower case so that the comparisons are case-insensitive, although it's not really necessary in this case- but then, neither is `set` since `stopwords.words("english")` does not contain any duplicate values.]</sup>

---

You can also use [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension) like

```python
# data = {... # OR [if you don't want to change data]
cleaned_data = {key: [cleanStr for cleanStr in (
    remove_stopwords(v, stop_words) for v in values
) if cleanStr] for key, values in data.items()}
```

---

`cleaned_data` [or `data` after the `for` loop] should look like

> ```python
> {'ACCOUNT_CLOSURE': ['account closure',
>   'close account',
>   'close bank',
>   'terminate account',
>   'account deletion',
>   'cancel account',
>   'account cancellation'],
>  'ACCOUNT_CHANGE': ['change account',
>   'switch account',
>   'change private savings',
>   'convert family package',
>   'change title account',
>   'make title account family',
>   'help access documentation']}
> ```
