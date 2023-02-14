---
title: "Remove redundant tuples from dictionary based on the score"
site: stackoverflow
question_id: 75448227
answer_id: 75451173
url: https://stackoverflow.com/a/75451173
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-14T17:15:43Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75451173/revisions
accepted: false
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 08cd2ad45f796f94cca52966393a0b3ea159fdec8a0f12ae3c4e16cc2439d251
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75451173>, 2023-02-14; score 1. Text as retrieved 2026-10-12.

<sub>Not sure it's the most efficient, but since you also mentioned *"a simple solution"* in a comment....</sub>

I think the simplest method would involve looping through every tuple *twice*: once to collect best scores, and then again to filter everything else. Something like <kbd>`new_a = onlyBest( a, bestRef=dict(sorted(getAllPairs(a))) )`</kbd> [see function definitions below].

```python
def getAllPairs(obj):
    if isinstance(obj, tuple) and len(obj)==2: return [obj]
    allPairs = []
    if isinstance(obj, dict): obj = obj.values()
    if hasattr(obj, '__iter__') and not isinstance(obj, str):
        for i in obj: allPairs += getAllPairs(i)
    return allPairs

def onlyBest(obj, bestRef:dict):
    if isinstance(obj, list):
      # if all(isinstance(i, tuple) and len(i)==2 for i in obj):
        return [i for i in obj if not i[1] < bestRef.get(i[0],i[1])]
    if isinstance(obj, dict):
        return {k: onlyBest(v,bestRef) for k, v in obj.items()}
    return obj        
```
