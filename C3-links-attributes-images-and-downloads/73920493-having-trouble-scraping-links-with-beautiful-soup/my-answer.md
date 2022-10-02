---
title: "having trouble scraping links with beautiful soup"
site: stackoverflow
question_id: 73920493
answer_id: 73928663
url: https://stackoverflow.com/a/73928663
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-02T19:18:05Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73928663/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 840f268a958f79901bcad8fa7c5bdf0f662d2de50f955717c4244406e9a2b2ef
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-02

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73928663>, 2022-10-02; score 0. Text as retrieved 2026-10-12.

You have a list of `li` tags which have no `href` attribute - the `href` attribute is of the `a` tags, which are wrapped as list items.

You can either get the `href`s like this:

    links_h = [link.find('a').get("href")for link in house if link.find('a')]

**OR** you can try getting the a tags directly as 

    house = committee[0].select("li > a")
so that the `[link.get("href")for link in house]` part works.
