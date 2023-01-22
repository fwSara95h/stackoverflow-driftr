---
title: "Descending count with iteration - Python"
site: stackoverflow
question_id: 75199648
answer_id: 75199849
url: https://stackoverflow.com/a/75199849
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-22T10:59:34Z
last_edited: 2023-01-22T11:05:01Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75199849/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 0abd440d8146e07149255c64094ad3ffe27681efb66bc6cd87104664e0d1c97b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75199849>, 2023-01-22, last edited 2023-01-22; score 0. Text as retrieved 2026-10-12.

If you start with 30 `0`s, you should end with 0 `30`s [i.e., at 1 `29`],

```python
# for i in range(a): print(','.join([f'{i}']*(a-i))) # OR
for i in range(a): print(*[i]*(a-i), sep=',')
```

You can end at 1 `30` if you start with 31 `0`s [ [output screenshot][2] ]

```python
for i in range(a+1): print(*[i]*(a-i+1), sep=',')
```

---

If you to save it as an object

```python
{f"{(a-i)} {i}'s": tuple([i]*(a-i)) for i in range(a)}
```

would return a dictionary of tuples

```python
{
   "30 0's":  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
   "29 1's":  (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
   "28 2's":  (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2),
   "27 3's":  (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3),
   "26 4's":  (4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4),
   "25 5's":  (5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
   "24 6's":  (6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6),
   "23 7's":  (7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7),
   "22 8's":  (8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8),
   "21 9's":  (9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9),
   "20 10's":  (10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
   "19 11's":  (11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11),
   "18 12's":  (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12),
   "17 13's":  (13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13),
   "16 14's":  (14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14),
   "15 15's":  (15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15),
   "14 16's":  (16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16),
   "13 17's":  (17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17),
   "12 18's":  (18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18),
   "11 19's":  (19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19),
   "10 20's":  (20, 20, 20, 20, 20, 20, 20, 20, 20, 20),
   "9 21's":  (21, 21, 21, 21, 21, 21, 21, 21, 21),
   "8 22's":  (22, 22, 22, 22, 22, 22, 22, 22),
   "7 23's":  (23, 23, 23, 23, 23, 23, 23),
   "6 24's":  (24, 24, 24, 24, 24, 24),
   "5 25's":  (25, 25, 25, 25, 25),
   "4 26's":  (26, 26, 26, 26),
   "3 27's":  (27, 27, 27),
   "2 28's":  (28, 28),
   "1 29's":  (29)
}
```


  [2]: https://i.sstatic.net/W6ODt.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[TF7](https://stackoverflow.com/users/21000447)** (2023-01-22): how can I store the list of numbers (30 0s, 29 1s ecc..) in a simple list?
- **me** (2023-01-22): Just **`[[i]*(a-i) for i in range(a)]`** or *`list({...}.values())`*
