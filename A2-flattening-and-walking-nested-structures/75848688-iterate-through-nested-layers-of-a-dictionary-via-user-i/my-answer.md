---
title: "Iterate through nested layers of a dictionary via user input python"
site: stackoverflow
question_id: 75848688
answer_id: 75850955
url: https://stackoverflow.com/a/75850955
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-03-26T22:38:37Z
last_edited: 2023-03-26T22:59:20Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75850955/revisions
accepted: false
score: 0
chapter: A2
chapter_title: "Flattening and walking nested structures"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: e7c021fb44c465b4f8338a8575b901d3e1bb9b92da9da639a6040430ffd0c798
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-03-26

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75850955>, 2023-03-26, last edited 2023-03-26; score 0. Text as retrieved 2026-10-12.

Your desired chain of events isn't very clear from your code, but I suppose you could use something like this function

```py
def traverse_choices(q_ch:dict): 
    while isinstance(q_ch, dict):
        print(q_ch['0'])
        if (user_resp:=input("Select an option: ")) not in ['R', *q_ch]:
            print('Invalid selection. Please enter a valid option [or "R" to exit].')
            continue
        if user_resp=='R': return 'R'
        if user_resp!='0': q_ch = q_ch[user_resp]
    print(q_ch)
```

and maybe utilize it as below

```py
            qloop = traverse_choices(data[i]["system"]) ## will return "R" or None
        if qloop != "R": break
        continue ## ONLY IF THERE IS ANYTHING AFTER IT [IN THE OUTER LOOP] TO SKIP
    #### REST OF OUTER LOOP #### 
```

[I'm assuming that the *`if qloop == "R": continue` `else: break`* part in your code snippet is nested inside a conditional block inside another loop, because there is no point in having anything in a loop after an unconditional `break` or `continue`...]

[![op][1]][1]

---

About 

> ```py
>         if qloop == "R":
>             continue
>         else:
>             break
> ```


**Note that you don't need to use `else` after `if...break` or `if...continue`;** and if there's nothing in the loop after `break`, you can just use <kbd>**`if qloop != "R": break`**</kbd>.



  [1]: https://i.sstatic.net/sEzwQ.png
