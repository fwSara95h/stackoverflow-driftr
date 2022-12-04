---
title: "print contents of remaining tags after a tag beautifulsoup"
site: stackoverflow
question_id: 74677516
answer_id: 74678043
url: https://stackoverflow.com/a/74678043
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-04T15:29:26Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74678043/revisions
accepted: false
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 002193541fe16c137f74334166c199b9d2d1aab908acdeabf7d9c6f6d808ac88
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74678043>, 2022-12-04; score 0. Text as retrieved 2026-10-12.

You can try this:
```python
for li in soup.select("li:not(li li)"): 
    print(" ".join([
        d.get_text().strip() for d in li.descendants 
        if 'NavigableString' in str(type(d)) and 
        d.parent.name == 'li' and d.get_text().strip()
    ])) 
    print("--sep--")

# for the p tags after ANY of the [outermost] li tags
for p in soup.select("li:not(li li) ~ p"):  print(p.text.strip(), "\n--sep--") 
```
(Using `:not(li li)` lets you not need the `if li.find_parent("li"): continue` part.)

This should get you 
- the text from [outermost] `li` tags, but only made up of strings that are **directly** inside that `li` tag or an `li` tag inside it

and then
- text from `p` tags that are [sibling to a preceding](https://facelessuser.github.io/soupsieve/selectors/combinators/#general-sibling-combinator) outermost `li` tag. (If you want only `p` tags after the *last* `li`, use `for p in soup.select("li:not(li li) ~ p:not(:has(~ li))")...`)

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Ajay Surya Senthilrajan](https://stackoverflow.com/users/20681043)** (2022-12-05): do i need to change the parser or something? this prints only  --sep--  --sep--  --sep--
- **me** (2022-12-05): @AjaySuryaSenthilrajan maybe try `html5lib` parser? [I actually didn't pass any parser argument at all when testing (sorry I forgot to mention that), but even just installing html5lib made a difference to the results I used to get from soupsieve]
