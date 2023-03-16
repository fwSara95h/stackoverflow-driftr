---
title: "Python Pandas: Append a column with each cell being a dictionary to pre-existing data-frame"
site: stackoverflow
question_id: 75749042
answer_id: 75755016
url: https://stackoverflow.com/a/75755016
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-16T10:35:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75755016/revisions
accepted: true
score: 0
chapter: A5
chapter_title: "pandas: building and reshaping DataFrames"
cluster: pandas-dataframe-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f50edbfe1e85e4537d1b7838c0ee55d1dbbf9a3471cc0d0dcac9f5ce6095ee3c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-16

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75755016>, 2023-03-16; **accepted**; score 0. Text as retrieved 2026-10-12.

With list comprehension:

```py
df['ColDict'] = [{str(b): myfunc(v, b) for b in list_b} for v in df['val']]
```

With `apply` [and `lambda`]:

```py
df['ColDict'] = df['val'].apply(lambda v: {str(b): myfunc(v, b) for b in list_b})
```

> *I dislike using lambda expressions here because I already defined the function elsewhere and it feels wrong to need to define a separate univariate function for this context. But that is probably just a personal issue*

<sup>I still can't quite understand your aversion, since simplifying multivariate functions to univariate is probably my most common use of `lambda` and something I consider it rather nifty for; but then, I have my own pet peeves that would quite difficult to explain, so I can empathize somewhat. Anyway...</sup> You could alter `myfunc` definition to handle lists-of-keys (with a bit of recursion) and set `list_b` as the default value of the second argument so that it becomes optional:

```py
# list_b = [....] # define first so that it can be used as arg2 default below

def myfunc(arg1, arg2=list_b):
    if isinstance(arg2, list):
        return {str(k): myfunc(arg1, k) for k in arg2}

    ##### continue with ORIGINAL FUNCTION BODY #####
```

then you could just use `apply` without `lambda`:

```py
df['ColDict'] = df['val'].apply(myfunc)
```

---

> *Any idea about how to avoid the "a value is trying to be set on a copy of a slice from a DataFrame" warning, which seems to not matter? It arises in both solutions for me.*

If it's appearing for all solutions, then `df` itself might be the issue; is it copied/generated from another DataFrame? I don't recall ever experiencing this warning myself, but hopefully [this thread](https://stackoverflow.com/q/42379818/6146136) about the same message might help you somehow.

My immediate first thought was to make `df` an independent object by re-forming it (before adding the column) with something like

```py
df = pd.DataFrame.from_dict(df.to_dict('index'), orient='index')
```
