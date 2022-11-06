---
title: "how to change boolean value thats another file"
site: stackoverflow
question_id: 74334979
answer_id: 74335222
url: https://stackoverflow.com/a/74335222
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-11-06T10:58:41Z
last_edited: 2022-11-07T20:30:19Z
revisions: 2
revision_history: https://stackoverflow.com/posts/74335222/revisions
accepted: false
score: 1
chapter: G2
chapter_title: "Small Python one-offs"
cluster: python-misc
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 946a5f1b86a9e4cd7d84c27c1af122ef71d960e1616f8fef5fe447a5af4eb40c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-11-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74335222>, 2022-11-06, last edited 2022-11-07; score 1. Text as retrieved 2026-10-12.

> Then i think booleans.storepass is like a variable but like a copy of the one in booleans? Because when i go on the booleans file again its still False.

That's correct - you can't change the values inside a .py file just by importing and then setting within another. py file. The standard way to manipulate files is by using some variation  of 
```python
with open('boolean.py', 'w') as f: 
    f.write('storepass = False')
```

<hr>

Personally, I really dislike writing over .py files like this; I usually save as [JSON](https://www.w3schools.com/python/python_json.asp). So "boolean.json" can have just
```json
{"storepass": false}
```
and then in your python code you can (instead of importing) get it as
```python
# import json
boolean = json.load(open('boolean.json', 'r'))
```

and set `storepass` with
```python
# import json
boolean.storepass = True
with open('boolean.json', 'w') as f:
    json.dump(boolean, f, indent=4)
    ## NOT f.write(boolean)
```
and this  way, if there are more values in `boolean`, they'll also be preserved (as long as you don't use the variable for anything else in between...)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **user20226026 (account no longer exists)** (2022-11-07): can you clarify how you set storepass? im struggiling to understand what it means, what is boolean doing in the f.write line? how do i make sure its changing storepass and not another boolean
- **me** (2022-11-07): @katie I'm so sorry! I should have been using `json.dump` with JSON, not `f.write`. I've corrected my answer. Anyway,  the `boolean.storepass = True` line just sets `storepass` locally, so only the code being run just then will be affected by the change; then `f.write(boolean)` saves the updated `boolean` to the 'boolean.json' file
- **me** (2022-11-07): @katie *"how do i make sure its changing storepass and not another boolean"* - as long as multiple programs aren't  writing to 'boolean.json' *at the same time*, it should be fine - when you read with `boolean = json.load(open('boolean.json', 'r'))`, you'll be getting all the booleans and [as I said] they'll be preserved **as long as you don't use the `boolean` variable for anything else in between**. with `boolean.storepass = True` you're only changing `storepass`
