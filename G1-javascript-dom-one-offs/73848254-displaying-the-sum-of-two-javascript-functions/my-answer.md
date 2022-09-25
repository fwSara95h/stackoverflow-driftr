---
title: "Displaying the sum of two Javascript Functions"
site: stackoverflow
question_id: 73848254
answer_id: 73848436
url: https://stackoverflow.com/a/73848436
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-25T23:23:03Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73848436/revisions
accepted: false
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 76ca10e35c15c92776e448842f161142b87b72d4a7ed34af2e6d17d02a6fa968
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73848436>, 2022-09-25; score 1. Text as retrieved 2026-10-12.

You should either return the values at the end of `firstSum` and `groPay` or change `grandTotal` to something like

    function grandTotal(){
      firstSum(); groPay();
      const fs = document.getElementById('result1').value;
      const gp = document.getElementById('result2').value;
      document.getElementById('result').value = fs + gp;
    }
