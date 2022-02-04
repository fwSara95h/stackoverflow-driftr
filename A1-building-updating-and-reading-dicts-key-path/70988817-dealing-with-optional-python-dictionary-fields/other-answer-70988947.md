---
title: "Dealing with optional python dictionary fields"
site: stackoverflow
question_id: 70988817
answer_id: 70988947
url: https://stackoverflow.com/a/70988947
author: "Ben Grossmann"
author_url: https://stackoverflow.com/users/2476977
posted: 2022-02-04T15:32:21Z
last_edited: 2022-02-04T15:50:04Z
accepted: true
score: 1
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: dde9822313e0a9415f5b5236b74d5b06dda17666b0562f0b34a06651f2501ceb
role: another answer on the same question, kept as context; not my work
---

# Answer by [Ben Grossmann](https://stackoverflow.com/users/2476977) — 2022-02-04

Posted on Stack Overflow, <https://stackoverflow.com/a/70988947>, 2022-02-04, last edited 2022-02-04; accepted answer. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

First of all, you refer to `" "` as the empty string. This is incorrect; `""` is the empty string.

Second, if you're checking for membership, I don't see a reason to use the `get` method in the first place. I'd opt for something like the following.

    if "optional" in dictionary2:
        value1 = dictionary2["optional"].get("value1")
    else:
        value1 = ""


-----

Another alternative to consider (since you're using the `get` method a lot) is to switch to the `defaultdict` class. For example, 

    from collections import defaultdict
    
    dictionary2 = {"required": {"value1": "one", "value2": "two"}}
    ddic2 = defaultdict(dict,dictionary2)
    value1 = ddic2["optional"].get("value1")

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): correct on the empty string, my bad. checking if optional is in the dictionary first will  create a lot of extra lines of code. This becomes somewhat unmanageable the more checks there are...
- **[Ben Grossmann](https://stackoverflow.com/users/2476977)** (2022-02-04): @c See my edit: maybe it would be helpful to start using defaultdicts.
- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): defaultdict seems great, can you explain why it doesnt work with .get("optional"), but only when I use ["optional"] ?
- **[Ben Grossmann](https://stackoverflow.com/users/2476977)** (2022-02-04): @c8999c3f964f64 Yeah, defaultdict doesn't have a "get" method; the alternative that you get when the key is not present is automatically part of the `ddic2["optional"]` call
- **[c8999c 3f964f64](https://stackoverflow.com/users/11803687)** (2022-02-04): I'm actually going with this answer because the check for membership can be used as a ternary operator which bypasses the evaluation of the statement entirely, and can be turned into a slick one-liner, just like I was looking for       `value1 = dictionary2["optional"]["value1"] if "optional" in dictionary2 else " "`
- **[Ben Grossmann](https://stackoverflow.com/users/2476977)** (2022-02-04): @c I didn’t realize you could use if/else that way, neat! Glad my answer was helpful
