---
title: "python say isalpha() is not defined despite it being built in (I think)"
site: stackoverflow
question_id: 75655791
answer_id: 75655893
url: https://stackoverflow.com/a/75655893
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-06T21:12:03Z
last_edited: 2023-03-06T21:17:50Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75655893/revisions
accepted: false
score: 0
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 2181431ddd70dc238a7f374be6d32f93bbe8bd7f914c627d86d24e891995d7cc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75655893>, 2023-03-06, last edited 2023-03-06; score 0. Text as retrieved 2026-10-12.

[`.isalpha`](https://www.programiz.com/python-programming/methods/string/isalpha) is a method not a function <sup>(see [this tutorial](https://techvidvan.com/tutorials/python-methods-vs-functions/) to learn more about the difference)</sup>, so it cannot be called by name. I think you want 

```py
    if str(things).isalpha(): continue
``` 

or 

```py
    if isinstance(things, str) and things.isalpha(): 
        continue
```

<br>

Also, the `else` is not necessary after `continue`, so you can follow with **`yes.append(things)`** <sup>(not just *`yes.append`*)</sup>:

```py
yes = []
item=[1,7,-10,34,2,"a",-8]
for things in item:
    if isinstance(things, str) and things.isalpha(): 
        continue
    yes.append(things)
    print(yes)
```

(But why are you printing `yes` [potentially on repeat] inside the loop instead of after the loop?)

---

Alternately you could just use [list comprehension](https://www.programiz.com/python-programming/list-comprehension) <sup>([view output][1])</sup> 

```py
item=[1,7,-10,34,2,"a",-8]
yes = [i for i in item if not (isinstance(i, str) and i.isalpha())] 
print(*yes, sep='\n')
```


  [1]: https://i.sstatic.net/oBaMj.png
