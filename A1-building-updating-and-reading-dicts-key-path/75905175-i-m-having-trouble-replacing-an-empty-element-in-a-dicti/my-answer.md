---
title: "I'm having trouble replacing an empty element in a dictionary in python 3.7"
site: stackoverflow
question_id: 75905175
answer_id: 75912007
url: https://stackoverflow.com/a/75912007
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T12:26:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75912007/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: f6a5a5e1949fda076790434def7c825ef8c03580f6be7736a1cc4701255d9f3d
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75912007>, 2023-04-02; score 0. Text as retrieved 2026-10-12.

If you use [dictionary comprehension](https://www.programiz.com/python-programming/dictionary-comprehension) with [formatted strings](https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/), you can loop through the [keys](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) to build `A` directly without even initiating it with empty values.<sup>([view example][1])</sup>

```py
# keys_A = [*A] ## if you already have A from a previous block
keys_A = ['name', 'age', 'tasks done', 'number of tasks done']

# print("hello 'Worker'")
# time.sleep(2)

A = {k:input(f'enter {k}') for k in keys_A}
```

<br>

---
---

<br>

If you want values of specific types, you can use a [`try...except...else`](https://www.geeksforgeeks.org/try-except-else-and-finally-in-python/) to convert the input and [`isinstance`](https://www.programiz.com/python-programming/methods/built-in/isinstance) to check against the type.<sup>([view example][2])</sup>

```py
# ref_A = {k:type(v) for k,v in A.items()} ## if you already have A from a previous block
ref_A = {'name': str, 'age': int, 'tasks done': str, 'number of tasks done': int}

# print("hello 'Worker'")
# time.sleep(2)

A = {} ## [ not necessary if you already have A ]
for k, t in ref_A.items():
    while not isinstance((inp:=input(f'enter {k}: ')), t):
        try: inp = t(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
        else: break
    A[k] = inp
```

<sup>[The [walrus operator](https://realpython.com/python-walrus-operator/#walrus-operator-fundamentals) (`:=`) conveniently eliminates that extra line for initiating a variable that will only be used conditionally.]</sup>

---

You can also put the `try...except` in a [function](https://www.programiz.com/python-programming/function) so that you don't need you can go back to using a dict comprehension instead of a [`for`-loop](https://www.programiz.com/python-programming/for-loop).<sup>([view example][3])</sup>

```py
def validated_input(promptStr:str, inp_type:type=str):
    while not isinstance((inp:=input(promptStr)), inp_type):
        try: return inp_type(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
    return inp
```

```py
A = {k: validated_input(f'enter {k}: ', t) for k, t in ref_A.items()}

## if you already have A and you just want to update the keys in ref_A:
# for k, t in ref_A.items(): A[k] = validated_input(f'enter {k}: ', t) ## OR
# A = {**A, **{k: validated_input(f'enter {k}: ', t) for k, t in ref_A.items()}}
```

<br>

---

<br>

You can also write a function to take in a list of inputs

```py
def list_input(itemName:str):
    inps = [] 
    promptStr = f'Enter a {itemName} to add [Or just press ENTER to stop]: ' 
    while (inp:=input(promptStr)).strip(): inps.append(inp)
    return inps
```

and then alter `validated_input` to utilize it [conditionally ofc]

```py
def validated_input(promptStr:str, inp_type:type=str):
    if inp_type in [list, tuple, set]:
        return inp_type(list_input(promptStr))
    while not isinstance((inp:=input(promptStr)), inp_type):
        try: return inp_type(inp)
        except ValueError as ve: print('! Invalid Input -', ve, '!')
    return inp
```

and then you could have `tasks done` as a list and calculate its length for `number of tasks done`.<sup>([view example][4])</sup>

```py
A =  {'name': input('enter name: ')} ## A['name']=input('enter name: ') # if A exists
A['age'] = validated_input('enter age: ', int)
A['tasks done'] = list_input('"task done"') # validated_input('"task done"', list)
A['number of tasks done'] = len(A['tasks done']) 
```


  [1]: https://i.sstatic.net/AYLXy.png
  [2]: https://i.sstatic.net/Di93k.png
  [3]: https://i.sstatic.net/d3r7r.png
  [4]: https://i.sstatic.net/GlbtR.png
