---
title: "add a prefix to all lines of a dataframe's column"
site: stackoverflow
question_id: 75048117
answer_id: 75048286
url: https://stackoverflow.com/a/75048286
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T13:54:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75048286/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 284c36f6a2c0aa14277c40072daa04cd3062f4d3c7f3e0f9c6b0ad75bf8ceee8
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75048286>, 2023-01-08; score 0. Text as retrieved 2026-10-12.

That's the expected behavior- [`.add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html) adds prefix to the *labels* (row labels if it's a series like `correct_X_test['review']`or`Modified_X_test`, column labels if it's a DataFrame like `correct_X_test`). 

You could try something like 

```python 
correct_X_test["review_prefixed"] = [f' xxxx {r}' for r in list(correct_X_test["review"])]
```

And then `correct_X_test` will have an added column with prefixed `review`s.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ouroboros1](https://stackoverflow.com/users/18470692)** (2023-01-08): `correct_X_test["review_prefixed"] = " xxxx " + correct_X_test["review"]` will do.
- **me** (2023-01-08): @ouroboros1 thanks! I didn't know that syntax (or maybe I forgot?) I'm used to using pandas only for saving the data at the last step
