---
title: "Check a subkey value using a random variable and a condition. KeyError: \"x\""
site: stackoverflow
question_id: 75851646
answer_id: 75851696
url: https://stackoverflow.com/a/75851696
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-27T02:27:40Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75851696/revisions
accepted: true
score: 2
chapter: A1
chapter_title: "Building, updating and reading dicts: key paths and defaults"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: c06da484b3204bafdad2e900d329f76d228b440bc7c5f32c2f42fbef28ff9e6f
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-27

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75851696>, 2023-03-27; **accepted**; score 2. Text as retrieved 2026-10-12.

> I think the problem is the row `if random_data == data["gender"]["male"]`, so I get the error:
>
> ```
> KeyError: "gender"
> ```

`"gender"` is a *nested* key - i.e., it's not in `data.keys()` <sup>*`['escritorio', 'viento', 'silla', 'mesa']`*</sup>, and `"male"` is not a key anywhere at all [it's a value paired to `"gender"`]. What you want is probably something like:

```py
if data[random_data]["gender"] == "male":
    print(random_data, ": word is Male")
else:
    print(random_data, ": word is Female") 
```

or, using the [ternary operator](https://book.pythontips.com/en/latest/ternary_operators.html#ternary-operators):

```py
print(random_data, ": word is", "Male" if data[random_data]["gender"]=="male" else "Female")
```

---

You actually don't even need conditions though - you can just have

```py
print(random_data, ": word is", data[random_data]["gender"].capitalize())
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Evangelos Dellas](https://stackoverflow.com/users/21374650)** (2023-03-27): Thank you! I accept your answer
