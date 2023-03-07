---
title: "how to print keys of dictionary in coordinate way?"
site: stackoverflow
question_id: 75659579
answer_id: 75668131
url: https://stackoverflow.com/a/75668131
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-07T23:29:03Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75668131/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f8f23317af3b50b6714545a5d8b5138bf9af9f2710fd07dd98e2f6dbaf4b4678
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-07

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75668131>, 2023-03-07; score 0. Text as retrieved 2026-10-12.

If you *must* print them, below is a version of the first suggestion in [mozway's answer](https://stackoverflow.com/a/75659819/6146136), where you initiate a matrix full of a single character and then fill it at certain indices [that correspond to the coordinates] according to `dic2`.

```py
bgChar = '+' # '▪' # '●' # ' ' # '⁜' # set a "background" character
dic2 = {(0,0):'⬃', (-2,-2):'⇩', (-2,-3):'⇩'}

getRange = lambda l: (min(l), max(l))
x_min, x_max = getRange([c[0] for c in dic2])
y_min, y_max = getRange([c[1] for c in dic2])

myCanvas = [[f'{bgChar:^3}']*(x_max-x_min+3) for _ in range(y_max-y_min+3)]
for (x,y),v in dic2.items(): 
    myCanvas[y+1-y_min][x+1-x_min] = f'{v:^3}'

print(' '*3+''.join([f'{i+1+x_min:^3}' for i in range(x_max - x_min + 3)]))
for i, r in list(enumerate(myCanvas))[::-1]: 
    print(''.join([f'{i-1+y_min:^3}']+r))
```

> ![view results][1]

<sup>I added the numbers for the axes and also changed the character (`bgChar`) in "coordinates" that are not covered in `dic2` (because I felt like using space `' '` made it a bit hard to figure out the coordinates of printed arrows).</sup>

---

However, as you can see, variations in character width mess up the alignment of x-coordinates, so it might be better to **plot** rather than print, using something like [`matplotlib.pyplot`](https://matplotlib.org/stable/tutorials/introductory/pyplot.html) which has a handy method called [`annotate`](https://www.geeksforgeeks.org/matplotlib-pyplot-annotate-in-python/).

```py
import matplotlib.pyplot as plt

dic2={(0,0):'⬃',(-2,-2):'⇩',(-2,-3):'⇩'}
getRange = lambda l: (min(l), max(l))
x_min, x_max = getRange([c[0] for c in dic2])
y_min, y_max = getRange([c[1] for c in dic2])

fig, myCanvas = plt.subplots()
myCanvas.set_xlim(x_min-1, x_max+1)
myCanvas.set_ylim(y_min-1, y_max+1)

for xy, v in dic2.items(): myCanvas.annotate(v, xy, xy)
plt.show()
```

[![opplt][2]][2]


  [1]: https://i.sstatic.net/mAzQI.png
  [2]: https://i.sstatic.net/8QgFH.png
