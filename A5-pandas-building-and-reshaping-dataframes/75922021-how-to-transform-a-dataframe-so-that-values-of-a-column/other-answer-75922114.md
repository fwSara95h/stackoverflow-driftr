---
title: "How to transform a dataframe so that values of a column are the column names and column names are rows but unstacked?"
site: stackoverflow
question_id: 75922021
answer_id: 75922114
url: https://stackoverflow.com/a/75922114
author: "Chrysophylaxs"
author_url: https://stackoverflow.com/users/9499196
posted: 2023-04-03T17:17:11Z
last_edited: never
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8694920af88917d392cdddc6cfc25bc15165228c9e356677c57536bc52d0e485
role: another answer on the same question, kept as context; not my work
---

# Answer by [Chrysophylaxs](https://stackoverflow.com/users/9499196) — 2023-04-03

Posted on Stack Overflow, <https://stackoverflow.com/a/75922114>, 2023-04-03. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Maybe via [`pivot`][1]?
```
import pandas as pd

df = pd.read_clipboard() # Your df here

out = (
    df
    .pivot(index="User ID", columns="Status")
    .swaplevel(axis=1)
    .stack()
    .reset_index(names=["User ID", "Attribute Changed"])
    .rename_axis(None, axis=1)
)
```

out:
```
   User ID Attribute Changed      After     Before
0        1          Favorite  Chocolate  Chocolate
1        1              Name      Stevy      Steve
2        2          Favorite    Vanilla  Chocolate
3        2              Name       John       John
```


  [1]: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[BeRT2me](https://stackoverflow.com/users/11865956)** (2023-04-03): Similar, Melting then pivoting: `df.melt(['User ID', 'Status']).pivot(index=["User ID", "variable"], columns="Status", values='value').reset_index().rename_axis(None, axis=1)`
- **[BeRT2me](https://stackoverflow.com/users/11865956)** (2023-04-03): Eliminate no-changes after pivoting: `df[df.After.ne(df.Before)]`
- **[Yisroel Len](https://stackoverflow.com/users/16627602)** (2023-04-03): Apparently I don't have the reputation to upvote but this worked perfectly. Thank you!
