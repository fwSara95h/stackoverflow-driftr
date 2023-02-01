---
title: "How do I extract the values of the innermost dictionary of a 3-level dictionary and save those values in a Pandas DataFrame?"
site: stackoverflow
question_id: 75310830
url: https://stackoverflow.com/q/75310830
asked: 2023-02-01T13:23:24Z
asked_by: "Sujai Banerji"
asked_by_url: https://stackoverflow.com/users/6788265
last_edited: never
tags: [python, pandas, dataframe, dictionary, nested]
score: 0
views_at_snapshot: 83
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 451cb9282e9144bab1ea8281a1c27a8b36edee10b4787c9bd5d5803b113cec86
---

# How do I extract the values of the innermost dictionary of a 3-level dictionary and save those values in a Pandas DataFrame?

Asked by [Sujai Banerji](https://stackoverflow.com/users/6788265) on Stack Overflow, <https://stackoverflow.com/q/75310830>, 2023-02-01. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a 3-level nested dictionary whose structure is as follows:

Dictionary 1:
Keys: 1, 2, 3, 4. 1 stands for winter, 2 for spring, 3 for summer and 4 for autumn season.

Dictionary 2.
Keys: Years from 2005 to 2018.

Dictionary 3.
Keys:0 to 24. 0 to 24 for hourly average. Every key has values pertaining to the hourly average for that year of that season.

I am posting pictures of the 3 dictionaries as well.

I am a beginner in Python and so far I have tried the code below, but it is not giving me the desired ouput.

    df = pd.DataFrame.from_dict({(i, j, k): pm_10_abs_season[i][j][k] for i in pm_10_abs_season.keys() for j in pm_10_abs_season[i].keys() for k in pm_10_abs_season[i][j]}, orient = 'index')



[![enter image description here][1]][1] 


The output I am getting looks like this:

[![enter image description here][2]][2]


  [1]: https://i.sstatic.net/GX0lb.png
  [2]: https://i.sstatic.net/eJu9H.png

I want to save the data in four Pandas DataFrames. One for each season. Then, I want to save the data in the following format:

Columns: Hour 0, Hour 1, Hour 3, ..., Hour 23

Rows: 2005, 2006, 2007, ..., 2018

So, the structure of the Pandas DataFrame would something like the following:

    Year|Hour 0|Hour 1|Hour 2|...|Hour 23
    -------------------------------------
    2005|
    2005|
    2005|
    ... |
    2018|

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mozway](https://stackoverflow.com/users/16343464)** (2023-02-01): Please provide minimal reproducible inputs, not images and only a reasonable number of rows. Also provide the matching expected output
