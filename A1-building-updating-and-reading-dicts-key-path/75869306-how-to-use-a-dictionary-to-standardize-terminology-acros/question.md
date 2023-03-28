---
title: "How to use a dictionary to standardize terminology across lists"
site: stackoverflow
question_id: 75869306
url: https://stackoverflow.com/q/75869306
asked: 2023-03-28T17:27:42Z
asked_by: "H. H."
asked_by_url: https://stackoverflow.com/users/12945798
last_edited: 2023-03-29T01:43:31Z
tags: [python, list, dictionary]
score: 0
views_at_snapshot: 97
answer_count: 1
accepted_answer_id: 75871953
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dbc90fa1e2b15d1454d400b1c8e77a7b2b3672d4fc88936499e5ba7e4260bf99
---

# How to use a dictionary to standardize terminology across lists

Asked by [H. H.](https://stackoverflow.com/users/12945798) on Stack Overflow, <https://stackoverflow.com/q/75869306>, 2023-03-28, last edited 2023-03-29. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have been trying to solve this issue for a while but I can't seem to think of a right solution.

Basically, I am parsing few pdfs and depending on the source of the pdf, the terminology used is different. For example, source A1 writes 'Batman' as 'The Batman'. Source B2 writes it as 'bat man'. 

So what I tried to do is create a dictionary:

```py
Voc_dict = {'Batman':'Batman',
'the Batman': 'Batman',
'bat man': 'Batman'}
```
Assume this dictionary extends to other superhero names. 

So, I am trying to standardize the following 2d list:

```py
Super_list  = [['among the heros with daddy issues, the bat man shines'], ['Bat man protects the city with everything he gots']]
```

You get the picture.

Apologies for the format and stupid example. I can't find more relatable one and it is my first time using mobile app.

Thank guys.

What I did is the following:
Loop through the list and loop through dictionary.

```py
For i in super_list:
    For key, value in voc_dict.items():
         i.replace(voc_dict[key], voc_dict[value])
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[LeoE](https://stackoverflow.com/users/9227188)** (2023-03-28): You can create a regex for each of your heroes that represents all the different ways that it is commonly spelled and search for that regex in your files maybe?
- **[H. H.](https://stackoverflow.com/users/12945798)** (2023-03-28): Thanks for your response. I have tried but unfortunately some of strings are mixed (letters and integer) also it tend to pick up some of the target but not all.
- **[Tim Roberts](https://stackoverflow.com/users/1883316)** (2023-03-28): It is pointless to replace `'Batman'` with `'Batman'`.  And your loop is incorrect because `str.replace` does not  (cannot) change the string in place.  You need to do something like `i = i.replace(...)` and then add the final `i` to a new list.
