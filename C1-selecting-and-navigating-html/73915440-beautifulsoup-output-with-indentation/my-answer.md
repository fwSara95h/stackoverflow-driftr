---
title: "Beautifulsoup output with indentation"
site: stackoverflow
question_id: 73915440
answer_id: 73932397
url: https://stackoverflow.com/a/73932397
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-03T07:38:22Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73932397/revisions
accepted: true
score: 0
chapter: C1
chapter_title: "Selecting and navigating HTML"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 8c3a2159ee9aa9ad7558bf9d7300737af143bf0b74a8d2ddeb6354aeb17fc8ef
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-03

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73932397>, 2022-10-03; **accepted**; score 0. Text as retrieved 2026-10-12.

You can define a dictionary of indents/prefixes

    preString =  {'h1': '', 'h2': '\t', 'h3':'\t\t', 'h4':'\t\t\t'}
then you can just loop and print like:

    tags = soup.find_all([t for t in preString])
    for soups in [t for t in tags if t.string]:
        print(preString[soups.name]+soups.string)

I filtered with `if t.string` in case they have tags inside rather than just text. Using `.text` gets you the full text regardless of child tags; if you want that, and you want your `find_all` to be independent, you can instead:

    tags = soup.find_all(['h1', 'h2'])
    for soups in tags:
        preStr = preString[soups.name] if soups.name in preString else ''
        print(preStr+soups.string)
(You can add a default indent/prefix after the `else` when defining `preStr`)
