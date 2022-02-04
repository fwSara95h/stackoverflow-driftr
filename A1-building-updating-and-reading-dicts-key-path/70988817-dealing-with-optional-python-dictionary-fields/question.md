---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
url: https://stackoverflow.com/q/70988817
asked: 2022-02-04T15:23:14Z
asked_by: "c8999c 3f964f64"
asked_by_url: https://stackoverflow.com/users/11803687
last_edited: 2023-02-15T17:26:51Z
last_editor: "ggorlen"
last_editor_url: https://stackoverflow.com/users/6243352
tags: [python, json, dictionary, attributeerror]
score: 6
views_at_snapshot: 3340
answer_count: 6
accepted_answer_id: 70988947
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b208f0f552c95b278107a0529ad7f2f6c9f2a0857c22a62045780ddea2d3d691
---

# Dealing with optional python dictionary fields

Asked by [c8999c 3f964f64](https://stackoverflow.com/users/11803687) on Stack Overflow, <https://stackoverflow.com/q/70988817>, 2022-02-04, last edited 2023-02-15 by [ggorlen](https://stackoverflow.com/users/6243352). Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I'm dealing with JSON data which I load into Python dictionaries. A lot of these have optional fields, which then may contain dictionaries, that kind of stuff.

    dictionary1 = 
    {"required": {"value1": "one", "value2": "two"},
    "optional": {"value1": "one"}}

    dictionary2 = 
    {"required": {"value1": "one", "value2": "two"}}

If I do this,

    dictionary1.get("required").get("value1")

this works, obviously, because the field `"required"` is always present.

However, when I use the same line on `dictionary2` (to get the optional field), this will produce an `AttributeError`

    dictionary2.get("optional").get("value1")
    AttributeError: 'NoneType' object has no attribute 'get'

which makes sense, because the first `.get()` will return `None`, and the second `.get()` cannot call `.get()` on the None object.

I can solve this by giving default values in case the optional field is missing, but this will be annoying the more complex the data gets, so I'm calling this a "naive fix":

    dictionary2.get("optional", {}).get("value1", " ")

So the first `.get()` will return an empty dictionary `{}`, on which the second `.get()` can be called, and since it obviously contains nothing, it will return the empty string, as defined per the second default.

This will no longer produce errors, but I was wondering if there is a better solution for this - especially for more complex cases (`value1` containing an array or another dictionary, etc....)

I could also fix this with try - except `AttributeError`, but this is not my preferred way either. 

    try:
        value1 = dictionary2.get("optional").get("value1")
    except AttributeError:
        value1 = " "

I also don't like checking if optional field exists, this produces garbage code lines like

    optional = dictionary2.get("optional")
    if optional:
        value1 = optional.get("value1")
    else:
        value1 = " "

which seems very non-Pythonic...

I was thinking maybe my approach of just chaining `.get()`s is wrong in the first place?

## Comments on the question

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Darina](https://stackoverflow.com/users/4916075)** (2022-02-04): Why don't you like the try-except clause? It's the most pythonic way of approaching this and easiest to read.
- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): just creates lines of code... I was looking for a one-liner I guess. (the code would be littered with try-except blocks)
- **[ggorlen](https://stackoverflow.com/users/6243352)** (2023-02-15): @c8999c3f964f64 thanks for sharing your solution, but typically that should be posted as an answer rather than an edit to the question. I removed it but feel free to post it as an answer. Thanks.
