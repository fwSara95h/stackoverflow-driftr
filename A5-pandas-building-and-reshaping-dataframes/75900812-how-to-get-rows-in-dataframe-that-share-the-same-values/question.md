---
title: "How to get rows in dataframe that share the same values"
site: stackoverflow
question_id: 75900812
url: https://stackoverflow.com/q/75900812
asked: 2023-03-31T16:32:29Z
asked_by: "denisRei"
asked_by_url: https://stackoverflow.com/users/17482514
last_edited: never
tags: [python, pandas, group-by]
score: 0
views_at_snapshot: 1211
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 6ea43acd40f2af3a93127846efb630c0b5c016255b38ca447713b9037cba4021
---

# How to get rows in dataframe that share the same values

Asked by [denisRei](https://stackoverflow.com/users/17482514) on Stack Overflow, <https://stackoverflow.com/q/75900812>, 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a python-pandas df that looks like this (image shows head of df):

[![enter image description here](https://i.sstatic.net/fMINn.png)](https://i.sstatic.net/fMINn.png)

As you can see for index 265 and index 743 the columns 'symbol', 'date' and 'hour' are equal.
The only difference is the group.
I want to know how often this happens, to be exact how often group 'BPG' has matching events with other groups (in this case matching event with 'BPF').
How can I count those events?



I tried grouping the df with
`test_df.groupby(["symbol", "date", "hour", "group"]).count()` receiving this:

[![enter image description here](https://i.sstatic.net/PkzmK.png)](https://i.sstatic.net/PkzmK.png)

But how can I access the matches now? For example turning the last column now into a list of lists, where every list included holds all 'group'-values where the columns 'symbol', 'date' and 'hour' are equal would be helpful.

I.e. turning it into: `[["BPG"]["BPG"]["MPG"]["BPF", "BPG"]]`


Thanks for the help!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-04-01): (Can you please include a snippet of whatever `test_df.to_dict('split')` returns so that I can reproduce `test_df`? Use [`.sample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html) or `.iloc` to reduce the rows if its a very large DataFrame....) Anyway, you can probably use some combination of `groupby` (but maybe list  `group` at the **start** instead of end) and [`.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html) and/or maybe [`.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)
- **[user19077881](https://stackoverflow.com/users/19077881)** (2023-04-01): Images of data are difficult to use to demonstrate a solution You should make it easier for responders by providing a minimal example as above but in usable (code) form..
- **[denisRei](https://stackoverflow.com/users/17482514)** (2023-04-01): Thanks for the tip @Driftr95 to reproduce the dataset you can find it here: https://github.com/SystemsLab-Sapienza/pump-and-dump-dataset (I work with the pump_telegram.csv). As said I am trying to find out which groups often publish the same symbol together. I did find an ugly and unclean way in python but I'm wondering what the solution in pandas would look like.
- **[denisRei](https://stackoverflow.com/users/17482514)** (2023-04-01): Thank you for this tip @user19077881 ! I am new to posing questions so I will try and fix this.
