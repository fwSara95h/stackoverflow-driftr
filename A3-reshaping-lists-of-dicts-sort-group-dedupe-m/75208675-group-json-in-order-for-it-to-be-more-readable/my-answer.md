---
title: "Group JSON in order for it to be more readable"
site: stackoverflow
question_id: 75208675
answer_id: 75217863
url: https://stackoverflow.com/a/75217863
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-24T05:53:11Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75217863/revisions
accepted: false
score: 0
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e5ec1e8de5ae31eb4eb4bcd460545bc13d32fe5d69e44e75040a10bfb23dc508
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75217863>, 2023-01-24; score 0. Text as retrieved 2026-10-12.

>  but it says `string indices must be integers`

`texty` is a string [**not a list** of dictionaries as you seem to be expecting] because that's what *`.read()`* returns (when you `open` with `mode='r'`); so when you iterate through it with *`for group in texty...`*, each `group` is a single-character string [and not a dictionary], and that's why the error is being raised [I assume] at *`ent = group["entity_group"]`*.

---

Reluctant suggestion: Try adding a line with **`exec(f'texty = {texty.strip()}')`** before *`for group...`*. 

But this is NOT a good way to save data. Please look into [json](https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/) and [pickle](https://www.thoughtco.com/using-pickle-to-save-objects-2813661). [I prefer json as it's not specific to python.]

---
---

As for

>  I also think that I could make it HTML and color it to visualize better the result, but I'm sure there's a quicker solution

I'm afraid there isn't enough code nor context to fully understand what you mean here. Including the definition of `replace_at` as well as a sample set of `text` and [desired] `text2` values might help.
