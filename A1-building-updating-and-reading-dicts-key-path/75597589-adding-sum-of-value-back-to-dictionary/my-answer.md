---
title: "Adding sum of value back to Dictionary"
site: stackoverflow
question_id: 75597589
answer_id: 75651237
url: https://stackoverflow.com/a/75651237
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-06T13:06:46Z
last_edited: 2023-03-06T13:16:52Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75651237/revisions
accepted: false
score: 0
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b47ff4f6408ba1ea5fc086ab49c6459a19a204c824f23c5881c608abc3741c8f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-06

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75651237>, 2023-03-06, last edited 2023-03-06; score 0. Text as retrieved 2026-10-12.

> *I'm trying to add 100 to the values.*
> 
> ```python
> for value in artist_dict.values():
>   value += 100
> ```

When looping like this, `value` is just a **copy** of the respective item in `artist_dict.values()`, and has no effect on the actual `artist_dict` at all.

<sup>[For lists, you might use [`enumerate`](https://www.programiz.com/python-programming/methods/built-in/enumerate) for something like this, but with a dictionary,]</sup> you can instead loop through the keys and access and increment the values via each key.

```python
for k in artist_dict:
    artist_dict[k] += 100
```

For more information see the [python docs](https://docs.python.org/3/library/stdtypes.html#frozenset.clear) on `dict`; but basically,  *`for k in artist_dict`* does the same as `for k in artist_dict.keys()`, and the loop above effectively does the same as <kbd>`for k, v in artist_dict.items(): artist_dict[k] = v + 100`</kbd>.

---
---

> *...and received an error message.  Also, ...all received an error message.*

<sup>You should always include in your question what error messages you received, but in this particular case they're not hard to guess.</sup>

---

> I tried `.append(value)`

> `artist_dict.updated(value +=100)`

Dictionaries don't have those methods, so you can't apply them to `artist_dict`.

---

> `artist_dict.update(value)`

You need to send another dictionary as the argument in `.update`.

---

> `artist_dict.values() = value`

Afaik `.values()` can only be read, not set.
