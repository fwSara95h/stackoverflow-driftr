---
title: "How to search for a key that is a float using an int that the float would round to"
site: stackoverflow
question_id: 75717254
answer_id: 75728342
url: https://stackoverflow.com/a/75728342
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-14T01:27:03Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75728342/revisions
accepted: true
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: a58601ba5c11d7cbf5a9ec3a5de863e3eb8742aa4564d047b750891084be61c3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-14

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75728342>, 2023-03-14; **accepted**; score 1. Text as retrieved 2026-10-12.

[If I understand correctly, you want help with the `num_find` function.] An integer `num` might have multiple float keys that round to it, so you can return a list of coordinates for keys that round to `num` using [list comprehension](https://www.programiz.com/python-programming/list-comprehension).

```py
def num_find(num):
    knums = [k for k in x_values if round(k)==num] ## random `number`s that round to num
    return [{'value':k, 'x':x_values[k], 'y':y_values[k]} for k in knums] 
```

With the [5x5 plane][1] described below:

```py
numbers = [22, 17, 17, 1, 7, 5, 23, 4, 21, 15, 7, 17, 12, 22, 12, 6, 24, 17, 7, 3, 11, 3, 9, 10, 16]
x_values = { 21.56616443204579: 1, 16.88672504030793: 1, 16.61564085529154: 1, 1.4623292817213773: 1, 7.186315822551395: 1,  5.387703554349793: 2, 23.004220335362547: 2, 4.30105672619399: 2, 20.7082214032309: 2, 15.161515180582256: 2, 7.038981849299793: 3, 17.32470245778697: 3, 11.939846516953184: 3, 
             21.985484460089975: 3, 12.186946846244577: 3, 5.953912098756866: 4, 24.077177195496617: 4, 16.932061089221378: 4, 6.965151311285224: 4, 2.8087793024821837: 4, 10.66278368789144: 5, 3.2461449455136293: 5, 8.615396657669486: 5, 9.667998604001081: 5, 15.636821583006896: 5 }
y_values = { 21.56616443204579: 1, 16.88672504030793: 2, 16.61564085529154: 3, 1.4623292817213773: 4, 7.186315822551395: 5, 5.387703554349793: 1, 23.004220335362547: 2, 4.30105672619399: 3, 20.7082214032309: 4, 15.161515180582256: 5, 7.038981849299793: 1, 17.32470245778697: 2, 
             11.939846516953184: 3, 21.985484460089975: 4, 12.186946846244577: 5, 5.953912098756866: 1, 24.077177195496617: 2, 16.932061089221378: 3, 6.965151311285224: 4, 2.8087793024821837: 5, 10.66278368789144: 1, 3.2461449455136293: 2, 8.615396657669486: 3, 9.667998604001081: 4, 15.636821583006896: 5 }
```

- <kbd>**`num_find(7)`**</kbd> would return 
  > ```py
  > [ {'value': 7.186315822551395, 'x': 1, 'y': 5},
  >   {'value': 7.038981849299793, 'x': 3, 'y': 1},
  >   {'value': 6.965151311285224, 'x': 4, 'y': 4} ]
  > ```
- <kbd>**`num_find(5)`**</kbd> would return `[{'value': 5.387703554349793, 'x': 2, 'y': 1}]`, and
- <kbd>**`num_find(29)`**</kbd> would return `[]` (an empty list because there would be no matches)

---

On another note,

1. It's a bit redundant to have two separate dictionaries (`x_values` and `y_values`) with the exact same set of keys. It might be better to have a dictionary of [`tuple`](https://www.programiz.com/python-programming/tuple)s instead. Instead of *`x_values[number]=num`* and *`y_values[number]=n`* (in *`if number not in numbers...`*), you can just have one dictionary `xy_values` that you fill up with <kbd>**`xy_values[number] = (num, n)`**</kbd>.

2. Since `number` is a float and `numbers` is being built as a list of integers, it's somewhat superfluous to check for *`number not in numbers`*:
    > ```py
    >             if number not in numbers:
    >                 numbers.append(round(number))
    > ``` 
    I know you can't use `if round(number) not in numbers:` since you *want* duplicate integers, but this is only checking against duplicate whole-number keys. The chances of repeating a "random" float (without specifying a limit on the decimal places) is miniscule, but if you're checking against duplicate keys (which you should be, if you don't want to risk losing any coordinates by over-writing them), you should be checking against *all* of them, not just whole numbers. 

I would suggest filling up your "plane" with something like:

```py
xy_values = {} ## instead of `x_values={}` and `y_values={}`

for num in range(1, (y_amount + 1)):
    for n in range(1, (x_amount + 1)):
        number = random.uniform(1, Room_Total)
        while number in xy_values: ## [ `in xy_values` <===> `in xy_values.keys()` ]
            number = random.uniform(1, Room_Total)
        numbers.append(round(number))
        xy_values[number] = (num, n) ## [ only one dictionary to fill ]
```

While `numbers` would be unaffected by this change, `xy_values` for the plane I described as an example above would look like:

>```py
> # xy_values = \
> { 21.56616443204579: (1, 1), 16.88672504030793: (1, 2), 16.61564085529154: (1, 3), 1.4623292817213773: (1, 4), 7.186315822551395: (1, 5),
>   5.387703554349793: (2, 1), 23.004220335362547: (2, 2), 4.30105672619399: (2, 3), 20.7082214032309: (2, 4), 15.161515180582256: (2, 5),
>   7.038981849299793: (3, 1), 17.32470245778697: (3, 2), 11.939846516953184: (3, 3), 21.985484460089975: (3, 4), 12.186946846244577: (3, 5),
>   5.953912098756866: (4, 1), 24.077177195496617: (4, 2), 16.932061089221378: (4, 3), 6.965151311285224: (4, 4), 2.8087793024821837: (4, 5),
>   10.66278368789144: (5, 1), 3.2461449455136293: (5, 2), 8.615396657669486: (5, 3), 9.667998604001081: (5, 4), 15.636821583006896: (5, 5) }
>```

and `num_find` could just be defined as

```py
def num_find(num): 
    return [{'value':k, 'x':x, 'y':y} for k,(x,y) in xy_values.items() if round(k)==num] 
```

[It will produce the same results as before, but will be a bit more efficient since there's only one loop (for going through one dictionary) rather than two loops where you have to loop through a dictionary to gather keys that match, and then loop through the matched keys and fetch values from two separate dictionaries...]

---

In addition, I recommend looking into [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings) and the built-in [`enumerate`](https://www.programiz.com/python-programming/methods/built-in/enumerate) function, and maybe into [conditional expressions](https://python-reference.readthedocs.io/en/latest/docs/operators/ternary.html) as well, because your *`if plane == "y":...`* block can be reduced to:

```py
# plane = input("Want to see the plane? y/n ")
if plane == "y": 
    for n, i in enumerate(numbers, 1):
        print(f'{i:<{length}}', end=' ' if n%y_amount else '\n') 
```

<sup>[You can use `if n%y_amount` instead of `if n%y_amount!=0` as `0` evaluates as `False`.]</sup>

  [1]: https://i.sstatic.net/7fZ2G.png
