---
title: "Why does soup=BeautifulSoup(data, \"html.parser\") work but soup2=... does not?"
site: stackoverflow
question_id: 75889461
answer_id: 75899772
url: https://stackoverflow.com/a/75899772
author: "Ghislain Fourny"
author_url: https://stackoverflow.com/users/284285
posted: 2023-03-31T14:36:54Z
last_edited: never
accepted: false
score: 0
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1d537531d92105617f7ae2df1eb00660db4a4d802492a804c94de20f3c08c3a8
role: another answer on the same question, kept as context; not my work
---

# Answer by [Ghislain Fourny](https://stackoverflow.com/users/284285) — 2023-03-31

Posted on Stack Overflow, <https://stackoverflow.com/a/75899772>, 2023-03-31. Licensed [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/); reproduced in full as context for my answer — the text is the author's. Retrieved 2026-10-12.

I do not recommend reading an Inline XBRL file at the level of XML or XHTML. Rather, it is highly recommended to use an XBRL processor, which will provide the XBRL semantics at the right level of abstraction.

The XBRL data model is based on data cubes, and by reading the data directly as XML, you are essentially re-building an XBRL processor from scratch.

For example, there is an open-source processor called Arelle and available in Python:

https://pypi.org/project/arelle/

Main project page: https://arelle.org/arelle/

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[henri.haiti](https://stackoverflow.com/users/21406103)** (2023-03-31): Thanks for the warning, you're absolutely right! But I tried Arelle and other XBRL-parsers and couldn't get them to work. So I figured if I have to understand XBRL better first to make those parsers work, I could just try to get as far as possible with writing my own parser and learning Python and XBRL while I'm doing that. Values, units, contextrefs, decimals and scales are working already without errors (tested it with 40 reports). Still struggling with label mapping but I'm getting there ;) But I'm sure there will be a point where I just switch to Arelle and call it a day
