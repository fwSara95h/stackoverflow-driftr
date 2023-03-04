---
title: "Create a list of values from an existing list if values are nearby"
site: stackoverflow
question_id: 75615203
answer_id: 75637960
url: https://stackoverflow.com/a/75637960
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-04T18:57:25Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75637960/revisions
accepted: false
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: bf9ed6df0971f498f5b678f19326cda9813f17e29b7af2b37be0dec667e172bc
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75637960>, 2023-03-04; score 1. Text as retrieved 2026-10-12.

Setup:

```py
apData = [{"Name": 'A', "Area": 10000, "Price": 100}, {"Name": 'B', "Area": 9500, "Price": 99}, {"Name": 'C', "Area": 11000, "Price": 101}, {"Name": 'D', "Area": 12000, "Price": 150}, {"Name": 'E', "Area": 14000, "Price": 200}, {"Name": 'F', "Area": 14500, "Price": 400}, {"Name": 'G', "Area": 12999, "Price": 159}]

threshRef = {'Area':1000, 'Price':10}
ck_margins = lambda c,n: all(abs(n[k]-c[k])<=threshRef[k] for k in threshRef)
```

`threshRef` should contain all the thresholds, and `ck_margins` is for checking if 2 dictionaries are within each other's thresholds as specified in `threshRef` (if the logic is more complicated, you might have to define a function instead of just using a [lambda expression](https://www.programiz.com/python-programming/anonymous-function)).

---

> *The only idea, which comes to my mind is the naive solution to perform 2 loops for the each list to compare the Area and Price values with others.*

That *is* the simplest way to do it - some variation of the code below, which checks each item against every other item [ [time complexity](https://blog.teclado.com/time-complexity-big-o-notation-python/): <kbd>[**O(n<sup>2</sup>)**](https://blog.teclado.com/time-complexity-big-o-notation-python/#6on2polynomialtime)</kbd> ]. 

```py
selected, unselected = [], []
for i, cur in enumerate(apData):
    selectCur = any(ck_margins(cur,d) for di,d in enumerate(apData) if di!=i) 
    (selected if selectCur else unselected).append(cur)
```

<br>


You could improve on it a bit by stopping as soon as you reach the first item that matches the criteria [since you only need one match]; then the time complexity could still be <kbd>O(n<sup>2</sup>)</kbd> in the worst case [if none of them were to be selected], but in the best case [sorted list where all of them get selected] it could be as low as <kbd>O(n)</kbd> [linear].

```py
selected, unselected = [], []
for i, cur in enumerate(apData):
    selectCur = False
    for di, d in enumerate(apData):
        if di!=i and ck_margins(cur,d):
            selectCur = True
            break
    (selected if selectCur else unselected).append(cur)
```

<br>

Or you could only check each item against every item that comes *after* it in the list, so that no combination gets checked more than once [time complexity: <kbd>[**<sub>n</sub>C<sub>2</sub>**](https://www.calculatorsoup.com/calculators/discretemathematics/combinations.php)</kbd>].

```py
selected, unselected, hasNeighbor = [], [], [False]*len(apData)

for i1, d1 in enumerate(apData):
    for i2, d2 in enumerate(apData[i1+1:], i1+1):
        if ck_margins(d1,d2): hasNeighbor[i1] = hasNeighbor[i2] = True

for cur, selectCur in zip(apData,hasNeighbor): 
    (selected if selectCur else unselected).append(cur)
```

---

### Suggestion: Iterate through Sorted List

Since you need *both* price and area to be within thresholds, if you sort the list by those fields, then you'll only need to check against the [items before and after][1] as you go down the sorted list <sup>([view results][2])</sup> [time complexity: <kbd>[**O(n\*log<sub>2</sub>n)**](https://realpython.com/sorting-algorithms-python/#measuring-merge-sorts-big-o-complexity)</kbd>].

```py
apSorted = sorted(apData, key=lambda d: [d[k] for k in threshRef])

selected, unselected = [], []
for prev, cur, nxt in zip([{}]+apSorted[:-1], apSorted, apSorted[1:]+[{}]):
    selectCur = any(ck_margins(cur, x) for x in [prev, nxt] if x)
    (selected if selectCur else unselected).append(cur)
```

This would be my preferred way to do it as long as I didn't care about the original order of the list [restoring that would require sorting yet again if this method is used].

[It doesn't matter much unless your list is very large, but] it would use up less memory if you iterated through indices (instead of [zipping](https://docs.python.org/3.3/library/functions.html#zip) shifted copies together):

```py
ap_sort_pad = [{}] + sorted(apData, key=lambda d: [d[k] for k in threshRef]) + [{}]

selected, unselected = [], []
for i in range(len(ap_sort_pad)-2):
    prev, cur, nxt = ap_sort_pad[i:i+3]
    selectCur = any(ck_margins(cur, x) for x in [prev, nxt] if x)
    (selected if selectCur else unselected).append(cur)
```



  [1]: https://i.sstatic.net/1JO3v.png
  [2]: https://i.sstatic.net/PWUPi.png
