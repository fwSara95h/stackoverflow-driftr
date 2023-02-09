---
title: "Back edges program"
site: stackoverflow
question_id: 75397027
answer_id: 75404626
url: https://stackoverflow.com/a/75404626
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-09T21:32:45Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75404626/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b6e3f660f39f2b70c9bda17061d98496b686aa8fb0eab1aff4fac0d08bd96a06
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-09

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75404626>, 2023-02-09; **accepted**; score 0. Text as retrieved 2026-10-12.

If I understand [this](https://stackoverflow.com/a/64298275/6146136) correctly, then back edges lead to `neighbor`s that are in `stack` at the time, so instead of *`elif discovery_time[neighbor] < discovery_time[current]`*, you need to use **`elif neighbor in stack`**

```python
def ArcA(graph, start):
    stack = []
    discovery_time = {}
    finish_time = {}
    back_edges = []
    time = 0

    stack.append(start)

    while stack:
        current = stack.pop()
        if current not in discovery_time:
            time += 1
            discovery_time[current] = time
            stack.append(current)
            
            for neighbor in graph[current]:
                if neighbor not in discovery_time:
                    stack.append(neighbor)
                elif neighbor in stack: ### EDIT ###
                    back_edges.append((current, neighbor))

            time += 1
            finish_time[current] = time

    return back_edges
```

and now <kbd>`ArcA(graph={'A': ['B','C'], 'B': ['C'], 'C': ['D'], 'D': ['A']}, start='A')`</kbd> should return just **`[('D', 'A')]`** and cross edges like *`('B', 'C')`* should no longer be included in the output.
