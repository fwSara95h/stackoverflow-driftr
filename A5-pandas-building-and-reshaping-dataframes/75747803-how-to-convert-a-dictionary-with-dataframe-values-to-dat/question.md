---
title: "How to convert a dictionary with DataFrame values to DataFrame using Pandas"
site: stackoverflow
question_id: 75747803
url: https://stackoverflow.com/q/75747803
asked: 2023-03-15T16:53:11Z
asked_by: "Tutu"
asked_by_url: https://stackoverflow.com/users/8155393
last_edited: 2023-03-15T17:06:54Z
tags: [python, pandas, dataframe, dictionary]
score: 0
views_at_snapshot: 197
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bf3cb86ab3db56ee870274396f39a7d500e5f19870af676c361468301b87bbc9
---

# How to convert a dictionary with DataFrame values to DataFrame using Pandas

Asked by [Tutu](https://stackoverflow.com/users/8155393) on Stack Overflow, <https://stackoverflow.com/q/75747803>, 2023-03-15, last edited 2023-03-15. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I want to join data frames using *pandas*. 

I have several data frames. For example, two of them are:

df1=
```
           A      B      C
0    1    1.1    1.2    1.3
1    2    1.4    1.5    1.4
```
and df2=

```
           A      B      C
0    1    2.1    2.2    2.3
1    2    2.4    2.5    2.4
```
I would like to join them into 1 data frame like:

```
                  A      B      C
R1     0    1    1.1    1.2    1.3
       1    2    1.4    1.5    1.4
                  A      B      C
R2     0    1    2.1    2.2    2.3
       1    2    2.4    2.5    2.4
```
I tried to put them into a dictionary and convert them to the DataFrame like:
```
dict_val = {}
dict_val['R1'] = df1
dict_val['R2'] = df2
df_join = pd.DataFrame.from_dict(dict_val)
```
however, I am getting the following error:
**ValueError: Must pass 2-d input.**

How can I make this type of data frame?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[mozway](https://stackoverflow.com/users/16343464)** (2023-03-15): Try `df_join = pd.concat(dict)` (NB. Don't use `dict` as variable name, this is a python built-in)
- **[Michael Cao](https://stackoverflow.com/users/21021990)** (2023-03-15): Does this answer your question? [Concatenate a list of pandas dataframes together](https://stackoverflow.com/questions/32444138/concatenate-a-list-of-pandas-dataframes-together)
- **[Tutu](https://stackoverflow.com/users/8155393)** (2023-03-15): I am not using dict as a variable I forgot to change it here (I will modify it now). The variables aren't causing an issue
- **[Paul H](https://stackoverflow.com/users/1552748)** (2023-03-15): fyi -- you should read the docs of `pandas.DataFrame.from_dict()`. It doesn't expect a dictionary of already created data frames. In the "Getting Started" section of documentation, there's a header labeled "How do I combine data from multiple tables?". You should read that too.
- **[Tutu](https://stackoverflow.com/users/8155393)** (2023-03-15): @MichaelCao, I need to add an additional column to each data frame and then specify the indices. I wondered if there is any way to convert a dictionary with pandas.DataFrame as its values to another pandas.DataFrame?
- **[Tutu](https://stackoverflow.com/users/8155393)** (2023-03-15): @PaulH, thanks for the information. But they do not sure this example. I need to specify 'R1' and 'R2' (and so on) for each data frame I am joining
- **[Paul H](https://stackoverflow.com/users/1552748)** (2023-03-15): This example *is* demonstrated. Read more closely the examples about air quality that use the `key` argument
- **[mozway](https://stackoverflow.com/users/16343464)** (2023-03-15): Have you tested `concat` as I suggested?
