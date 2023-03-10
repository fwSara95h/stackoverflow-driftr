---
title: "Ordering keys in a dictionary"
site: stackoverflow
question_id: 75700999
url: https://stackoverflow.com/q/75700999
asked: 2023-03-10T21:03:18Z
asked_by: "rithvik"
asked_by_url: https://stackoverflow.com/users/19370127
last_edited: 2023-03-11T07:34:00Z
last_editor: "Anthon"
last_editor_url: https://stackoverflow.com/users/1307905
tags: [python, dictionary]
score: 0
views_at_snapshot: 84
answer_count: 2
accepted_answer_id: 75702903
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b5ef3382c97cbad2756939362f0d30c58d785b08f59bca666dfedcef380a3239
---

# Ordering keys in a dictionary

Asked by [rithvik](https://stackoverflow.com/users/19370127) on Stack Overflow, <https://stackoverflow.com/q/75700999>, 2023-03-10, last edited 2023-03-11 by [Anthon](https://stackoverflow.com/users/1307905). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

Given a dictionary loaded from the following YAML:

```yaml
song1:
  chunk1:
    attr1: value
    attr2: value
    attr3: value
  chunk2:
    attr1: value
    attr2: value
    attr3: value
  chunk3:
    attr1: value
    attr2: value
    attr3: value
song2:
  chunk1:
    attr1: value

... and so on
```

How can one go about reordering the keys to get something like this:

```yaml
attr1:
  song1:
    chunk1: value
    chunk2: value
    chunk3: value
  song2:
    chunk1: value
    chunk2: value
    chunk3: value
  song3:
    chunk1: value
    chunk2: value
    chunk3: value
attr2:

... and so on
```

I think I know how to do this but I wanted to look for any optimized methods to solve this, preferably in Python using YAML but general solutions also welcome. Additionally, what is the name of this type of problem?

Edit: a rudimentary solution with python dictionaries, but I was wondering if there's any other way apart from a brute force approach to this:

```python
reordered = {}
for song_name in output.keys():
    for chunk_name in output[song_name].keys():
        for attr_name in output[song_name][chunk_name].keys():
            if attr_name not in reordered:
                reordered[attr_name] = {}
            if song_name not in reordered[attr_name]:
                reordered[attr_name][song_name] = {}
            reordered[attr_name][song_name][chunk_name] = output[song_name][chunk_name][attr_name]

```

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[njzk2](https://stackoverflow.com/users/671543)** (2023-03-10): in principle, it makes little sense, as the order has no meaning in a yaml object. In practice, https://stackoverflow.com/questions/8651095/controlling-yaml-serialization-order-in-python and https://stackoverflow.com/questions/40226610/ruamel-yaml-equivalent-of-sort-keys
- **[njzk2](https://stackoverflow.com/users/671543)** (2023-03-10): Does this answer your question? [Controlling Yaml Serialization Order in Python](https://stackoverflow.com/questions/8651095/controlling-yaml-serialization-order-in-python)
- **[rithvik](https://stackoverflow.com/users/19370127)** (2023-03-10): I checked over these threads but they don't seem to be pertinent. I'm not looking for the specific ordering of objects in the same key-pair level, I'm looking for how to rearrange keys across dictionary levels if that makes more sense. So if the original dictionary schema is `song : { chunk : { attr : values} }` I want to change this to `attr : { song : { chunk : values } }`
- **[njzk2](https://stackoverflow.com/users/671543)** (2023-03-10): oh, my bad. In that case, maybe something with de-grouping and re-grouping the values. I assume pandas can do that
- **[rithvik](https://stackoverflow.com/users/19370127)** (2023-03-10): Could you share some links regarding that, or make an answer to this post? Would appreciate it, I left an edit on my og post showing what the brute force solution is and asked if there's a better way of doing it
- **[JonSG](https://stackoverflow.com/users/218663)** (2023-03-10): check out `setdefault()` to clean this up a bit.
- **[rithvik](https://stackoverflow.com/users/19370127)** (2023-03-11): setdefault() doesn't work in this situation because it either returns a value given a key or adds a key-value pair, none of which I want to do.
- **[Anthon](https://stackoverflow.com/users/1307905)** (2023-03-11): As you only load your data structure from YAML, and then work on that data structure applying the tag [tag:yaml] is inappropriate ( as would be adding [tag:ascii] even though it looks like you have ASCII input ).
