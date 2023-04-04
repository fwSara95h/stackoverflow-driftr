---
title: "Stuck on this function"
site: stackoverflow
question_id: 75925033
answer_id: 75926769
url: https://stackoverflow.com/a/75926769
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-04T07:48:32Z
last_edited: 2023-04-04T07:54:50Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75926769/revisions
accepted: false
score: 1
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ac632278b8618a350b92fb9fd48e65dad6deddcce6bfd2c329ca1b38a08d5b0
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75926769>, 2023-04-04, last edited 2023-04-04; score 1. Text as retrieved 2026-10-12.

You were on the right track with nested for-loops, but

> ```py
>     num_ended_games = 0 ## beginning of loop
> ```
> ```py
>         key = (move, num_ended_games)
>         if key not in current_dict:
> ``` 
> ```py
>     num_ended_games += 1 ## end of loop
> ```

Incrementing `num_ended_games` at the end of loop without setting it anywhere does not update it in the `result` dictionary. To [change a dictionary key](https://stackoverflow.com/a/4406521/6146136) you need to set the old value to the new key and [`del`](https://www.programiz.com/python-programming/del) or [`.pop`](https://www.programiz.com/python-programming/methods/dictionary/pop) the old key. Also, keep in mind that tuples are [not mutable](https://realpython.com/python-mutable-vs-immutable-types/#mutability-vs-immutability) in python, so to change one value in a tuple, you need to replace the whole tuple...

Try something like the version of `moves_to_nested_dict` below. <sup>([view example outputs][1])</sup>

```py
def moves_to_nested_dict(moves: list[list[str]]) -> dict[tuple[str,int], dict]:
    result = {}
    for game_moves in moves:
        cur_dict = result

        for reverse_index, move in enumerate(game_moves, 1-len(game_moves)):
            cur_key = [k for k in cur_dict if k[0]==move]            
            if not cur_key: cur_dict[(cur_key := (move, 0))] = {}
            else: cur_key = cur_key[0]
            
            if not reverse_index: ## <-- reverse_index=0 on last move
                cur_dict[(move, cur_key[1]+1)] = cur_dict.pop(cur_key)
            else: cur_dict = cur_dict[cur_key]
    return result
```

<sup>[Using [`enumerate`](https://www.programiz.com/python-programming/methods/built-in/enumerate) with `start=1-len` makes `reverse_index` count starting from `1-len` and ending at 0 - so we can use that to keep track of how many moves are left and when we're on the last move; and the [walrus operator](https://realpython.com/python-walrus-operator/#walrus-operator-fundamentals) (`:=`) is just a handy way of defining/updating and using a variable in one statement instead of needing an extra line to set it first before using it.]</sup>

<br>

---

<br>

Btw, this would be much simpler if `num_ended_games` was a value *inside* the dictionary so that just `move` could be used as the key, and you could just use [`.setdefault`](https://www.programiz.com/python-programming/methods/dictionary/setdefault) instead of needing to check for and sometimes update the key:

```py
def moves_to_nested_dict(moves: list[list[str]]) -> dict[str,dict]:
    result = {}
    for game in moves:
        cur_dict = result
        for move in game: 
            cur_dict = cur_dict.setdefault(move, {'__games_ended__':0}) # (move,{})
        if game: cur_dict['__games_ended__'] = cur_dict.get('__games_ended__',0)+1
    return result
```

<sup>[Using [`<dict>.get(<key>)`](https://www.programiz.com/python-programming/methods/dictionary/get) is safer than `<dict>[<key>]` when you can't be sure that the key exists.]</sup>

With this version,

```py
moves_to_nested_dict([['a','b'], ['a','b'], ['a','b','c'], ['d','a'], ['a','d']])
```

would return

> ```py
> {
>   'a': {
>     '__games_ended__': 0,
>     'b': {'__games_ended__': 2, 'c': {'__games_ended__': 1}},
>     'd': {'__games_ended__': 1}
>   },
>   'd': {'__games_ended__': 0, 'a': {'__games_ended__': 1}}
> }
> ```

  [1]: https://i.sstatic.net/lZzKi.png
