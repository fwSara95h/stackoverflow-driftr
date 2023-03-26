---
title: "Time complexity for constructing a Python list from a dict"
site: stackoverflow
question_id: 75849296
url: https://stackoverflow.com/q/75849296
asked: 2023-03-26T17:09:00Z
asked_by: "Rayan Zakaria Hassici"
asked_by_url: https://stackoverflow.com/users/21495417
last_edited: never
tags: [python, dictionary, time-complexity]
score: -1
views_at_snapshot: 118
answer_count: 1
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 3484e5d6b31ab6f0def16a617b40258afd8b76aaa4d3ece8dd19d1d4100e1865
---

# Time complexity for constructing a Python list from a dict

Asked by [Rayan Zakaria Hassici](https://stackoverflow.com/users/21495417) on Stack Overflow, <https://stackoverflow.com/q/75849296>, 2023-03-26. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I am trying to find the best way ( the most efficient in terms of time complexity ) to pop the last key-value pair in a Python dictionary.

What I am currently using is 

```python
my_dict.pop(list(my_dict.keys())[-1])
```

But I am not sure what is the time complexity of ```list(my_dict.keys())```
as I am trying to keep it `O(1)` on average

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[luk2302](https://stackoverflow.com/users/2442804)** (2023-03-26): What is "the last key-value pair"? Why do you want to do that? The problem is not the .keys(), if anything the conversion to a list is the problem.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-26): You won't know which one is the last one until you go through all the keys. Maybe there's a way to get it from the dict keys iterator itself, although probably not. I'll look. But making a list of it completely rules that out. You've already executed O(n) at that point, before you access [-1]
- **[Thomas W.](https://stackoverflow.com/users/480982)** (2023-03-26): The definition of *last* in a dictionary is not very meaningful.
- **[Kenny Ostrom](https://stackoverflow.com/users/1766544)** (2023-03-26): Thomas Weller makes a good point. If you care about retrieving items by index, maybe dict isn't the right data structure for you. But in the spirit of answering the question, all I've found so far is class dict_keys, which may be a PyListObject in the C interface, but is not a list, and """ D.keys() -> a set-like object providing a view on D's keys """ If there is a way, it is probably implementation specific.
- **[Samwise](https://stackoverflow.com/users/3799759)** (2023-03-26): `dict` won't let you do this in O(1).  Have you looked at `OrderedDict`?  https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem
- **[Timus](https://stackoverflow.com/users/14311263)** (2023-03-26): What's wrong with [`my_dict.popitem()`](https://docs.python.org/3/library/stdtypes.html#dict.popitem) (it is LIFO)?
