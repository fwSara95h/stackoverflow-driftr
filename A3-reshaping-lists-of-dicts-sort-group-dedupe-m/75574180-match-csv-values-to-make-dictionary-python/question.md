---
title: "Match CSV Values to Make Dictionary Python"
site: stackoverflow
question_id: 75574180
url: https://stackoverflow.com/q/75574180
asked: 2023-02-26T18:31:02Z
asked_by: "Domenic Urso"
asked_by_url: https://stackoverflow.com/users/20617790
last_edited: 2023-02-26T18:50:00Z
last_editor: "Mark Tolonen"
last_editor_url: https://stackoverflow.com/users/235698
tags: [python, csv, dictionary]
score: -1
views_at_snapshot: 71
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3837540f327f843e4c037a22d3698f43396c5863192ced5bde602481a42aa55c
---

# Match CSV Values to Make Dictionary Python

Asked by [Domenic Urso](https://stackoverflow.com/users/20617790) on Stack Overflow, <https://stackoverflow.com/q/75574180>, 2023-02-26, last edited 2023-02-26 by [Mark Tolonen](https://stackoverflow.com/users/235698). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I've been trying to make an auto-correct and -complete program and trying to make it more useful using a frequency algorithm using CSV, but am pretty new to using CSV files. I'm trying to create a dictionary from a CSV file that I can then use to determine the top results. 

The CSV file contains of 1/3 of a million lines, sorted from highest frequency to lowest. It starts with the two item categories, "word" and "count", followed by 333,333 lines.
```
word,count
the,23135851162
of,13151942776
and,12997637966
to,12136980858
a,9081174698
in,8469404971
for,5933321709
is,4705743816
on,3750423199
```
Using the file, which can be found [here](https://www.kaggle.com/datasets/rtatman/english-word-frequency), I am trying to create a dictionary like so:
```python
{"the":23135851162, "of":13151942776, "and":12997637966, "to":12136980858, etc.}
```
I've tried using the following script using the pandas library like so,
```python
import pandas as pd
data = pd.read_csv("./unigram_freq.csv")
wordFreq = {col: list(data[col]) for col in data.columns}
```
but end up with a dictionary output that looks something like the following.
```python
{'word': ['the', 'of', 'and', 'to', etc.], 'count':[23135851162, 13151942776, 12997637966, 12136980858, etc.]}

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[ARK1375](https://stackoverflow.com/users/12976010)** (2023-02-26): Hi, Can you update me a little on what you are trying to do next with your data? Converting CSV to Dict format is easy enough and I can walk you through the process. However I have a feeling the Pandas (as you guessed already) will be a more suitable option for you.
- **me** (2023-02-26): try just `wordFreq = dict(zip(data['word'], data['count']))`
- **[Domenic Urso](https://stackoverflow.com/users/20617790)** (2023-02-26): @ARK1375 I am planning on taking an incomplete or incorrect word and returning the three best suitable answers. The frequency will help to suggest more oftenly used words instead of returning words like "aaa" just because it is the third word when sorted alphabetically.
- **[Mark Tolonen](https://stackoverflow.com/users/235698)** (2023-02-26): Don't put the solution in the question.  You can answer your own question below.
