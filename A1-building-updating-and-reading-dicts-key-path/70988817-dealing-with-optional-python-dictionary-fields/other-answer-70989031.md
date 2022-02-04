---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 70989031
url: https://stackoverflow.com/a/70989031
author: "ggorlen"
author_url: https://stackoverflow.com/users/6243352
posted: 2022-02-04T15:39:28Z
last_edited: 2022-02-04T16:09:02Z
accepted: false
score: 5
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: fd7f4f1af41f51cd2163372ab032ae230c8a06b67eefc34542fc88273e2659b3
role: another answer on the same question, kept as context; not my work
---

# Answer by [ggorlen](https://stackoverflow.com/users/6243352) — 2022-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/70989031>, 2022-02-04, last edited 2022-02-04. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

In your code here:

```python
try:
    value1 = dictionary2.get("optional").get("value1")
except AttributeError:
    value1 = " "
```

You can use brackets and `except KeyError`:

```python
try:
    value1 = dictionary2["optional"]["value1"]
except KeyError:
    value1 = " "
```

If this is too verbose for the caller, add a helper:

```python
def get_or_default(d, *keys, default=None):
    try:
        for k in keys:
            d = d[k]
    except (KeyError, IndexError):
        return default
    return d

if __name__ == "__main__":
    d = {"a": {"b": {"c": [41, 42]}}}
    print(get_or_default(d, "a", "b", "c", 1)) # => 42
    print(get_or_default(d, "a", "b", "d", default=43)) # => 43
```

You could also subclass dict and use tuple bracket indexing, like NumPy and Pandas:

```python
class DeepDict(dict):
    def __init__(self, d, default=None):
        self.d = d
        self.default = default

    def __getitem__(self, keys):
        d = self.d
        try:
            for k in keys:
                d = d[k]
        except (KeyError, IndexError):
            return self.default
        return d

    def __setitem__(self, keys, x):
        d = self.d
        for k in keys[:-1]:
            d = d[k]
        d[keys[-1]] = x

if __name__ == "__main__":
    dd = DeepDict({"a": {"b": {"c": [42, 43]}}}, default="foo")
    print(dd["a", "b", "c", 1]) # => 43
    print(dd["a", "b", "c", 11]) # => "foo"
    dd["a", "b", "c", 1] = "banana"
    print(dd["a", "b", "c", 1]) # => "banana"
```

But there might be an engineering cost to this if it's confusing for other developers, and you'd want to flesh out the other expected methods as described in [How to "perfectly" override a dict?](https://stackoverflow.com/questions/3387691/how-to-perfectly-override-a-dict) (consider this a proof-of-concept sketch). It's best not to be too clever.
