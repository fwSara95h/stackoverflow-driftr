---
title: "How to extract the details from particular HTML text"
site: stackoverflow
question_id: 75410558
answer_id: 75410757
url: https://stackoverflow.com/a/75410757
author: "Corralien"
author_url: https://stackoverflow.com/users/15239951
posted: 2023-02-10T11:52:18Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: ba234741e64dafe2056fb146ff92e08d127e83f6697ffcfed239faaf1985d845
role: another answer on the same question, kept as context; not my work
---

# Answer by [Corralien](https://stackoverflow.com/users/15239951) — 2023-02-10

Posted on Stack Overflow, <https://stackoverflow.com/a/75410757>, 2023-02-10. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

You can search for `a` tag where `href` starts with `https://maps.google.com`:

```
>>> soup.find('a', {'href': re.compile('^https://maps.google.com')}).text.replace('\n', ' ')
'1183 Pelham Wood Dr, Rock Hill, SC 29732'
```

The important thing here is not the `soup` object used but the strategy with a regexp to extract the address text from the tag.
