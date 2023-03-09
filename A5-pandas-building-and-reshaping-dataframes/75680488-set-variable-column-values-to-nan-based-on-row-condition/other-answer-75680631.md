---
title: "Set variable column values to nan based on row condition"
site: stackoverflow
question_id: 75680488
answer_id: 75680631
url: https://stackoverflow.com/a/75680631
author: "Marcelo Paco"
author_url: https://stackoverflow.com/users/11286032
posted: 2023-03-09T05:07:44Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4b46611da4a7fa739729b2a1d0858062f3b6a306095f94d78b58b1c322360c90
role: another answer on the same question, kept as context; not my work
---

# Answer by [Marcelo Paco](https://stackoverflow.com/users/11286032) — 2023-03-09

Posted on Stack Overflow, <https://stackoverflow.com/a/75680631>, 2023-03-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can get the `values` of `df["col_ind"]`, iterate through them and set the `slice` to `np.nan`:

    vals = df["col_ind"].values
    for i, v in enumerate(vals):
        df.iloc[i, -v:] = np.nan

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[thefrollickingnerd](https://stackoverflow.com/users/10339757)** (2023-03-09): Yeah this works but I was hoping for a more efficient solution. It's pretty time costly. Thank you though
