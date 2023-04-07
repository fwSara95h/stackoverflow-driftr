---
title: "Use Python to calculate difference between date in current row and date in previous row and previous column"
site: stackoverflow
question_id: 75962581
url: https://stackoverflow.com/q/75962581
asked: 2023-04-07T23:27:58Z
asked_by: "the_zeef"
asked_by_url: https://stackoverflow.com/users/6266807
last_edited: 2023-04-08T21:07:01Z
last_editor: "Laurent B."
last_editor_url: https://stackoverflow.com/users/13460543
tags: [python, pandas, diff, calculation]
score: 2
views_at_snapshot: 845
answer_count: 2
accepted_answer_id: 75962918
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3265b633c4c6685f04a1e833e86edc7fa2c8d9cedd1951ad69d7b254fe5eee7b
---

# Use Python to calculate difference between date in current row and date in previous row and previous column

Asked by [the_zeef](https://stackoverflow.com/users/6266807) on Stack Overflow, <https://stackoverflow.com/q/75962581>, 2023-04-07, last edited 2023-04-08 by [Laurent B.](https://stackoverflow.com/users/13460543). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to calculate the difference between dates in different rows that are not in the same column. I have the following dataset:

| Kiosk | Online | Offline | Online Days |
| --- | --- | --- | --- |
| 1 | 12/1/2022 | 12/5/2022 | 4 |
| 1 | 12/7/2022 | 12/17/2022 | 10 |
| 1 | 12/20/2022 | 12/21/2022 | 1 |
| 1 | 12/24/2022 | 12/29/2022 | 5 |
| 2 | 11/15/2022 | 11/30/2022 | 15 |
| 2 | 12/2/2022 | 12/7/2022 | 5 |
| 2 | 12/15/2022 | 12/25/2022 | 10 |
| 3 | 10/30/2022 | 11/15/2022 | 16 |
| 3 | 11/17/2022 | 11/22/2022 | 5 |
| 3 | 11/23/2022 | 11/30/2022 | 7 |
| 3 | 12/4/2022 | 12/15/2022 | 11 |
| 3 | 12/18/2022 | 12/20/2022 | 2 |

I know I can use the diff function to calculate the difference between different rows in the same column, but I have not found a function that allows me to offset the row AND columns. In my example, I need to calculate the Offline Days as the difference between the Online date in my dataset and the Offline date in the previous row for the same Kiosk.

This is the output that I need in my output dataframe:

| Kiosk | Online | Offline | Online Days | Offline Days |
| --- | --- | --- | --- | --- |
| 1 | 12/1/2022 | 12/5/2022 | 4 | Nan |
| 1 | 12/7/2022 | 12/17/2022 | 10 | 2 |
| 1 | 12/20/2022 | 12/21/2022 | 1 | 3 |
| 1 | 12/24/2022 | 12/29/2022 | 5 | 3 |
| 2 | 11/15/2022 | 11/30/2022 | 15 | Nan |
| 2 | 12/2/2022 | 12/7/2022 | 5 | 2 |
| 2 | 12/15/2022 | 12/25/2022 | 10 | 8 |
| 3 | 10/30/2022 | 11/15/2022 | 16 | Nan |
| 3 | 11/17/2022 | 11/22/2022 | 5 | 2 |
| 3 | 11/23/2022 | 11/30/2022 | 7 | 1 |
| 3 | 12/4/2022 | 12/15/2022 | 11 | 4 |
| 3 | 12/18/2022 | 12/20/2022 | 2 | 3 |

**Dataframe to start with :**
```python
df=pd.DataFrame({'Kiosk':[1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3],
                 'Online':["12/1/2022", "12/7/2022","12/20/2022", "12/24/2022","11/15/2022", 
                           "12/2/2022","12/15/2022", "10/30/2022","11/17/2022", "11/23/2022",
                           "12/4/2022", "12/18/2022"],
                 'Offline':["12/5/2022", "12/17/2022","12/21/2022", "12/29/2022","11/30/2022", 
                            "12/7/2022","12/25/2022", "11/15/2022","11/22/2022", "11/30/2022",
                            "12/15/2022", "12/20/2022"],
                 'Online Days':[4, 10, 1, 5, 15, 5, 10, 16, 5, 7, 11, 2],
                 })
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Laurent B.](https://stackoverflow.com/users/13460543)** (2023-04-08): please give dataframe in the future ;-)
