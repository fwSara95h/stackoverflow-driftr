---
title: "How to extract the url from a website when the url gets abbreviated in the chrome console?"
site: stackoverflow
question_id: 75043783
answer_id: 75044717
url: https://stackoverflow.com/a/75044717
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2023-01-08T00:27:01Z
last_edited: 2023-01-08T00:38:46Z
revisions: 2
revision_history: https://stackoverflow.com/posts/75044717/revisions
accepted: false
score: 0
chapter: C3
chapter_title: "Links, attributes, images and downloads"
cluster: scrape-static-html-bs4
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 1a9e972bf528bd6d420f1b5bd7cd6d947b485ab0df384ca6cc2e3d718bd3dda6
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2023-01-08

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/75044717>, 2023-01-08, last edited 2023-01-08; score 0. Text as retrieved 2026-10-12.

<sub>Why not just copy it from the address bar after clicking on it if it *"takes [you] to the desired link"*?</sub> 

If you mean [something like this](https://i.sstatic.net/XUlAx.jpg), then **after clicking on the element** (in dev tools), 
1. go to the "Properties" tab (it should be to a side or at the bottom) and then 
2. right click on the `href` property and 
3. select "Copy string contents"

OR:
1. right click on the `href` attribute [in the "Elements" tab](https://i.sstatic.net/VPJbh.png) itself and 
2. click on "Edit attribute" and it should automatically [select the whole link](https://i.sstatic.net/vGGRE.png), and 
3. then you can either `CTRL`+`C` or right-click and select "Copy".

---

> I tried to use a f string and it didn't work to estimate what the string would be.

That's not [how f-strings are meant to be used](https://realpython.com/python-f-strings/#simple-syntax) - they do not [and cannot] estimate unknown entities - you have to specify pre-existing variables to fill them.
