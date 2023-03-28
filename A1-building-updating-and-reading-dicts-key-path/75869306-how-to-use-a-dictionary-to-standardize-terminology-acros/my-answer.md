---
title: "How to use a dictionary to standardize terminology across lists"
site: stackoverflow
question_id: 75869306
answer_id: 75871953
url: https://stackoverflow.com/a/75871953
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-28T23:46:17Z
last_edited: 2023-03-29T00:15:17Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75871953/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 30608d8f00534156e6710ca88cd37691ab66e963802f7abbef09399059b45836
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75871953>, 2023-03-28, last edited 2023-03-29; **accepted**; score 1. Text as retrieved 2026-10-12.

> What I did is the following: Loop through the list and loop through dictionary.
> 
> ```py
> for i in super_list:
>     for key, value in voc_dict.items():
>          i.replace(voc_dict[key], voc_dict[value])
> ```

I would expect there to be at least three issues with this:

1. You mentioned that `super_list` is a nested list, for you also need a nested `for`-loop to traverse it. Also `i` is just a list [not a string] and does not have a `.replace` method, so `i.replace` would [raise an `AttributeError`][1].
2. As TimRoberts [commented](https://stackoverflow.com/questions/75869306/how-to-use-a-dictionary-to-standardize-terminology-across-lists#comment133828984_75869306), `.replace` is **not** an [inplace](https://stackoverflow.com/a/22453908/6146136) method, so you would need something like `i = i.replace...` to change `i` [if `i` was a string].
3. Although, even if `i` *was* a string, there would be no point in using *`i = i.replace...`* because `i` would be a ***copy*** of an item in the list. Generally, you should use [`enumerate`](https://www.programiz.com/python-programming/methods/built-in/enumerate) if you want to loop through and edit a list.

```py
for si, sub_list in enumerate(super_list):
    for i, sl_item in enumerate(sub_list):
        for k, kw in Voc_dict.items():
            super_list[si][i] = sl_item.replace(k, kw)
```

However, if you try the above code on your sample `super_list`, you might notice that [only the first item gets altered][2], so you need to either add `'Bat man': 'Batman'` to `Voc_dict` or use [regex](https://www.w3schools.com/python/python_regex.asp) with [`re.IGNORECASE`](https://www.geeksforgeeks.org/name-validation-using-ignorecase-in-python-regex/) by using <kbd>**`re.sub(k, kw, sl_item, flags=re.I)`**</kbd><sup>([view output][3])</sup> instead of *`sl_item.replace(k, kw)`*.

<br>

If you use regex, you can reduce the number of iterations by first reducing `Voc_dict` to something like <kbd>*`{'(Batman|the Batman|bat man)': 'Batman'}`*</kbd> with

```py
Voc_dict = {'('+'|'.join([
    k for k,v in Voc_dict.items() if v==kw
])+')':kw for kw in set(Voc_dict.values())}
```


  [1]: https://i.sstatic.net/zc35o.png
  [2]: https://i.sstatic.net/WpiGX.png
  [3]: https://i.sstatic.net/uD08s.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[H. H.](https://stackoverflow.com/users/12945798)** (2023-03-29): Hi @Driftr95 thank you very much for this response. it is very helpful. To explore, your regex take. What I did before is break each statement by space split(" ") and try to replace and loop through each word in each list and replace if matches. but it did not work for statements where the it is written like "Batman's". Is there a smarter way to to avoid this loop in a loop issue.
- **me** (2023-03-29): @H.H. that would also not work for `bat man` and `the Batman` since those are separate words. On the other hand, `.replace` or `re.sub` [without `split`] should work with added `'s` or any other suffix (or prefix, for that matter) though, *and* it involve one less loop so what's the issue?
