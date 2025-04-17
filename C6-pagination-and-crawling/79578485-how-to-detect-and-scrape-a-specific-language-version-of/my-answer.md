---
title: "How to detect and scrape a specific language version of a multilingual publication, if available?"
site: stackoverflow
question_id: 79578485
answer_id: 79579163
url: https://stackoverflow.com/a/79579163
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2025-04-17T11:37:03Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/79579163/revisions
accepted: false
score: 2
chapter: C6
chapter_title: "Pagination and crawling"
cluster: scrape-pagination-crawling
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 49554e29bb63a360735e7650ad707de9d57296d832f1f6dd07f0d8372c721f77
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2025-04-17

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/79579163>, 2025-04-17; score 2. Text as retrieved 2026-10-12.

> ```
> def extract_details(item):
>     # Check if language attribute is English
>     lang = item.get("lang", "en")
>     if lang != "en":
>         return None  # Skip non-English
> ```

I don't think this bit is doing what you want it to. As far as I can tell, on this site, `.ds-artifact-item` elements don't *have* any `lang` attribute <sup>[ [view screenshot](https://i.sstatic.net/oTS8JETA.png) ]</sup>, but you're using `.get("lang", "en")` to set `lang` in your code so it just defaults to `"en"` and nothing gets filtered.

---

> ```
>     url = f"https://iris.who.int/discover?filtertype=dateIssued&filter_relational_operator=equals&filter=2025&rpp={RPP}&page={page_num}"
> ```

I would suggest filtering from the URL itself before you scrape, maybe something like:

```
    url = f"https://iris.who.int/discover?filtertype_1=dateIssued&filter_relational_operator_1=equals&filter_1=2025&filtertype_2=iso&filter_relational_operator_2=equals&filter_2=English&rpp={RPP}&page={page_num}"
```

(I expect you are more familiar with this site's filters than me and would know better if you need a different `filter_relational_operator` or `filter_2` value, but at a glance, this seems to work alright.)
