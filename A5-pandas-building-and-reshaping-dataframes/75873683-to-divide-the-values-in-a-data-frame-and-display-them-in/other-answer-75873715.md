---
title: "To divide the values in a data frame and display them in the row below"
site: stackoverflow
question_id: 75873683
answer_id: 75873715
url: https://stackoverflow.com/a/75873715
author: "jezrael"
author_url: https://stackoverflow.com/users/2901002
posted: 2023-03-29T06:12:40Z
last_edited: 2023-03-29T06:19:27Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 009e2040f79e0676acf53aa1cc81cca75d19471bc3199ce0f3ffdf4f6e0fc472
role: another answer on the same question, kept as context; not my work
---

# Answer by [jezrael](https://stackoverflow.com/users/2901002) — 2023-03-29

Posted on Stack Overflow, <https://stackoverflow.com/a/75873715>, 2023-03-29, last edited 2023-03-29; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use [`DataFrame.assign`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html) for [`Series.str.split`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.split.html) and [`DataFrame.explode`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html), last assign empty string by [`Index.duplicated`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Index.duplicated.html) with [`DataFrame.loc`](http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html):


    df1 = df.assign(feature = df['feature'].str.split('/')).explode('feature')
    df1.loc[df1.index.duplicated(), ['model','kind']] = ''
    print (df1)
         model      kind    feature
    0   animal       cat       cute
    0                         small
    1  anmimal       dog   reliable
    1                          kind
    1                           big
    2   plants  mushroom  delicious
    2                          dark
    3   plants  gingseng    healthy
    3                        bitter
    3                     expensive
