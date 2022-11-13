---
title: "Parse html tables from emails to lists then convert to pandas dataframe"
site: stackoverflow
question_id: 74407902
answer_id: 74421202
url: https://stackoverflow.com/a/74421202
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-13T12:58:14Z
last_edited: 2022-11-16T02:56:25Z
revisions: 4
revision_history: https://stackoverflow.com/posts/74421202/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 4987bcdfc859498c05d52f792bb569f9c7a327f49d940a0246d901a0fe0912b2
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74421202>, 2022-11-13, last edited 2022-11-16; **accepted**; score 1. Text as retrieved 2026-10-12.

If you had a list of dataframes (`df`) that looked like 
```python
[         0        1
 0  Column1  Value1a
 1  Column2  Value2a
 2  Column3  Value3a
 3  Column4  Value4a
 4  Column5  Value5a
 5  Column6  Value6a
 6  Column7  Value7a
 7  Column8  Value8a,
          0        1
 0  Column1  Value1b
 1  Column2  Value2b
 2  Column3  Value3b
 3  Column4  Value4b
 4  Column5  Value5b
 5  Column6  Value6b
 6  Column7  Value7b
 7  Column8  Value8b,
          0        1
 0  Column1  Value1c
 1  Column2  Value2c
 2  Column3  Value3c
 3  Column4  Value4c
 4  Column5  Value5c
 5  Column6  Value6c
 6  Column7  Value7c
 7  Column8  Value8c]
```
then **`pd.concat([d.set_index(d.columns[0]) for d in df], axis='columns', ignore_index=True).T`** would return a single Dataframe

|index|Column1|Column2|Column3|Column4|Column5|Column6|Column7|Column8|
|---|---|---|---|---|---|---|---|---|
|0|Value1a|Value2a|Value3a|Value4a|Value5a|Value6a|Value7a|Value8a|
|1|Value1b|Value2b|Value3b|Value4b|Value5b|Value6b|Value7b|Value8b|
|2|Value1c|Value2c|Value3c|Value4c|Value5c|Value6c|Value7c|Value8c|

---

But if `df` was instead oriented as
```python
[         0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1a  Value2a  Value3a  Value4a  Value5a  Value6a  Value7a  Value8a,
          0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1b  Value2b  Value3b  Value4b  Value5b  Value6b  Value7b  Value8b,
          0        1        2        3        4        5        6        7
 0  Column1  Column2  Column3  Column4  Column5  Column6  Column7  Column8
 1  Value1c  Value2c  Value3c  Value4c  Value5c  Value6c  Value7c  Value8c]
```
then 
```python
pd.concat([d.rename(columns=d.iloc[0]).drop(d.index[0]) for d in df], ignore_index=True)
```
would return the same combined DataFrame.

---

If you leave out `ignore_index=True` then the rows will have the same indexes from before combining; i.e., 1,1,1 instead of 0,1,2.

---
---

**ADDED EDIT:**

If you just want the tables from each message in one combined Dataframe, this should do:
```python
pd.concat([mdf.set_index(mdf.columns[0]) for mdf in [
    (pd.read_html(str(mtable))[0] if mtable else None) for mtable in 
    [BeautifulSoup(m.HTMLBody, "lxml").find('table') for m in Mail_Messages] 
] if mdf is not None], axis='columns', ignore_index=True).T
``` 
|[![SampleOp][1]][1]|
|:-:|

---

but if you want/need the loop for anything else, then you can also do 
```python
output = []
for mail in Mail_Messages:
    html_tables = BeautifulSoup(mail.HTMLBody, "lxml").find('table')
    
    # read html table to dataframe list
    df = pd.read_html(str(html_tables))[0]
    output.append(df.set_index(df.columns[0]))

    ## WHATEVER ELSE YOU NEED TO DO IN THE LOOP ##

output = pd.concat(output, axis='columns', ignore_index=True).T
print(output)
```

and that should print something like 
```lang-none
0 Column1 Column2 Column3 Column4 Column5 Column6 Column7 Column8
0  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8
1  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8
2  Value1  Value2  Value3  Value4  Value5  Value6  Value7  Value8
``` 


  [1]: https://i.sstatic.net/ev7Ky.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-13): if i add  pd.concat([d.set_index(0) for d in df], axis='columns', ignore_index=True).T  i recieve this error  AttributeError: 'int' object has no attribute 'set_index'
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-13): where would I add your suggestion to the current code? I do apologize , i'm a total newbie
- **me** (2022-11-13): @Dante you should add it at whichever point in your code `df` is in the format described in the answer (I assumed it was right after `df = pd.read_html(str(html_tables))` but I can't be sure without seeing a sample of `html_tables`). And as for the error, are you using `d` as a variable name for something already? Or maybe I'm mistaken about your original df's column names [it's safer to use `d.set_index(d.columns[0])` anyway - I've edited my answer].
- **me** (2022-11-13): @Dante If the edited version doesn't work when added right after `read_html` line and you do already have a variable `d` try changing `d` [all instances in *my* code only] to some other name you're not using yet (I think that's unlikely to be the reason, but it's worth a try....). If it still doesn't work I would need a sample of `html_tables` to check what's causing the issue
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-13): Thanks for all your help .. I've added a screen shot of the table im trying to grab from each email..  obviously i've changed the data in the table ,  but thats the table structure..
- **me** (2022-11-14): @Dante I need the **HTML** of the table actually (could you print `html_tables`?), but arranged the way it is, `pd.concat([d.set_index(d.columns[0]) for d in pd.read_html(str(html_tables))], axis='columns', ignore_index=True).T` *should* work...it's still not working?
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-14): i've posted the html from the email the table ,  again i appreciate your time in helping me..
- **me** (2022-11-15): @Dante it *should* work - I pasted your html and ran that line and got [**this** output](https://i.sstatic.net/v14n8.png) . So, the only reason I can think of for `AttributeError` is - are you *sure* you don't already have a variable called `d`? (although even then, it shouldn't be an issue.... still, try changing to something like **`pd.concat([tdf.set_index(tdf.columns[0]) for tdf in pd.read_html(str(body))], axis='columns', ignore_index=True).T`** and see if you still get the error)
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-15): ok i got rid of the error, but i still cannot get the lists into the dataframe as you have demonstrated.   i've added what the output i receive with and without your line of code.
- **me** (2022-11-16): @Dante I didn't realize you were tying to combine tables from different emails/htmls - in which case, you would need to `concat` **outside** the loop. Please see my added edit
- **[Dante](https://stackoverflow.com/users/20191122)** (2022-11-16): yes this is exactly what i was trying to achieve ...  Thank you so much , i really appreciate the time you've taken to help me...   One last question ,  how could i now get the dataframe into a excel / csv file from with your code example ?
- **me** (2022-11-16): @Dante you can use [`.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) [ or [`ExcelWriter`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter) +  [`.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel) ]
