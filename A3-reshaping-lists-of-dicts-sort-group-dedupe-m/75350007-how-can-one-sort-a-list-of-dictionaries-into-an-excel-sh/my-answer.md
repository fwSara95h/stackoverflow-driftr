---
title: "How can one sort a list of dictionaries into an excel sheet such that each unique key and one corresponding key are placed into columns?"
site: stackoverflow
question_id: 75350007
answer_id: 75351812
url: https://stackoverflow.com/a/75351812
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-05T11:14:41Z
last_edited: 2023-02-05T21:06:52Z
revisions: 3
revision_history: https://stackoverflow.com/posts/75351812/revisions
accepted: true
score: 2
chapter: A3
chapter_title: "Reshaping lists of dicts: sort, group, dedupe, merge"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 17fcb54360b875ec50de8dedb9949826904503005a16e525d40fca0053751408
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75351812>, 2023-02-05, last edited 2023-02-05; **accepted**; score 2. Text as retrieved 2026-10-12.

With `pandas`, you can use something like this function 

```python
def groupItems(dictList, itemsFrom, groupBy, saveTo=None):
    ik, gk, colsDict = itemsFrom, groupBy, {}
    groups = {str(d.get(gk)): d.get(gk) for d in dictList} 
    itemsList = [ [d.get(ik) for d in dictList if str(d.get(gk))==g] 
                  for g in groups   ]

    maxRows = max(len(li) for li in itemsList) if groups else 0
    for gi, (g, li) in enumerate(zip(groups.keys(), itemsList), 1):
        colsDict[f'Group {gi}'] = [groups[g]] + [None]*(maxRows-1)
        colsDict[f'Group {gi} Items'] = li + [None]*(maxRows-len(li))
    
    rdf = pandas.DataFrame(colsDict)
    if saveTo and isinstance(saveTo, str):
        print('Saving', maxRows, 'rows for', len(groups),'groups to', saveTo)
        rdf.to_csv(saveTo, index=False)
    return rdf
```

Calling <kbd>**`groupItems(listofdictionaries, 'key1', 'key2', 'x.csv')`**</kbd> will save the DataFrame from the screenshot below to `x.csv`.

[![dfop1][1]][1]
**<sub>To demonstrate that the brackets were not lost:</sub>**
[![opmd1][2]][2]

---

You could also get it in [this format][3] if you change the function to

```python
def groupItems(dictList, itemsFrom, groupBy, saveTo=None):
    ik, gk = itemsFrom, groupBy
    groups = {str(d.get(gk)): d.get(gk) for d in dictList} 
    itemsList = [ [d.get(ik) for d in dictList if str(d.get(gk))==g] 
                  for g in groups   ]

    maxRows = max(len(li) for li in itemsList) if groups else 0
    
    colsDict = {f'Group {gi}': [groups[g]] + [None] + (
        [f'Group {gi} Items'] + li + [None]*(maxRows-len(li))
    ) for gi, (g, li) in enumerate(zip(groups.keys(), itemsList), 1)}
    rdf = pandas.DataFrame(colsDict) 

    if saveTo and isinstance(saveTo, str):
        print('Saving', maxRows+4, 'rows for', len(groups),'groups to', saveTo)
        rdf.to_csv(saveTo, index=False)
    return rdf
```

---

##### NOTE: Saving as csv will [stringify all non-numeric cells][4]. If you want to preserve nested structure, I suggest [saving as JSON](https://docs.python.org/3/library/json.html#json.dump) instead.


  [1]: https://i.sstatic.net/3eRN6.png
  [2]: https://i.sstatic.net/AAZpd.png
  [3]: https://i.sstatic.net/70Wty.png
  [4]: https://i.sstatic.net/MTZ7O.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[David Leal](https://stackoverflow.com/users/6237093)** (2023-02-05): Quick note, as per question expected output, the brackets in **GroupX** columns are part of the output, so instead of `1,2,3` it should be `[1,2,3]` for example.
- **me** (2023-02-05): @DavidLeal Thanks [I hadn't noticed before] but the brackets disappeared just because of how DataFrames get displayed - if you print the markdown or view the CSV, the brackets are still there
