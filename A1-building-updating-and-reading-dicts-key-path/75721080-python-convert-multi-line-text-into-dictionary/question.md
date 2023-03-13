---
title: "Python: Convert multi-line text into dictionary"
site: stackoverflow
question_id: 75721080
url: https://stackoverflow.com/q/75721080
asked: 2023-03-13T11:09:19Z
asked_by: "user2286565"
asked_by_url: https://stackoverflow.com/users/2286565
last_edited: never
tags: [python, python-3.x, dictionary, text, multiline]
score: 2
views_at_snapshot: 672
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 68de91910740512f64656767d02da54e3cb8ed735bd5464a65c8c70cb2db8bf2
---

# Python: Convert multi-line text into dictionary

Asked by [user2286565](https://stackoverflow.com/users/2286565) on Stack Overflow, <https://stackoverflow.com/q/75721080>, 2023-03-13. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have a textfile of the format (well, it is much less structured, but the parts I need follow the below idea):

```
[ThisShouldBeAKey]
Value1=yes
Value2=no
Value3=fancywords
Value4=numbers

[ThisShouldBeAnotherKey]
Value2=true
Value3=333
Value5=qqq
```

I want to convert this file into a dictionary, so that I can easily compare certain values of certain keys. E.g., retrieve Value8 and Value9 of [Key1] and [Key100].

I imagine I can retrieve Value8 and Value9 by simply iterating over a textdump of the [key], and using startswith() or other string functions to retrieve what I want. So, although you could (ideally?) make a nested dictionary, I don't >think< I necessarily require this.

However, I even have trouble simply getting a dictionary of [Key]:Value1Value2Value3AllthevaluesTextdump. I have tried a few things on my own, I have tried the suggestion here ( https://stackoverflow.com/questions/52330853/in-python-how-do-i-read-a-file-into-a-dictionary-with-multiple-line-entries ) and alterations on it, but I always run into a problem with for-loops, while-loops, or the file simply not being read properly.

How would you recommend doing this?

Thank you in advance!

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[buran](https://stackoverflow.com/users/4046632)** (2023-03-13): Check [configparser module from standard library](https://docs.python.org/3/library/configparser.html)
- **[OuterSoda](https://stackoverflow.com/users/19922257)** (2023-03-13): Dictionaries can only have one value per key, so you would need an array to hold all the values or a nested dictionary if you want the custom indexes.
- **[Jorge Luis](https://stackoverflow.com/users/12575557)** (2023-03-13): Does this answer your question? [How to read and write INI file with Python3?](https://stackoverflow.com/questions/8884188/how-to-read-and-write-ini-file-with-python3)
