---
title: "select element that is created by insertAdjacentHTML for adding or remove class"
site: stackoverflow
question_id: 73873818
answer_id: 73875491
url: https://stackoverflow.com/a/73875491
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-28T02:11:07Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73875491/revisions
accepted: true
score: 1
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9339b1d1ed2d2356728bf9c3409222aa0fff11f36efa7f02ae4c77cc58034c50
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-28

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73875491>, 2022-09-28; **accepted**; score 1. Text as retrieved 2026-10-12.

I think your commented code is better, but if you want to stick with the `insertAdjacentHTML`, you can alter to something like this:

        var liClass, cBtnInner;
        if (todo.complete) {
            liClass = 'uncompleted well';
            cBtnInner = 'UnComplete';
        } else {
            liClass = 'completed well is';
            cBtnInner = 'Complete';
        }
        todoListElem.insertAdjacentHTML(
            'beforeend', 
            '<li class="' + liClass + '"><label>' + todo.title + 
                '</label><button class="btn btn-success" onclick="editTodo(' + 
                todo.id + ')">' + cBtnInner + 
                '</button><button class="btn btn-danger" onclick="removeTodo(' + 
                todo.id + ')">Delete</button></li>'
        );

## Comments on this answer

*Comments are their authors' and licensed CC BY-SA 4.0; names link to the authors' profiles.*

- **[joyi61](https://stackoverflow.com/users/19601673)** (2022-09-28): it worked :) thanks ** Driftr95** ,  thank youuu
- **me** (2022-09-28): @joyi61 glad to have helped!
