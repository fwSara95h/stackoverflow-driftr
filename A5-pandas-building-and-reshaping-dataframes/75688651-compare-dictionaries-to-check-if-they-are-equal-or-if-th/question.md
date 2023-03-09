---
title: "Compare dictionaries to check if they are equal or if they go from empty to having a value"
site: stackoverflow
question_id: 75688651
url: https://stackoverflow.com/q/75688651
asked: 2023-03-09T18:26:02Z
asked_by: "Angie"
asked_by_url: https://stackoverflow.com/users/12981397
last_edited: 2023-03-09T18:44:18Z
tags: [python, pandas, dataframe, dictionary, comparison]
score: 0
views_at_snapshot: 550
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a1fe4a73e356b5278e656176b15fa5e980bf0edcf02be1630db51a7d62367053
---

# Compare dictionaries to check if they are equal or if they go from empty to having a value

Asked by [Angie](https://stackoverflow.com/users/12981397) on Stack Overflow, <https://stackoverflow.com/q/75688651>, 2023-03-09, last edited 2023-03-09. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have two dataframes where I am looping through each row and creating a dictionary for the rows that I am looking at to compare against each other.

I've done this by doing:

```
ids = []
for row in range(len(df1)-1):
    df1_row = dict(df1.iloc[row])
    df2_row = dict(df2.iloc[row])
    if df1_row == df2_row:
        ids.append(df1_row['ID'])

```
I am checking whether the two rows I am comparing at a time are equal and if they are I am appending the id from that row to a list to return at the end. 

However I would also like to check the condition where if the row from df2 contains an empty string for a given key and the row from df1 contains a value for that same key, but the rest of the key-value pairs are equal between them, then I want to append that id to the list as well.

For example if I am looking at two rows like this
```
df1_row = {'NAME': 'Kelly', 'AGE': '15', 'CITY': 'London', 'GENDER': 'F', 'ID': 15}
df2_row = {'NAME': 'Kelly', 'AGE': '15', 'CITY': '', 'GENDER': 'F', 'ID': '15'}
```
Then I would like to append ID 15 to my list since CITY goes from EMPTY in df2_row to having a value in df1_row.

If the pair looked like this
```
df1_row = {'NAME': 'Kelly', 'AGE': '15', 'CITY': 'London', 'GENDER':''  'ID': 15}
df2_row = {'NAME': 'Kelly', 'AGE': '15', 'CITY': '', 'GENDER': 'F', 'ID': '15'}
```
I would not want to append id 15 to my resulting list since even though though CITY goes from EMPTY to having a value from df2_row to df1_row, GENDER goes form having a value to EMPTY from df2 to df1.

(Basically my checks are: the rows are exactly equal OR they have values that go from empty to non-empty (from df2 to df1) and the rest of the values are equal)

I tried doing 

```
ids = []
for row in range(len(df1)-1):
    df1_row = dict(df1.iloc[row])
    df2_row = dict(df2.iloc[row])
    if df1_row == df2_row:
        ids.append(df1_row['ID'])
    else:
        for key in df1_row:
            if df1_row[key] == df2_row[key] or (df2_row[key] == '' and df1_row[key] != ''):

```
But I am not sure how to write the second condition so that it only appends the id after the whole row has been checked, rather than just check the condition on the current key-value and append the id right there...is there a way to check this condition for the entire row at once/another way to write this? Thanks! (or maybe there is just a better way to compare two rows in a dataframe for the same id against each other using these conditions without having to turn the rows into dictionaries to compare?)

TEST TABLES

DF1:

|     NAME   | AGE |CITY|GENDER|ID|
|----------|-----|------|----|---|
|Kelly  |       15    | London|F|15|
|  Jack    |     12   | |M| 98|
|          Josh         |     30  |Austin|M| 12|

DF2:

|     NAME   | AGE |CITY|GENDER|ID|
|----------|------------------|------|----|---|
|         Kelly         |       15 |   |F|15|
|          Jack         |     | Munich|M| 98|
|          Josh         |     30  |Austin|M| 12|


I would want to get back IDs 15 and 12 because 12 matches exactly, and in 15 it matches exactly or it has a column value in df2 that goes to non empty in df1.

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[RomanPerekhrest](https://stackoverflow.com/users/3185459)** (2023-03-09): post a testable sample dataframes
- **[Angie](https://stackoverflow.com/users/12981397)** (2023-03-09): posted two test dataframes
- **[wwii](https://stackoverflow.com/users/2823755)** (2023-03-09): `has a column value in df2 that goes to non empty in df1` - any **single** column? If there are 2 empty columns in df2 but both have values in df1 does it meet your requirement? Why did you choose to turn each row into a dict first? [Series are dict-like](https://pandas.pydata.org/docs/user_guide/dsintro.html#series-is-dict-like). Are the missing values empty strings or null or nan?
- **[Angie](https://stackoverflow.com/users/12981397)** (2023-03-09): If any of the columns if df2 are empty and go to non-empty in df1 AND the other columns match on values that meets my requirement (so yes to if there are two empty column in df2 but they have values in df1), my case where i would not want to retain this id is if there is at least one column that goes from non-empty in df2 to empty in df1 (even with other values matching) OR  the rows all have values but do not match at all
- **[Angie](https://stackoverflow.com/users/12981397)** (2023-03-09): The missing values are empty strings. I turned it into dictionaries because that was the only way I could think to compare the rows, so was not sure if there was a better method to achieve this
- **[Alias Cartellano](https://stackoverflow.com/users/16653700)** (2023-03-09): `isnull()` may be able to determine if the values changed to non-null between dataframes. After you have determined the value has changed to non-null then iterate the row to determine if the other values have changed. If the values have not changed then append the id, otherwise continue to the next row.
