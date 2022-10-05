---
title: "How to find all elements within specific div ID in Beautiful Soup and Selenium"
site: stackoverflow
question_id: 73952815
answer_id: 73957068
url: https://stackoverflow.com/a/73957068
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-10-05T07:28:09Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73957068/revisions
accepted: false
score: 0
chapter: C7
chapter_title: "JavaScript-rendered pages: Selenium and friends"
cluster: scrape-js-rendered-selenium
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: b61af6b2eac812a81a0f1a889da03a2404dcc3a4d80843bfa40cf7efc716d164
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-10-05

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73957068>, 2022-10-05; score 0. Text as retrieved 2026-10-12.

Well, there *isn't* any test inside the div with id="experience" - the data you want is *after* that. So maybe try something like

    expAnchor = soup.find(id="experience")
    if expAnchor: #to avoid error, in case expAnchor = None
        expContainer = expAnchor.find_next('div', {"class": "pvs-list__outer-container"}) 

Or, you could use [css selectors](https://www.w3schools.com/css/css_combinators.asp) and get it in one call like:

    expContainer = soup.select_one('#experience ~ div.pvs-list__outer-container')
