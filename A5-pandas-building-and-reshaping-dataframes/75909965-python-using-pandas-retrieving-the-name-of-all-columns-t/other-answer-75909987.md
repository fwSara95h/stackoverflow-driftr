---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
answer_id: 75909987
url: https://stackoverflow.com/a/75909987
author: "Long Luu"
author_url: https://stackoverflow.com/users/11235205
posted: 2023-04-02T03:31:34Z
last_edited: never
accepted: false
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7ad5f4c3c4871c58d15f6ab22eaad4f2b98adf8c7797406fe0982051ba733c56
role: another answer on the same question, kept as context; not my work
---

# Answer by [Long Luu](https://stackoverflow.com/users/11235205) — 2023-04-02

Posted on Stack Overflow, <https://stackoverflow.com/a/75909987>, 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

Based on Marcelo's comment, you can use:
```python
from pandas.api.types import is_numeric_dtype

numeric_columns = []
for column in df.columns:
    if is_numeric_dtype(df[column]):
        numeric_columns.append(column)
print(numeric_columns)
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Long Luu](https://stackoverflow.com/users/11235205)** (2023-04-02): @Adrian you should move your comment to here. Btw, you can read only the first row via the parameter `nrows`: `pd.read_csv('your_file.csv', nrows=1)`
- **[Adrian](https://stackoverflow.com/users/6176440)** (2023-04-03): Thank you, this code did the job too.
