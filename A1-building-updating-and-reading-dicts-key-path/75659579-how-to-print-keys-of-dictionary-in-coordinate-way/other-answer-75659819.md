---
title: "how to print keys of dictionary in coordinate way?"
site: stackoverflow
question_id: 75659579
answer_id: 75659819
url: https://stackoverflow.com/a/75659819
author: "mozway"
author_url: https://stackoverflow.com/users/16343464
posted: 2023-03-07T08:58:49Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f9ce17d30e79d9933efd942c448718cd6548a089ae44b8202435f6648a28ed3a
role: another answer on the same question, kept as context; not my work
---

# Answer by [mozway](https://stackoverflow.com/users/16343464) — 2023-03-07

Posted on Stack Overflow, <https://stackoverflow.com/a/75659819>, 2023-03-07. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

My understanding is that you want to print your values on a grid at the coordinates specified by the key.

Let's assume a square matrix of size `N`. I will show empty cells as `⋅` for clarity.

You can use:
```
N = 5

dic2={(0,0):'⬃',(-2,-2):'⇩',(-2,-3):'⇩'}

matrix = [['⋅' for _ in range(5)] for _ in range(5)]

for (x,y), v in dic2.items():
    matrix[x][y] = v
    
print('\n'.join(map(''.join, matrix)))
```

Alternatively, you wan rework the dictionary and use:
```
N = 5

dic3 = {(i if i>=0 else N+i, j if j>=0 else N+j):v for (i,j),v in dic2.items()}
# {(0, 0): '⬃', (3, 3): '⇩', (3, 2): '⇩'}

print('\n'.join([''.join([dic3.get((i, j), '⋅')
                 for i in range(N)]) for j in range(N)]))
```
Output:
```
⬃⋅⋅⋅⋅
⋅⋅⋅⋅⋅
⋅⋅⋅⋅⋅
⋅⋅⇩⇩⋅
⋅⋅⋅⋅⋅
```
