---
title: "Deduplicating nested values that are also key in outer dictionary - Python"
site: stackoverflow
question_id: 75958907
answer_id: 75961692
url: https://stackoverflow.com/a/75961692
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-07T20:20:19Z
last_edited: 2023-04-07T20:26:50Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75961692/revisions
accepted: true
score: 1
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 38c5fd18853b3e4b0f50f255bde9724b1ede1cb250841cc1effe8b1a1036fc41
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75961692>, 2023-04-07, last edited 2023-04-07; **accepted**; score 1. Text as retrieved 2026-10-12.

There's not really any way to check every item without iterating through every value in every key's list at least once; the most I can suggest is to eliminate the need for the `if _ in x` checks by using [`.get`](https://www.programiz.com/python-programming/methods/dictionary/get) and [`.pop`](https://www.programiz.com/python-programming/methods/dictionary/pop):

```py 
for k in [*x]: 
    for z in x.get(k, []): 
        x.pop(z, None) 
```

or with [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```py
for k in [*x]: [x.pop(z,None) for z in x.get(k,[])]
```

(Using [`[*x]`](https://towardsdatascience.com/306ae44cd480) is effectively the same as using `list(x)` or `list(x.keys())` or `[k for k in x]`.)

<br>

---

<br>

Btw, it would be a bit simpler to remove the list items that are duplicates of keys, like

```py
x_dedup = {k: [z for z in y if z not in x] for k,y in x.items()}
```

and `x_dedup` would look like

> ```py
> {
>   'A fantastic gift for art lovers': ['Designed for adults, this stunning piece of 3D art can be proudly displayed on a wall following a rewarding build experience.'],
>   'Build and relax': ['Art lovers can enjoy a relaxing and immersive building experience as they create this unique artwork from 1,810 pieces.'],
>   'Create your own artwork': ['Build Hokusai’s The Great Wave with layers of LEGO® bricks.'],
>   'Finishing touch': ['Add a decorative tile with Hokusai’s signature.'],
>   'Hokusai – The Great Wave': [
>     'Build Hokusai’s The Great Wave with layers of LEGO® bricks.',
>     'The picture’s multiple layers create a stunning 3D effect.',
>     'Add a decorative tile with Hokusai’s signature.'
>   ],
>   'Immerse yourself in the world of art': ['Listen to the set’s Soundtrack, tailor-made with content to enhance the time you spend building this Japanese wall art.'],
>   'Recreate an iconic piece of Japanese art': ['Celebrate your passion for Japanese art when you build this incredible LEGO® version of Hokusai’s The Great Wave.'],
>   'The Great Wave comes to life!': ['The picture’s multiple layers create a stunning 3D effect.']
> }
> ```

Is that a viable option for you?

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[alvas](https://stackoverflow.com/users/610569)** (2023-04-08): Definitely not the 2nd case to remove duplicates in values. But it'll be good to leave it in the answer just in case anyone in the future find it useful. Seems like `.pop` is one way to avoid the `if k in x` checks.
