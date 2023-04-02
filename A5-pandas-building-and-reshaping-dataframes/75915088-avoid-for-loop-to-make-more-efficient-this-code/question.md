---
title: "Avoid for loop to make more efficient this code"
site: stackoverflow
question_id: 75915088
url: https://stackoverflow.com/q/75915088
asked: 2023-04-02T23:14:10Z
asked_by: "AM27"
asked_by_url: https://stackoverflow.com/users/21551448
last_edited: 2023-04-03T00:21:44Z
last_editor: "Ynjxsjmh"
last_editor_url: https://stackoverflow.com/users/10315163
tags: [pandas, dataframe, performance, for-loop, multi-index]
score: 1
views_at_snapshot: 79
answer_count: 1
accepted_answer_id: 75920208
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3d17c274e1dcd0a2cc5520907d47adf152e0d1050f4981f5511e9450634e75c4
---

# Avoid for loop to make more efficient this code

Asked by [AM27](https://stackoverflow.com/users/21551448) on Stack Overflow, <https://stackoverflow.com/q/75915088>, 2023-04-02, last edited 2023-04-03 by [Ynjxsjmh](https://stackoverflow.com/users/10315163). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a big data frame and I need to apply a double if condition to each cell of it.
My code works but it is really slow. I would like to have a code that is more efficient.

di, dm and dmm are data frame with multi index column
dm is the rolling median of the data frame so it has the first 60 values = 0
dmm is a linear transformation of dm so it also has the first 60 values = 0
di, dm and dmm have all the same size, the same index and the same columns name 
the data frame you see above is a copy of one similar taken from another question
my has 2520 rows x 4015 columns, the first level column index contains 803 columns each key so, the first level column index has 5 category, each category has 803 columns that in total are 4015.

I need to apply this formula for each cell of di:

```
𝑑𝑖 = dm + 5dmm if 𝑑𝑖 >= dm + 5dmm or
𝑑𝑖 = dm - 5dmm if 𝑑𝑖 <= dm - 5dmm
```

this is my code:

    for i in range(len(di)):
        for j in range(len(di.columns)):
            if di.iloc[i,j] >= dm.iloc[i,j] + 5 * dmm.iloc[i,j]:
                di.iloc[i,j] = dm.iloc[i,j] + 5 * dmm.iloc[i,j]
            elif di.iloc[i,j] <= dm.iloc[i,j] - 5 * dmm.iloc[i,j]:
                di.iloc[i,j] = dm.iloc[i,j] - 5 * dmm.iloc[i,j]`

in this data frame the first level column index has two classes, each class contains 3 columns 

```
                 JAN                 Feb            
                PRICE AMOUNT NAME   PRICE AMOUNT NAME
     2011-03-31     2      7    3       6      0    5
     2011-04-01     6      2    5       0      4    2
     2011-04-04     9      0    7       2      7    9
     2011-04-05     5      3    5       7      9    9
```

This is a simil-image of the data frame

![](https://i.sstatic.net/sBPX0.jpg)

Thank you in advice
