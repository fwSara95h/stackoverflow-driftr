---
title: "How can I simplify my dict statements into one statement?"
site: stackoverflow
question_id: 75499914
answer_id: 75501136
url: https://stackoverflow.com/a/75501136
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-02-19T15:17:43Z
last_edited: 2023-02-19T15:23:05Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75501136/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8ed1db4ec7299f8e486c5d0157b437e78802bb91bc94d083b55c4e5f50c86b3c
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-02-19

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75501136>, 2023-02-19, last edited 2023-02-19; score 0. Text as retrieved 2026-10-12.

> *`{'South': 'Dining Room', 'item': 'Helmet', 'East': 'Study', 'item': 'Armor', 'West': 'Balcony’, 'item': 'Dark Knight', ‘North’: ‘Foyer'}`*

the structure suggested in your comment is not valid (as others have already pointed out), but there are still many ways to combine the two dictionaries.

---

#### Suggestion 1: <kbd>room -> direction -> (room, item)</kbd>

```python
rooms_items = {rk: {
    dk: (drv, items.get(drv)) for dk, drv in rv.items()
} for rk, rv in rooms.items()}
```

will have `rooms_items` as

>```python
> { 'Stable': {'West': ('Foyer', 'Shield')},
>   'Foyer': {'South': ('Great Hall', 'Sword')},
>   'Great Hall': {'South': ('Dining Room', 'Helmet'),
>     'East': ('Study', 'Armor'),
>     'West': ('Balcony', 'Dark Knight'),
>     'North': ('Foyer', 'Shield')},
>   'Study': {'North': ('Library', 'Spell Book'),
>     'West': ('Great Hall', 'Sword')},
>   'Dining Room': {'North': ('Great Hall', 'Sword'),
>     'East': ('Kitchen', 'Cooked Chicken')},
>   'Library': {'South': ('Study', 'Armor')},
>   'Kitchen': {'West': ('Dining Room', 'Helmet')},
>   'Balcony': {'East': ('Great Hall', 'Sword')}}
>```

---

#### Suggestion 2: <kbd>room -> {item, direction_room, direction_item}</kbd>

```pythpn
{rk: dict(sorted([
    *[(f'{dk}_room', drv) for dk, drv in rv.items()],
    *[(f'{dk}_item', items.get(drv)) for dk, drv in rv.items()],
    ('item', items.get(rk))
 ], reverse=True)) for rk, rv in rooms.items()}
```

would return

>```python
> { 'Stable': {'item': None, 'West_room': 'Foyer', 'West_item': 'Shield'},
>   'Foyer': {  'item': 'Shield', 
>               'South_room': 'Great Hall', 'South_item': 'Sword'  },
>   'Great Hall': { 'item': 'Sword',
>                   'West_room': 'Balcony', 'West_item': 'Dark Knight',
>                   'South_room': 'Dining Room', 'South_item': 'Helmet',
>                   'North_room': 'Foyer', 'North_item': 'Shield',
>                   'East_room': 'Study', 'East_item': 'Armor' },
>   'Study': {  'item': 'Armor',
>               'West_room': 'Great Hall', 'West_item': 'Sword',
>               'North_room': 'Library', 'North_item': 'Spell Book'  },
>   'Dining Room': {  'item': 'Helmet',
>                     'North_room': 'Great Hall', 'North_item': 'Sword',
>                     'East_room': 'Kitchen', 'East_item': 'Cooked Chicken'  },
>   'Library': {  'item': 'Spell Book',
>                 'South_room': 'Study', 'South_item': 'Armor'  },
>   'Kitchen': {  'item': 'Cooked Chicken',
>                 'West_room': 'Dining Room', 'West_item': 'Helmet'  },
>   'Balcony': {  'item': 'Dark Knight',
>                 'East_room': 'Great Hall', 'East_item': 'Sword'  } }
>```

---

#### Suggestion 3: <kbd>room -> {item, direction -> {room, item}}</kbd>

```python
{rk: {'item':  items.get(rk), **{dk: {
    'room': drv, 'item': items.get(drv)
} for dk, drv in rv.items()}} for rk, rv in rooms.items()}
```

returns

>```python
> { 'Stable': {'item': None, 'West': {'room': 'Foyer', 'item': 'Shield'}},
>   'Foyer': {  'item': 'Shield',
>               'South': {'room': 'Great Hall', 'item': 'Sword'}  },
>   'Great Hall': { 'item': 'Sword',
>                   'South': {'room': 'Dining Room', 'item': 'Helmet'},
>                   'East': {'room': 'Study', 'item': 'Armor'},
>                   'West': {'room': 'Balcony', 'item': 'Dark Knight'},
>                   'North': {'room': 'Foyer', 'item': 'Shield'} },
>   'Study': {  'item': 'Armor',
>               'North': {'room': 'Library', 'item': 'Spell Book'},
>               'West': {'room': 'Great Hall', 'item': 'Sword'}  },
>   'Dining Room': {  'item': 'Helmet',
>                     'North': {'room': 'Great Hall', 'item': 'Sword'},
>                     'East': {'room': 'Kitchen', 'item': 'Cooked Chicken'}  },
>   'Library': {  'item': 'Spell Book',
>                 'South': {'room': 'Study', 'item': 'Armor'}  },
>   'Kitchen': {  'item': 'Cooked Chicken',
>                 'West': {'room': 'Dining Room', 'item': 'Helmet'}  },
>   'Balcony': {  'item': 'Dark Knight',
>                 'East': {'room': 'Great Hall', 'item': 'Sword'}  } }
>```

---

Once you decide on a [valid] structure for the combined data, you can figure out how to build it.
