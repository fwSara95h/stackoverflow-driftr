---
title: "How to tag a row if at least one column is greater than a specific value"
site: stackoverflow
question_id: 75897954
url: https://stackoverflow.com/q/75897954
asked: 2023-03-31T11:21:39Z
asked_by: "Chinthana"
asked_by_url: https://stackoverflow.com/users/4684030
last_edited: 2023-03-31T11:31:40Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, pandas]
score: 0
views_at_snapshot: 49
answer_count: 3
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 41b619d3268b6e616482a6f171764e7f73d17450160f20129ba43ca21872c44c
---

# How to tag a row if at least one column is greater than a specific value

Asked by [Chinthana](https://stackoverflow.com/users/4684030) on Stack Overflow, <https://stackoverflow.com/q/75897954>, 2023-03-31, last edited 2023-03-31 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a pandas DataFrame as follows;

| Unique ID | Value_1 |Value 2  |Value 3|
| -------- | -------- |-------- |-------|
| 111      | 10       |50       |  18   |
| 222      | 5        | 8       |  2    |
|333       | 12       | 3       |  5    |

I want a new column in the pandas data frame and create a tag (1) , if at least one of columns from `Value_1` to `Value_3` is greater than 10.

The output desired as follows;

| Unique ID | Value_1 |Value 2  |Value 3|Column_tag|
| -------- | -------- |-------- |-------|--------- |
| 111      | 10       |50       |  18   |1         |
| 222      | 5        | 8       |  2    |0         |
|333       | 12       | 3       |  5    |1         |




I tried following code which resulted an error:

```py
def flag_df_new(df):
    
    if (df[df.columns[2:]]>10).any(axis=1):
        return 1
    else:
        return 0
    
customer_summary_1['Flag'] = customer_summary_1.apply(flag_df_new, axis = 1)
```

The result I am getting:

> ```
> AttributeError: 'Series' object has no attribute 'columns'
> ```
