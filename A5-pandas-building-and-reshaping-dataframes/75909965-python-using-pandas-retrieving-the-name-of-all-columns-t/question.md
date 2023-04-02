---
title: "Python using Pandas - Retrieving the name of all columns that contain numbers"
site: stackoverflow
question_id: 75909965
url: https://stackoverflow.com/q/75909965
asked: 2023-04-02T03:23:03Z
asked_by: "Adrian"
asked_by_url: https://stackoverflow.com/users/6176440
last_edited: 2023-04-02T03:25:51Z
tags: [python, pandas, dataframe]
score: 2
views_at_snapshot: 504
answer_count: 5
accepted_answer_id: 75910288
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ee658623f78b329302071dcc8f7952a66a2bf5dfd8e47448ffeca25d710351b1
---

# Python using Pandas - Retrieving the name of all columns that contain numbers

Asked by [Adrian](https://stackoverflow.com/users/6176440) on Stack Overflow, <https://stackoverflow.com/q/75909965>, 2023-04-02, last edited 2023-04-02. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I searched for a solution on the site, but I couldn't find anything relevant, only outdated code. I am new to the Pandas library and I have the following `dataframe` as an example:

|      A      |     B    |     C    |     D    |     E    |
|-------------|----------|----------|----------|----------|
|          142|       0.4|       red|       108|     front|
|          164|       1.3|     green|        98|      rear|
|           71|      -1.0|      blue|       234|     front|
|          109|       0.2|     black|       120|     front|

I would like to extract the name of the columns that contain numbers (integers and floats). It is completely fine to use the first row to achieve this.
So the result should look like this: `['A', 'B', 'D']`

I tried the following command to get some of the columns that contained numbers:

    dataframe.loc[0, dataframe.dtypes == 'int64']
    
    Out:
    A 142
    D 108

There are two problems with this. First of all, I just need the name of the columns, but not the values. Second, this captures only the integer columns. My next attempt just gave an error:

    dataframe.loc[0, dataframe.dtypes == 'int64' or dataframe.dtypes == 'float64']

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Marcelo Paco](https://stackoverflow.com/users/11286032)** (2023-04-02): Does this answer your question? [How to determine whether a column/variable is numeric or not in Pandas/NumPy?](https://stackoverflow.com/questions/19900202/how-to-determine-whether-a-column-variable-is-numeric-or-not-in-pandas-numpy)
- **[Long Luu](https://stackoverflow.com/users/11235205)** (2023-04-02): It should be `dataframe.loc[0, (dataframe.dtypes == 'int64') | (dataframe.dtypes == 'float64')]`. I don't know why [pandas uses these characters though](https://stackoverflow.com/a/54358361/11235205)
- **[Long Luu](https://stackoverflow.com/users/11235205)** (2023-04-02): But Marcelo answer is the better way though
- **[Adrian](https://stackoverflow.com/users/6176440)** (2023-04-02): @MarceloPaco It is one step closer to the solution, but I still don't get the name of the columns that contain numeric values.
- **[Adrian](https://stackoverflow.com/users/6176440)** (2023-04-02): @Minh-LongLuu Your code did work! However, I still need to retrieve just the column names without any data.
- **[Long Luu](https://stackoverflow.com/users/11235205)** (2023-04-02): @Adrian you should move your comment to here. Btw, you can read only the first row via the parameter nrows: pd.read_csv('your_file.csv', nrows=1)
