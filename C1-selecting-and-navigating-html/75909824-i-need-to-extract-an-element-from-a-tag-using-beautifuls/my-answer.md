---
title: "I need to extract an element from a tag using BeautifulSoup4"
site: stackoverflow
question_id: 75909824
answer_id: 75910101
url: https://stackoverflow.com/a/75910101
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-04-02T04:20:49Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/75910101/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 437dc61a0b4cfbf6aeebe24f13218566d5908cf40619df33f4bcd478ef1cf333
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-04-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75910101>, 2023-04-02; **accepted**; score 0. Text as retrieved 2026-10-12.

You can get any [tag attribute](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#bs4.Tag.attrs) by treating it like a dictionary - with [`<Tag>.get(<attr>)`](https://www.programiz.com/python-programming/methods/dictionary/get) [if you're not sure the element will have that attribute] or `<Tag>[<attr>]` [if you *are* sure that the element has that key].

If you find the element with

```
date = cmbs_soup.find('input', title='Select as of date', type='text', value=True) # OR
# date = cmbs_soup.select_one('input.mm-date-field.form-control.input-sm.date-picker[title="Select as of date"][type="text"][value]')
```

then you can get the `value` attribute with `date['value']` or `date.get('value')` or `date.attrs['value']` or `date.attrs.get('value')`.

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[WhoIsJonGalt](https://stackoverflow.com/users/1565926)** (2023-04-02): Amazing! I was thinking about this all wrong. Thank you!
