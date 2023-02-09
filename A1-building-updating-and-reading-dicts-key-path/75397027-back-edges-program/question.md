---
title: "Back edges program"
site: stackoverflow
question_id: 75397027
url: https://stackoverflow.com/q/75397027
asked: 2023-02-09T10:07:22Z
asked_by: "Mustapha Doubabi"
asked_by_url: https://stackoverflow.com/users/21179054
last_edited: 2023-02-09T14:26:11Z
last_editor: "Driftr95 (me)"
last_editor_url: https://stackoverflow.com/users/6146136
tags: [python, dictionary, graph, depth-first-search, directed-acyclic-graphs]
score: 0
views_at_snapshot: 88
answer_count: 1
accepted_answer_id: 75404626
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: d1485bc38bc9463bfddce54367010090fd5743b0d07fabefc2329b82bdef136b
---

# Back edges program

Asked by [Mustapha Doubabi](https://stackoverflow.com/users/21179054) on Stack Overflow, <https://stackoverflow.com/q/75397027>, 2023-02-09, last edited 2023-02-09 by me. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I implemented a program that finds back edges on a graph stored a dictionary.

Example :
 
- Input : `(graph={'A': ['B','C'], 'B': ['C'], 'C': ['D'], 'D': ['A']}, start='A')`

- Output : `[('D', 'A'), ('B', 'C')]`

The problem is that it also returns cross edges, can you help me find where the problem is ?
I haven't found an answer for several days.


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
                elif discovery_time[neighbor] < discovery_time[current]:
                    back_edges.append((current, neighbor))

            time += 1
            finish_time[current] = time

    return back_edges
```
Thank you !


I expect my code to only returns back edges, but I think that it also returns cross edges.
