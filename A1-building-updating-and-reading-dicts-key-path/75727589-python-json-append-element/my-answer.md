---
title: "Python - Json: append element"
site: stackoverflow
question_id: 75727589
answer_id: 75730126
url: https://stackoverflow.com/a/75730126
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-14T07:26:25Z
last_edited: 2023-03-14T07:41:04Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75730126/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 96cf6875597c6b2626014d22a5be81107ee4a6e5f200fd5a992b8ea98ae56b87
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75730126>, 2023-03-14, last edited 2023-03-14; score 0. Text as retrieved 2026-10-12.

> ```py
>     if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"]:
>         jsondata["Job"]["LoggingData"]["Logs"]["LogDetails"].append(new_data)
> ```

This would have worked as intended if your initial `jsonfile` looked like

```py
jsonfile = {
    "Job": {
        "id": "",
        "LoggingData": {
            "Logs":{"LogDetails": [{}]} ## NOT [{"LogDetails": [{}]}]
        }
    }
}
```

However, what you have is *`..."Logs":[{"LogDetails": [{}]}]...`*; so, *`jsondata["Job"]["LoggingData"]["Logs"]`* is a **list** (from which items can be accessed with [indices, not keys](https://realpython.com/python-dicts/#dictionary-keys-vs-list-indices)), so you can't check in it for *`"LogDetails"`* which is a **key** in the dictionary that is the first item in said list (i.e., **`jsondata["Job"]["LoggingData"]["Logs"][0]`**).

To add `new_data` to the first dictionary in `Logs`, you should change that `if` block to 

```py
    if "LogDetails" in jsondata["Job"]["LoggingData"]["Logs"][0]:
        print("Joy - Found LogDetails") 
        jsondata["Job"]["LoggingData"]["Logs"][0]["LogDetails"].append(new_data)
```

Use **`...["Logs"][-1]...`** (instead of *`...["Logs"][0]...`*) if you want to add `new_data` to the *last* dictionary in `Logs`. [Ofc, it won't make a difference if `Logs` has only one item.]

<sub>Btw, you could also use [`isinstance`](https://www.programiz.com/python-programming/methods/built-in/isinstance) and [`.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) [or even just [`try...except`](https://www.programiz.com/python-programming/exception-handling)] to check for and ensure your data structure.</sub>
