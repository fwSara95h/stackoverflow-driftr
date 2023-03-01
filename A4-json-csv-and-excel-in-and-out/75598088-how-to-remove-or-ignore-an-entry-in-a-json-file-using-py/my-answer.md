---
title: "How to remove or ignore an entry in a JSON file using python?"
site: stackoverflow
question_id: 75598088
answer_id: 75599180
url: https://stackoverflow.com/a/75599180
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-01T02:54:27Z
last_edited: 2023-03-01T03:00:12Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75599180/revisions
accepted: false
score: 1
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: de0d2ed3730e8921b7f7ed84c15f531e700136367f1b867aaa87b110fd8c71cf
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-01

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75599180>, 2023-03-01, last edited 2023-03-01; score 1. Text as retrieved 2026-10-12.

> *So how can I delete entries with 'ipv6Prefix' or better to say, ignore them in my for loop?*

You can skip/ignore prefixes containing `ipv6Prefix` with `if...continue`:

```py
# import json
# with open('cloud.json') as f: data = json.load(f) ## safer than f=open...

with open ("ip.txt" ,'w') as d:
    for prefix_i in data['prefixes']:
        # if 'ipv6Prefix' not in prefix_i: d.write("{prefix_i}\n") ## OR
        if 'ipv6Prefix' in prefix_i: continue
        d.write("{}\n".format(prefix_i))
    ## list-comprehension INSTEAD OF for-loop:
    # d.write('\n'.join(str(p) for p in data['prefixes'] if 'ipv6Prefix' not in p)) 
```

<br>

You can write only prefixes containing `ipv4Prefix` with *`if 'ipv4Prefix' in...`*

```py
with open ("ip.txt" ,'w') as d:
    for prefix_i in data['prefixes']:
        if 'ipv4Prefix' in prefix_i: d.write("{}\n".format(prefix_i))
```

<br>

You can alter `data` itself to omit prefixes containing `ipv6Prefix` with [list comprehension](https://www.programiz.com/python-programming/list-comprehension):

```py
data['prefixes'] = [p for p in data['prefixes'] if 'ipv6Prefix' not in p]
```

<br>

You can save a list of prefixes containing `ipv4Prefix` as JSON with `json.dump`:
```py
## to just save the list as a variable:
# ipv4Prefixes = [p for p in data['prefixes'] if 'ipv4Prefix' in p]

with open('ipv4Prefixes.json', w) as f:
    json.dump([p for p in data['prefixes'] if 'ipv4Prefix' in p], f)
```

---
---

> *getting this error: `TypeError: list indices must be integers or slices, not str`*

That's probably due to the *`if [i]["prefixes"] == ['ipv6Prefix']:`* line; `[i]` is a **list** with just a single item [`i`, which is a dictionary], so *`[i]["prefixes"]`* just doesn't make any sense. You can use <kbd>`if 'ipv6Prefix' in i["prefixes"]`</kbd> instead, but there are more issues with what you're trying to accomplish in that block [I'll explain in the next section].

---

> ```py
> # for i in data['prefixes']...
>         data.pop(i)
> ```

The [`.pop`](https://www.programiz.com/python-programming/methods/list/pop) method only takes an **integer** as input [which has to be the **index** of the item you want to remove from that list], but `i` is a copy of a *dictionary* inside `data['prefixes']`, so *`.pop(i)`* would raise an error if there's an attempt to execute it. 

You could loop through [`enumerate`](https://docs.python.org/3/library/functions.html#enumerate)`(data['prefixes'])`<sup>(instead of just *`data['prefixes']`*)</sup> to keep track of the index associated `i`, but keep in mind that **looping through a list to `pop` multiple items [from that same list] is *NOT* advisable at all**. For example, if you pop the second item  from the list [index=1], then the indices of all items after it will decrease by one; so if you next need to pop what was *originally* the 5th item in the list, `enumerate` will tell you that its index is 4, but it actually became 3 after executing *`.pop(1)`*...

You *could* loop through the list in reverse as below (but isn't the list-comprehension approach I suggested before simpler?)

```py
for pi, p in enumerate(reversed(data['prefixes']), 1-len(data['prefixes'])):
    if 'ipv6Prefix' in p["prefixes"]: data['prefixes'].pop(pi)
```

<sup>Btw, instead of applying [`reversed`](https://www.programiz.com/python-programming/methods/built-in/reversed), you can also use [slicing](https://www.programiz.com/python-programming/examples/list-slicing) like `data['prefixes'][::-1]`. I just thought using the function is better for readability because it makes it very obvious what it's doing.</sup>

---
 
> ```py
>     if data[i]["prefixes"] == "ipv6Prefix":
> ```
>
> *for this one I get `TypeError: unhashable type: 'dict'` which is new to me*

`i` is a dictionary (which is unhashable, as the error message said), and therefore cannot be used as a key the way *`....data[i]...`* is trying to. 

---

> *so I get key error like this: `KeyError: 'ipv4Prefix'`*

probably from the `data['ipv4Prefix']` bit in the *`array = [i['prefix'] for i in data['ipv4Prefix']]`*, because `data` does not have a key `ipv4Prefix`; **some** `i`s in ***`for i in data['prefixes']`*** might, but there is **no point** in using <kbd>*`if 'ipv4Prefix' in i: del i`*</kbd> because `i` is a *copy* of an item in the list being looped though. 

You can try using [`.remove`](https://www.programiz.com/python-programming/methods/list/remove) like **`data['prefixes'].remove(i)`** [instead of *`del i`*], but I don't think that would be very efficient. List comprehension is definitely my preferred method in this case [and also probably considered the most "pythonic" approach here].

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Hosein Nikkhah](https://stackoverflow.com/users/21258013)** (2023-03-02): Thanks for the help, I tried your solution and it worked perfectly.
