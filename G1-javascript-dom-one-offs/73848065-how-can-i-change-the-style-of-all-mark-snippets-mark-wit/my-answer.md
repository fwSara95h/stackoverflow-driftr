---
title: "How can I change the style of all <mark>snippets</mark> within html using javascript?"
site: stackoverflow
question_id: 73848065
answer_id: 73848324
url: https://stackoverflow.com/a/73848324
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-25T22:53:53Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73848324/revisions
accepted: true
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 7bb789db995827a0218c1cc5eb5c8684c9a653570053c0d86f90474aff79a33a
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-25

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73848324>, 2022-09-25; **accepted**; score 1. Text as retrieved 2026-10-12.

Sometimes I use this function :

    function changeStyleProperty(ssIndex, selTxt, pName, pVal) {
        const cssRules = document.styleSheets[ssIndex].cssRules;
        for (let i = 0; i < cssRules.length; i++) {
            if (cssRules[i].selectorText === selTxt) {
                cssRules[i].style.setProperty(pName, pVal);
            }
        }
    }
You can use `changeStyleProperty(ssIndex, 'mark', 'text-weight', 'bold')` to bold, and then `changeStyleProperty(ssIndex, 'mark', 'text-weight', 'normal')` to change back.

(If you have only one stylesheet / style block then you can just use `ssIndex=0`, otherwise you might need to check [maybe with `console.log(document.styleSheets);`] and find out which stylesheet your `mark` rule is in.)
