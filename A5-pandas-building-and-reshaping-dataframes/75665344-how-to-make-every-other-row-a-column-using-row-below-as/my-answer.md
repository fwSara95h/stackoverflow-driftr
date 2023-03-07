---
title: "How to make every other row a column using row below as the value in Pandas?"
site: stackoverflow
question_id: 75665344
answer_id: 75666201
url: https://stackoverflow.com/a/75666201
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-07T19:07:02Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75666201/revisions
accepted: false
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a3a45451572ab41a0101559d332c28603359650a15366dfe6d521194ab9fc207
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75666201>, 2023-03-07; score 0. Text as retrieved 2026-10-12.

Using [`zip`](https://docs.python.org/3.3/library/functions.html#zip) and [list comprehension](https://www.programiz.com/python-programming/list-comprehension), you could do something like:

```py
df = pd.DataFrame.from_dict({
  'type': { 4: 'Second Product', 5: 'table', 6: 'First Product', 7: 'chair',
            8: 'Second Product', 9: 'desk', 10: 'First Product', 11: 'chair' },
  'id': { 4: 'cust1', 5: 'cust1', 6: 'cust1', 7: 'cust1',
          8: 'cust2', 9: 'cust2', 10: 'cust2', 11: 'cust2' }
})

itpZip = list(zip(df['id'][::2], df['type'][::2], [*df['type'][1::2], None]))
getProdTypes = lambda c: set(ctp[1] for ctp in itpZip if c==ctp[0])
custProdTypes = {ci: getProdTypes(ci) for ci in set(df['id'][::2])}
df = pd.DataFrame([{
    'cust': ci, **{ti:', '.join(
        p for c,t,p in itpZip if c==ci and t==ti
      ) for ti in getProdTypes(ci)}
} for ci in set(df['id'][::2])])
```

[[view stages and output][1]]


  [1]: https://i.sstatic.net/skRUK.png
