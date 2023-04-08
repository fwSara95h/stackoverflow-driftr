---
title: "Use Python to calculate difference between date in current row and date in previous row and previous column"
site: stackoverflow
question_id: 75962581
answer_id: 75962808
url: https://stackoverflow.com/a/75962808
author: "Laurent B."
author_url: https://stackoverflow.com/users/13460543
posted: 2023-04-08T00:59:37Z
last_edited: 2023-04-08T03:49:37Z
accepted: false
score: 2
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 05b4bbae7094b4dd9402682e3e92bb9525e25321aca92063ec13d7b2471b6d8a
role: another answer on the same question, kept as context; not my work
---

# Answer by [Laurent B.](https://stackoverflow.com/users/13460543) — 2023-04-08

Posted on Stack Overflow, <https://stackoverflow.com/a/75962808>, 2023-04-08, last edited 2023-04-08. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I took into account Mozway comment, so I propose you instead the following code (I didn't see you want it by kiosk) :

```python
df['Online'] = pd.to_datetime(df['Online'], infer_datetime_format=True)
df['Offline'] = pd.to_datetime(df['Offline'], infer_datetime_format=True)

df['Offsets'] = (df['Online'] - df.groupby('Kiosk')['Offline'].shift(1)).dt.days
print(df)
```
**Result**

```
    Kiosk     Online    Offline  Online Days Offsets
0       1 2022-12-01 2022-12-05            4     NaT
1       1 2022-12-07 2022-12-17           10  2 days
2       1 2022-12-20 2022-12-21            1  3 days
3       1 2022-12-24 2022-12-29            5  3 days
4       2 2022-11-15 2022-11-30           15     NaT
5       2 2022-12-02 2022-12-07            5  2 days
6       2 2022-12-15 2022-12-25           10  8 days
7       3 2022-10-30 2022-11-15           16     NaT
8       3 2022-11-17 2022-11-22            5  2 days
9       3 2022-11-23 2022-11-30            7  1 days
10      3 2022-12-04 2022-12-15           11  4 days
11      3 2022-12-18 2022-12-20            2  3 days
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mozway](https://stackoverflow.com/users/16343464)** (2023-04-08): This is incorrect, you should use `groupby.shift` with a step of `1` (not `-1`). Then you can remove the `apply`.
- **[Laurent B.](https://stackoverflow.com/users/13460543)** (2023-04-08): Hi Mozway thank you for your vigilance, you are right
- **[mozway](https://stackoverflow.com/users/16343464)** (2023-04-08): It's still incorrect. You must use `groupby` to avoid any side effect. Let me write an answer to show it.
- **[mozway](https://stackoverflow.com/users/16343464)** (2023-04-08): We cross-posted, now it's correct. I'll delete my answer ;)
- **[mozway](https://stackoverflow.com/users/16343464)** (2023-04-08): Also OP wants the days so you can add `.dt.days`.
