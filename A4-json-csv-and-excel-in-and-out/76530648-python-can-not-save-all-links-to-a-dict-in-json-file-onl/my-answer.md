---
title: "Python: can not save all links to a dict in json file, only the last one"
site: stackoverflow
question_id: 76530648
answer_id: 76530840
url: https://stackoverflow.com/a/76530840
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-06-22T10:14:14Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/76530840/revisions
accepted: false
score: 0
chapter: A4
chapter_title: "JSON, CSV and Excel in and out"
cluster: nested-json-dict-wrangling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9eb2bd5a1d267fde7d195cb94932a1fa614d459403fce6c37a375a0265f9fa6b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-06-22

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/76530840>, 2023-06-22; score 0. Text as retrieved 2026-10-12.

There are several issues:

---

> ```py
>     all_links_dict = {}
>     for item in name_link:
>         value_links = ("https://www.sothebysrealty.com" + item.get("href"))
>     all_links_dict[number + 1] = value_links
> ```

You're not updating `number` at any point, so only a value keyed to `1` gets saved every loop. Either use some derivation of `page_number` updates itself in each iteration, or add a line to increment `number` and bring it inside the inner loop.

```py
    all_links_dict = {}
    for item in name_link:
        value_links = ("https://www.sothebysrealty.com" + item.get("href"))
        number += 1
        all_links_dict[number] = value_links
```

---

> ```py
>     with open("all_links_dict.json", "w", encoding="utf-8-sig") as file:
>         json.dump(all_links_dict, file, indent=4, ensure_ascii=False)
> ```

You should use `mode="a"` instead of `"w"` to append instead of over-writing in each iteration. However, you should be aware that the file will not be valid json (ie, you can't decode it any more) after a second iteration. Might be better to have a list that you append to every time and then write the list to json after (or at the end of) the loop.

---

**There's also the fact that *`for page_number in range(1, 2):`* will only lead to one iteration (where `page_number` is 1), so even with all this, only one page's info will be saved unless the range is expanded to include more pages.**
