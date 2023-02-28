---
title: "Python Dictionary to Array"
site: stackoverflow
question_id: 75591182
answer_id: 75594394
url: https://stackoverflow.com/a/75594394
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-28T15:54:45Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75594394/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bff34c1843a27ea68b3952c5f8f33c69605f170ac8d9b1d19b602a7d284e98e3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75594394>, 2023-02-28; score 0. Text as retrieved 2026-10-12.

<sup>(Btw, initiating with *`res=[]`* isn't necessary here.)</sup>

Setting *`key=lambda x:(-x[1],x[0])`* [same as <kbd>**`key=lambda k,v: (-v,k)`**</kbd>] tells the `sorted` function to sort `D.items()` [which is a list of tuples each containing a key-value pair] to first sort by values (in reverse, because of the negative) and then [if there are multiple values that are the same] by keys.

For more details, you might want to read [this article on How a List of Tuples is Sorted](https://learnpython.com/blog/sort-tuples-in-python/#:~:text=The%20sorted()%20method%20sorts,and%20the%20third%20with%203.&text=The%20second%20element%20is%20the,by%20the%20sorted()%20function.) and/or documentation on [sorting](https://docs.python.org/3/howto/sorting.html#key-functions), [`lambda`](https://docs.python.org/3/reference/expressions.html#lambda) expressions and the [`.items`](https://docs.python.org/3/library/stdtypes.html#dict.items) method.
