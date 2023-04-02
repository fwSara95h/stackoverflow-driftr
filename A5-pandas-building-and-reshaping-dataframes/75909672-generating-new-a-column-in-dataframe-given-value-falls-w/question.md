---
title: "Generating new a column in dataframe given value falls within a certain range of another column value"
site: stackoverflow
question_id: 75909672
url: https://stackoverflow.com/q/75909672
asked: 2023-04-02T01:22:27Z
asked_by: "newbzzs"
asked_by_url: https://stackoverflow.com/users/16922748
last_edited: never
tags: [python, pandas, dataframe]
score: 1
views_at_snapshot: 67
answer_count: 2
accepted_answer_id: 75909747
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a619f68a980c46801fdcaf6b676d9efc576bb684c8d3a97eb6b6d3edca67d757
---

# Generating new a column in dataframe given value falls within a certain range of another column value

Asked by [newbzzs](https://stackoverflow.com/users/16922748) on Stack Overflow, <https://stackoverflow.com/q/75909672>, 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Given the following dataframe:
```
df = pd.DataFrame({'A':[random.randrange(0, 9, 1) for i in range(10000000)],
                   'B':[random.randrange(0, 9, 1) for i in range(10000000)]})
```
That may look like this:
```
    A	B
0	8	3
1	3	0
2	8	4
3	6	5
4	8	2
...
```
I'd like to generate a new column called Eq. This column confirms if A and B row values fall within a certain range. If so, the number 1 is appended, if not 0 is appended.

If the range is 2 the result should look like this:
```
    A	B   Eq
0	8	3    0
1	3	0    0
2	8	4    0
3	6	5    1
4	8	2    0
...
```
```
Essentially:
8 does NOT fall in range of (3-2,3+2)
3 does NOT fall in range of (0-2,0+2)
6 DOES fall in range of (5-2,5+2)
```

In my first attempt, I wrote a simple function to apply to each row of the df.

```
def CountingMatches(row, range_limit):
    if row['A'] in range (-range_limit + row['B'], range_limit+row['B']):
        return 1
    else:
        return 0
```
```
df['Eq'] = df.apply(CountingMatches, axis=1, range_limit=3)
```
This worked but took an incredibly long time, so kinda useless.

I then used my function with swifter https://towardsdatascience.com/speed-up-your-pandas-processing-with-swifter-6aa314600a13 

```
df['Eq'] = df.swifter.apply(CountingMatches, axis=1, range_limit=3)
```

This also took a really long time.

I then checked how long it would take to check if the columns matched, no range.
```
df['Eq'] = (df['A'].astype(int) == df['B'].astype(int)).astype(int)
```
This was incredibly fast ~ 1s.

Given this hopeful result, I tried to incorporate the ranges.

```
range_limit=2
df['Eq'] = (df['A'].astype(int) in range(df['B'].astype(int)-range_limit,df['B'].astype(int) + range_limit)).astype(int)
```
But I get the following error, rightfully so:
```
'Series' object cannot be interpreted as an integer
```

How can I efficiently complete this task on this dataframe?
