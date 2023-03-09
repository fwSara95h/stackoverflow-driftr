---
title: "Set variable column values to nan based on row condition"
site: stackoverflow
question_id: 75680488
url: https://stackoverflow.com/q/75680488
asked: 2023-03-09T04:38:29Z
asked_by: "thefrollickingnerd"
asked_by_url: https://stackoverflow.com/users/10339757
last_edited: 2023-03-09T05:26:05Z
last_editor: "rajendra"
last_editor_url: https://stackoverflow.com/users/2105924
tags: [python, python-3.x, pandas, slice]
score: 2
views_at_snapshot: 107
answer_count: 4
accepted_answer_id: 75680750
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c18fd9427cd8f1040d779a43a5cba662b733c65b8c70f5ba9b48d3d9e87edbc0
---

# Set variable column values to nan based on row condition

Asked by [thefrollickingnerd](https://stackoverflow.com/users/10339757) on Stack Overflow, <https://stackoverflow.com/q/75680488>, 2023-03-09, last edited 2023-03-09 by [rajendra](https://stackoverflow.com/users/2105924). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to be able to variably change a column value based on the value of the first column.

Say I have a dataframe as follows:
```
col_ind   col_1   col_2   col_3
    3       a       b       c
    2       d       e       f
    1       g       h       i  
```
I effectively want to do 
```
df.loc[:, df.columns[-df['col_ind']:]] = np.nan
```
Which would result in:
```
col_ind   col_1   col_2   col_3
    3      nan     nan     nan
    2       d      nan     nan
    1       g       h      nan 
```
