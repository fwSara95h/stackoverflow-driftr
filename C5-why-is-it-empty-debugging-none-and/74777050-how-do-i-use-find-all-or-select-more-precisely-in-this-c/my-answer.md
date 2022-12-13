---
title: "How do I use find_all or select more precisely in this case?"
site: stackoverflow
question_id: 74777050
answer_id: 74779366
url: https://stackoverflow.com/a/74779366
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-13T02:28:10Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74779366/revisions
accepted: true
score: 1
chapter: C5
chapter_title: "Why is it empty? Debugging None and []"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1063bf3ffa710430ef35d31161a84b14be309d979310edd67db22728c8e733d3
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-13

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74779366>, 2022-12-13; **accepted**; score 1. Text as retrieved 2026-10-12.

If your issue is that you're getting a list of lists, and you just want a flat list, then you should do it like

```python
            for test2 in soup.find_all(class_="fighter left_side"): 
                Fighter1Main += [t for t in test2.find_all(itemprop="url")]
```

but since you weren't happy with the output from *`for test2 in soup.select('.fighter.left_side [itemprop="url"]'): Fighter1Main.append(test2)`*, and from your title, I'm guessing that isn't the the problem here.

---

If you want to filter out any tags that have a nested tag inside them then you can add `:not(:has(*))` to your selector

```python
            for test2 in soup.select('.fighter.left_side *[itemprop="url"]:not(:has(*))'): 
                Fighter1Main.append(test2)
```

however, you can **expect an empty list** if you do this because [as far as I can tell] all tags matched to `.fighter.left_side *[itemprop="url"]` *will* have an `img` tag nested within.

---
---

If you *really* want something like your expected output, you'll have to either alter the `soup` or build it up yourself.

---

You can either remove everything inside the Tags with `itemprop="url"` [original `soup` object will be altered]:

```python
            for test2 in soup.select('.fighter.left_side *[itemprop="url"]'): 
                test2.clear()
                Fighter1Main.append(test2) 
```

---

Or you could form new html tags with only the `href` [if there is any] and `itemprop` attributes [original `soup` object will remain unaltered, but you'll be parsing and extracting again for each item]:

```python
            soup = BeautifulSoup(response, "html.parser")
            Fighter1Main += [BeautifulSoup(
                f'<{n}{h} itemprop="url"></{n}>', "html.parser"
            ).find(n) for n, h in [(
                t.name, '' if t.get("href") is None else f' href="{t.get("href")}"'
            ) for t in soup.select('.fighter.left_side *[itemprop="url"]')]]
```
