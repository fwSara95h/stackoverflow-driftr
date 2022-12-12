---
title: "Parsing inline elements of a paragraph with BeautifulSoup & Python"
site: stackoverflow
question_id: 74778497
url: https://stackoverflow.com/q/74778497
asked: 2022-12-12T23:40:24Z
asked_by: "kevski"
asked_by_url: https://stackoverflow.com/users/17997098
last_edited: never
tags: [python, beautifulsoup, html-parsing]
score: 0
views_at_snapshot: 172
answer_count: 2
accepted_answer_id: none
closed: no
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 5d6c44a93b58df80c565e1546dde2a0c29ed01b136cbc07f9e140a11a9459257
---

# Parsing inline elements of a paragraph with BeautifulSoup & Python

Asked by [kevski](https://stackoverflow.com/users/17997098) on Stack Overflow, <https://stackoverflow.com/q/74778497>, 2022-12-12. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as the context of my answer — the text is the asker's. Retrieved 2026-10-12.

I have some text with some inlined span elements (icons)

```
<p>
  <span class="icon-water icon"></span>
  Some text...
  <span class="icon-steel icon"></span>
  some more text.
</p>
```

I need to write a function that will get me the text of this paragraph however I need to convert the icons to text.

```
<span class="icon-water icon"></span> => '{water}'
<span class="icon-steel icon"></span> => '{steel}'
```

Resulting string should be like:
```
{water} Some text... {steel} some more text.
```

How can I do this with python/bs4?
