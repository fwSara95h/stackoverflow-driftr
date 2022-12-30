---
title: "python beautifulsoup - parsing an HTML table row"
site: stackoverflow
question_id: 74959245
answer_id: 74961683
url: https://stackoverflow.com/a/74961683
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-30T12:42:22Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74961683/revisions
accepted: true
score: 1
chapter: C4
chapter_title: "Tables into DataFrames"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 082e872fa4c09fc61a87734b0eba7d93967690a5b67315079fe3c989bce40547
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-30

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74961683>, 2022-12-30; **accepted**; score 1. Text as retrieved 2026-10-12.

> ```python
> Exception has occurred: KeyError
> 'class'
> ```

You could try to avoid the error with

```python
            if col.div:
                if not col.div.get('class'): continue
                print(f"{col.div['class']}")

```

---

> figure out the correct method to skip a td.div tag containing the attribute{'class': ['stars']}

(I'm assuming that by `td.div tag` you mean a `td` tag containing a certain type of `div`.)

If you use [`select`](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors) [instead of `find_all`] with [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.php), you can filter them out right from the start.

```python
        # for col in row.select('td:not(:has(div.stars)):not(:has(img))'):
        for col in row.select('td:not(:has(div.stars))'):
```

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Meghan M.](https://stackoverflow.com/users/9915864)** (2022-12-30): I tried  ```for col in row.select('td:not(:has(div.stars)):not(:has(img))'):``` which works! But it's a bit more convoluted than I want to have 4 months down the road.
- **me** (2022-12-31): @MeghanM. Would you find it more readable to stick with *`for col row.select('td'):`* and then start [inside the loop] with **`if col.select('div.stars, img'): continue`**?
- **[Meghan M.](https://stackoverflow.com/users/9915864)** (2022-12-31): Yes, that's exactly what I was looking for!! Making a note to use `.select()` more. Thank you so much!
- **me** (2022-12-31): @MeghanM. Glad to hear that! I find [soupsieve](https://facelessuser.github.io/soupsieve/selectors/pseudo-classes/#has) beautifully convenient and I'm a little bit happier every time I introduce someone to using it 😅
