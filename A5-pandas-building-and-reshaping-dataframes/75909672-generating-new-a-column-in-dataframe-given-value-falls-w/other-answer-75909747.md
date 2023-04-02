---
title: "Generating new a column in dataframe given value falls within a certain range of another column value"
site: stackoverflow
question_id: 75909672
answer_id: 75909747
url: https://stackoverflow.com/a/75909747
author: "SomeDude"
author_url: https://stackoverflow.com/users/1410303
posted: 2023-04-02T01:57:13Z
last_edited: never
accepted: true
score: 3
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8fc0f3bca7459cc52afd5a92cdece0a078e0f9d9c273276c5467ede00f218523
role: another answer on the same question, kept as context; not my work
---

# Answer by [SomeDude](https://stackoverflow.com/users/1410303) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75909747>, 2023-04-02; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Use [`Series.between`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html). It should be fast.

    df['Eq'] = df['A'].between(df['B'].sub(2), df['B'].add(2)).astype(int)
