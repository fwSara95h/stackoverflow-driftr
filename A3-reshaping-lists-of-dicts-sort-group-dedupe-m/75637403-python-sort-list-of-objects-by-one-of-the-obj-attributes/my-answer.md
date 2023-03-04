---
title: "Python - sort list of objects by one of the obj attributes and then by dict value"
site: stackoverflow
question_id: 75637403
answer_id: 75638136
url: https://stackoverflow.com/a/75638136
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-04T19:22:42Z
last_edited: 2023-03-04T21:19:36Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75638136/revisions
accepted: false
score: 1
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 751e5253853201b890abfc13ccfd7446345a89ae2ea2a4dbc541749b6a03ac75
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75638136>, 2023-03-04, last edited 2023-03-04; score 1. Text as retrieved 2026-10-12.

> *Everything in the code works fine except for line: `dwarfs.sort(key=lambda x:-x.physics)` which is incomplete.....I want to sort the objects by: `self.physics` and then, if multiple with the same value, by appearance of the `color`*

Change the `key` argument in *`dwarfs.sort(key=lambda x:-x.physics)`* to
- <kbd>**`dwarfs.sort(key=lambda x:(-x.physics, -colors[x.hat_color]))`**</kbd> to have the color with the maximum value in `colors` at the top (which is probably what you want, judging by how you sorted `colors` first)
- <kbd>**`dwarfs.sort(key=lambda x:(-x.physics, x.hat_color))`**</kbd> if you just want to sort by the name of the color
- <kbd>**`dwarfs.sort(key=lambda x:(-x.physics, x.hat_color, x.name))`**</kbd>if you want to sort by the name as well.... 

For more details see [Sorting HOW TO — Python 3 documentation](https://docs.python.org/3/howto/sorting.html).

---

Btw, you can shorten your code to

```py
dwarfs, colors = [], {}
while (entry := input())!='Once upon a time':
    name,hat_color,physics = entry.split(" <:> ")
    obj = Dwarf(name, hat_color, int(physics))

    for i, d in enumerate(dwarfs):
        if d.name==name and d.hat_color==hat_color:
            dwarfs.pop(i)
            break
    else: colors[hat_color] = colors.get(hat_color,0)+1
    dwarfs.append(obj) 

# colors = dict(sorted(colors.items(),key=lambda x:-x[1])) # ? unnecessary ?
dwarfs.sort(key=lambda x:(-x.physics, -colors[x.hat_color]))

print(*dwarfs, sep='\n')
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **me** (2023-03-04): @KellyBundy what does that mean? something like `list(colors.keys()).index(x.hat_color)`? The rgb value? `colors[x.hat_color]`? Until they specify, I'll assume they just meant the color itself ¯\_(ツ)_/¯
- **[ddoch003](https://stackoverflow.com/users/19971042)** (2023-03-05): thank you so very much! `dwarfs.sort(key=lambda x:(-x.physics,-colors[x.hat_color]))` is exactly what I wanted. I was just not sure about the correct syntaxis. It is working fine now.
