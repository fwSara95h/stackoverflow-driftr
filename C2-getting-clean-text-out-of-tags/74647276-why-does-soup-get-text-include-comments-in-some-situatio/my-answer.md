---
title: "Why does soup.get_text() include comments in some situations?"
site: stackoverflow
question_id: 74647276
answer_id: 74672659
url: https://stackoverflow.com/a/74672659
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-12-04T03:34:00Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/74672659/revisions
accepted: true
score: 1
chapter: C2
chapter_title: "Getting clean text out of tags"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 04c697917778d62a9cd1e35f1d9d9bb686a7513849fb48ba167ab3d13ef2890b
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-12-04

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/74672659>, 2022-12-04; **accepted**; score 1. Text as retrieved 2026-10-12.

I can't reproduce the issue [running your code just returns `\n\n\n\n\n\n\n\n\n\xa0\n\n\n\n` for me <sub>(bs4 4.11.1, python 3.7.15, IPython 7.9.0)</sub>], but I expect it's because everything inside the `style` tag is stored as one `Stylesheet` element rather than being further parsed into Tag/NavigableString/Comment/etc

[![stylesheet vs comment][1]][1]


I don't think that's a valid html anyway - stylesheet comments should be like `/*Some Comment*/`, and you can't just put html inside a stylesheet like that...

  [1]: https://i.sstatic.net/kIzma.png

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[Peter](https://stackoverflow.com/users/968132)** (2022-12-05): I'm going to close this since 2 people haven't been able to reproduce. Thanks for taking a look anyway!
- **me** (2022-12-05): @Peter thanks for accepting my answer, but your comment indicates that you were maybe hoping for something a bit more helpful. Since your question only asked *why*, I just offered a possible explanation, but if you want to have more control over the text you extract, you can use something like [this function](https://pastebin.com/fh4P45iE), which will let you skip all style tags if you call it like `html_to_text(soup, specialTags={'style': ['""']})`
- **me** (2022-12-05): (you could even modify the function to parse inside `style` tags like normal html, but please remember that **html is not recognized inside `style` tags** - they should only contain css)
- **[Peter](https://stackoverflow.com/users/968132)** (2022-12-05): Yeah, that added invalid HTML inside style tags bit seems to be an interesting feature of the Words Doc to HTML conversion
