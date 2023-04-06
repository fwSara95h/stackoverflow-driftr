---
title: "convert txt into dictionaries"
site: stackoverflow
question_id: 75947650
url: https://stackoverflow.com/q/75947650
asked: 2023-04-06T08:59:25Z
asked_by: "Lynn"
asked_by_url: https://stackoverflow.com/users/21579646
last_edited: 2023-04-06T10:54:39Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary]
score: -2
views_at_snapshot: 90
answer_count: 1
accepted_answer_id: 75949375
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 876198b75061076e4f3da4916615a484ceae610dcdd49e5c262a75081330ad5e
---

# convert txt into dictionaries

Asked by [Lynn](https://stackoverflow.com/users/21579646) on Stack Overflow, <https://stackoverflow.com/q/75947650>, 2023-04-06, last edited 2023-04-06 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a txt file has a header of 10 keys, with more than 1000 rows of both strings and numerics, and I want to read them and do some analyses in dictionay format. (I try some codes I can search, they will either said too many values to unpack, or not enough values to unpack. )

for instance the txt file could be like:

```lang-none
name age city job food ... address
Amy 26 London lawyer fish ... WE09KT
...
Lisa 30 LA teacher egg ... LY76SU
```


I want the output to be like a dictionary:

```py
[{name: Amy,age: 26,city: London,...}{name: Lisa, age: 30, ...}]
```


some ask me to visit [here][1], but the output will be *`{'name age city job ... address':['amy ... lisa','26 ... 30',...]}`* which is not what I want. (yes I don't even know what I even didn't get what the link shows: a return like *`{name:[Amy, ..., Lisa],age:[26,...,30],...}`*), could anybody also tell me the reason?



thanks for the help again, hope this clarify and could reach the answer!




  [1]: https://stackoverflow.com/questions/34010534/how-do-i-read-a-text-file-and-make-it-into-a-dictionary-in-python

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Frank Vel](https://stackoverflow.com/users/4000964)** (2023-04-06): You may want to read the Markdown Editing Help, particularly the one for [syntax highlighting](https://stackoverflow.com/editing-help#syntax-highlighting). The file format you are using is more commonly known as a CSV file. It's common to use the reverse of your current index notation, e.g string2.3 is row 2, column 3.
- **[user1763658](https://stackoverflow.com/users/1763658)** (2023-04-06): this question has been answered [here](https://stackoverflow.com/questions/34010534/how-do-i-read-a-text-file-and-make-it-into-a-dictionary-in-python)
- **[Frank Vel](https://stackoverflow.com/users/4000964)** (2023-04-06): Does this answer your question? [How do I read a text file and make it into a dictionary in Python?](https://stackoverflow.com/questions/34010534/how-do-i-read-a-text-file-and-make-it-into-a-dictionary-in-python)
- **[Lynn](https://stackoverflow.com/users/21579646)** (2023-04-06): i try this https://stackoverflow.com/questions/34010534/how-do-i-read-a-text-file-and-make-it-into-a-dictionary-in-python but the return is different from what they said. Mine will be {'key1 key2 ... key10':['string1.1 number2.1 ... string10.1','string1.2 number2.2 ... string10.2'...'string1.10 number2.10 ... string10.10']}
- **[Pete Kirkham](https://stackoverflow.com/users/1527)** (2023-04-06): It's not really worth an answer here, but look at the answer already mentioned, then look at the manual for the library they use here https://docs.python.org/3/library/csv.html and you will see there is a `delimiter` parameter which you can change from comma to space
- **[Timus](https://stackoverflow.com/users/14311263)** (2023-04-06): If your delimiter is a single whitespace then `import csv` and do `with open("file.txt", "r") as file: result = list(csv.DictReader(file, delimiter=" "))`. Maybe you have to adjust `delimiter` and/or add `skipinitialspace=True`.
