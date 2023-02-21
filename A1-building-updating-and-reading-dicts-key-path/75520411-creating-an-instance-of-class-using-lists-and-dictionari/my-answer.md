---
title: "Creating an instance of class using lists and dictionaries"
site: stackoverflow
question_id: 75520411
answer_id: 75524347
url: https://stackoverflow.com/a/75524347
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-21T18:11:03Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75524347/revisions
accepted: true
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: abfe0461dc7d5a1fac5e2c9fd003ce71d07a11f1b7247d45136020627d60251f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-21

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75524347>, 2023-02-21; **accepted**; score 0. Text as retrieved 2026-10-12.

> *@Driftr95, I have different processing times & electricity consumption for each id. How do I call that?*

Not sure exactly what you're going for, but I'll suggest 2 solutions based on the assumption that your current data looks something like

```py
equipments = ['EAF1','EAF2','AOD1', 'AOD2','LF1','LF2']
procTimes = {"1": 80.0, "2": 40.0}
eleCon = {"1": 34.0, "2": 49.0}
```

---

### Suggestion 1

If you just want to avoid the error, you can simply shift all arguments ahead of *`**kwargs`* as it should be.

```py
class Tasks():
    def __init__(self, equipment, id, processingtime:dict={}, electricityconsumption:dict={}, **kwargs):
        self.equipment = equipment
        self.id = id
        for key,value in kwargs.items():
            setattr(self,key,value)
        self.processingtime = processingtime.get(id)
        self.electricityconsumtption = electricityconsumption.get(id)

tasksList = [
    Tasks(taskEq, str(taskId), procTimes, eleCon, kwarg1=f'kw1_{taskId}', kwarg2=f'kw2_{taskId}') 
    for taskId, taskEq in enumerate(equipments, 1)
]
```

[![opkw][1]][1]

---

### Suggestion 2 

```py
class Task():
    def __init__(self, id, equipment, **kwargs):
        self.id=id
        self.equipment=equipment
        for key,value in kwargs.items(): setattr(self,key,value)
```

<sup>I moved `id` ahead of `equipment` just because id is often the first parameter, but it doesn't really matter much.</sup> 

Then you can produce a list (`tasksList`) of 6 `Task` objects with

```py
## Task(task_id,task_eq,processingtime=...,electricityconsumption=...) # <-- format
tasksList = [Task(
    str(taskId), taskEq, 
    processingtime=procTimes.get(str(taskId)), 
    electricityconsumption=eleCon.get(str(taskId))    
) for taskId, taskEq in enumerate(equipments, 1)]
```

[![op][2]][2]


  [1]: https://i.sstatic.net/rc3h9.png
  [2]: https://i.sstatic.net/97hpn.png
