---
title: "Python - sort list of objects by one of the obj attributes and then by dict value"
site: stackoverflow
question_id: 75637403
url: https://stackoverflow.com/q/75637403
asked: 2023-03-04T17:31:55Z
asked_by: "ddoch003"
asked_by_url: https://stackoverflow.com/users/19971042
last_edited: never
tags: [python, list, dictionary, sorting, object]
score: -1
views_at_snapshot: 92
answer_count: 1
accepted_answer_id: none
closed: 2023-03-06T07:39:48Z (Duplicate)
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 282ee58c41afd636fdaaec580949dd4926c1656a0000a5edee5d36585e0567ec
---

# Python - sort list of objects by one of the obj attributes and then by dict value

Asked by [ddoch003](https://stackoverflow.com/users/19971042) on Stack Overflow, <https://stackoverflow.com/q/75637403>, 2023-03-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Literally need correction in only one line of the code below. Everything in the code works fine except for line: `dwarfs.sort(key=lambda x:-x.physics)` which is incomplete.
After creating the objects and appending them in the list `dwarfs` and keeping track of the colors in the `colors` dictionary I want to sort the objects by: `self.physics` and then, if multiple with the same value, by appearance of the `color` in `colors` dictionary.
With my current code when entering
```
Grumpy <:> Red <:> 5000
Grumpy <:> Blue <:> 10000
Grumpy <:> Red <:> 10000
Happy <:> Blue <:> 10000
Once upon a time
```
I would like to receive:
```
(Blue) Grumpy <-> 10000
(Blue) Happy <-> 10000
(Red) Grumpy <-> 10000
```
Instead I have:
```
(Blue) Grumpy <-> 10000
(Red) Grumpy <-> 10000
(Blue) Happy <-> 10000
```

Code:
```
class Dwarf:
    def __init__(self,name,hat_color,physics:int):
        self.name=name
        self.hat_color=hat_color
        self.physics=physics

    def __repr__(self):
        return f"({self.hat_color}) {self.name} <-> {self.physics}"

dwarfs=[]
colors={}

while True:
    entry=input()
    if entry=="Once upon a time":
        break
    name,hat_color,physics=entry.split(" <:> ")
    physics=int(physics)
    obj=Dwarf(name,hat_color,physics)
    tracker=None
    if len(dwarfs)==0:
        dwarfs.append(obj)
    else:
        for i in dwarfs:
            if name==i.name and hat_color==i.hat_color:
                tracker=i
                break
        if tracker!= None:
            dwarfs.remove(tracker)
        dwarfs.append(obj)
    if hat_color not in colors:
        colors[hat_color]=1
    else:
        if tracker is None:
            colors[hat_color]+=1

colors={k:v for k,v in sorted(colors.items(),key=lambda x:-x[1])}
dwarfs.sort(key=lambda x:-x.physics)

for dwarf in dwarfs:
    print(dwarf)
```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Kelly Bundy](https://stackoverflow.com/users/12671057)** (2023-03-04): Please make your [mre] minimal. Unless you have a problem with the code that *creates* the dicts, hardcode an example instead.
