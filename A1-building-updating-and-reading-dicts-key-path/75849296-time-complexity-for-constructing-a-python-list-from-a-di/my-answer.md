---
title: "Time complexity for constructing a Python list from a dict"
site: stackoverflow
question_id: 75849296
answer_id: 75849875
url: https://stackoverflow.com/a/75849875
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-26T18:55:51Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75849875/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fa253182668a0e09e9b7afdc71036bd01bfe0197940c786179ec3a435b0bd38e
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75849875>, 2023-03-26; score 0. Text as retrieved 2026-10-12.

> *What's wrong with [`my_dict.popitem()`](https://docs.python.org/3/library/stdtypes.html#dict.popitem) (it is LIFO)?* - [comment](https://stackoverflow.com/questions/75849296/time-complexity-for-constructing-a-python-list-from-a-dict#comment133791128_75849296) by [Timus](https://stackoverflow.com/users/14311263/timus)

It [has O(1) time complexity](https://thecodingbot.com/python-dictionarys-popitem-method-with-examples/#:~:text=Time%20Complexity:) [due to being a [LIFO](https://www.geeksforgeeks.org/lifo-last-in-first-out-approach-in-programming/) operation] like you want.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-10-07): Your reference for O(1) doesn't exist anymore. Do you have another?
