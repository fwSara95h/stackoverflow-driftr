---
title: "how can i hide whole table according to row count"
site: stackoverflow
question_id: 73237326
answer_id: 73835433
url: https://stackoverflow.com/a/73835433
author: Driftr95 (me)
author_url: https://stackoverflow.com/users/6146136
answered: 2022-09-24T07:23:06Z
last_edited: never
revisions: 1
revision_history: https://stackoverflow.com/posts/73835433/revisions
accepted: false
score: 0
chapter: G1
chapter_title: "JavaScript / DOM one-offs"
cluster: javascript-dom
helpers_referenced: []
license: my own text and code (also published on Stack Overflow under CC BY-SA 4.0)
retrieved_at: 2026-10-12T16:14:00Z
content_sha256: 9208c8a3f8a20c5413bc4f4663f995d3e37b217c1019041ab94ea4fabfd34359
commit_dated: answered (the commit holds the text as retrieved, i.e. the last revision, not the first)
status: as posted
---

# My answer — 2022-09-24

Posted by me ([Driftr95](https://stackoverflow.com/users/6146136)) on Stack Overflow, <https://stackoverflow.com/a/73835433>, 2022-09-24; score 0. Text as retrieved 2026-10-12.

Since I do not know the other question about this topic, I cannot know whether this will be any more helpful, but you could add a function like :

        function displayOneTable() {
            const cartTable = document.querySelector('table#sepettablo');
            const emptyTable = document.querySelector('table.sepetbos');
            //hopefully you only have 1 table with class='sepetbos' 
            //[would be better to set a unique id]

            var cartRows = cartTable.querySelectorAll('tr').length;
            if (cartRows > 0) {//use (cartRows>2) if header/total doesn't count
                emptyTable.setAttribute('hidden', true);

                cartTable.setAttribute('hidden', false);
                cartTable.removeAttribute('hidden');
            } else {
                cartTable.setAttribute('hidden', true);

                emptyTable.setAttribute('hidden', false);
                emptyTable.removeAttribute('hidden');
            }
        }


-- then you can call it once in your script so that in runs at when page is first rendered and also in whatever function/s remove (and/or add) rows from the cart table.
