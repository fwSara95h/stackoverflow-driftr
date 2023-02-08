---
title: "How to increase efficiency of rename files by dictionary value according to keywords(keys) from dictionary?"
site: stackoverflow
question_id: 75385824
answer_id: 75391748
url: https://stackoverflow.com/a/75391748
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-08T21:08:15Z
last_edited: 2023-02-09T15:04:15Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75391748/revisions
accepted: true
score: 0
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1e42fe80af612c6e051b404f237f360bdf142a1b71155288332565327c27b3a1
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75391748>, 2023-02-08, last edited 2023-02-09; **accepted**; score 0. Text as retrieved 2026-10-12.

I don't know anyway to get all the `file_names` without nested for loops, but you should `break` after `os.rename(old_name, new_name)`, because there's no point in renaming the same file multiple times (and wouldn't it raise [`FileNotFoundError`][1] after the first renaming since there will no longer be a file named `file_name` in that directory?). And also, using [`for...else`](https://book.pythontips.com/en/latest/for_-_else.html#else-clause) (instead of `if...else` inside *`for keyWords...`*) would keep the same `file_name` from being printed multiple times.

```python
for (dir_path, dir_names, file_names) in walk(dir_path):
    for file_name in file_names:
        for keyWords in nameKeyWords:
            if keyWords in file_name:
                old_name = os.path.join(dir_path,file_name)
                new_name = os.path.join(dir_path,nameKeyWords.get(keyWords)+'.csv')
                os.rename(old_name, new_name)
                break ## [ no need to keep checking ]
        else: print(file_name) ## [ only prints if for never breaks ]

```

---

If you just want to decrease the level of nesting in your innermost loop, you can separate the loops:

```python
fNameGenerator = (
    (dPath, fName) for dPath, dnames, fNames
    in os.walk(dir_path) for fName in fNames
)

for dPath, file_name in fNameGenerator:
    for keyWords in nameKeyWords:
        if keyWords in file_name:
            new_name = os.path.join(dPath, f'{nameKeyWords.get(keyWords)}.csv')
            os.rename(os.path.join(dPath, file_name), new_name)
            break
    else: print(file_name)
```

---

You could also get `new_name`s within `fNameGenerator`

```python
# nameKeyWords = {....}
def getNewFn(oldFn:str):
    for k in nameKeyWords:
        if k in oldFn: return f"{nameKeyWords[k]}.csv"

fNameGenerator = (
    (dPath, fName, getNewFn(fName)) for dPath, dnames, fNames 
    in os.walk(dir_path) for fName in fNames
)

for dPath, file_name, new_name in fNameGenerator:
    if new_name is None: print(file_name)
    else: os.rename(*[os.path.join(dPath, fn) for fn in [file_name, new_name]]) 
```

---
---

**Please note that none of these have decreased the complexity**, and the nested loops might actually be the fastest alternative [although none of them seem take up significantly less time that the rest].

  [1]: https://i.sstatic.net/HS6S5.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Victor Pan](https://stackoverflow.com/users/21093275)** (2023-02-09): Thanks, this is exactly what I am looking for. I am a python self-learning new starter, can you explain how the 'fNameGenerator' works? I am still very confused about how 'fNamegenerator' works after I did some research about the generator functions.
- **me** (2023-02-09): @VictorPan It's a generator expression for a [flattened list that used to be nested](https://stackoverflow.com/a/25674934/6146136). If you use square brackets (like `[(...,fName,...) for ...,fNames in os.walk(dir_path) for fName in fNames]`) it becomes [list comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp). Using the generator is more memory-efficient (but not necessarily faster) so I don't think it'll make much of a difference unless you have LOTS of files. Read [this blog](https://codete.com/blog/python-basics-generator-expressions-and-comprehensions) for more
